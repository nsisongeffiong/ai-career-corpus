#!/usr/bin/env python3
"""Corpus publish gate.

Run this against any tree you are about to push to a PUBLIC remote (this
template, a fork, or anything derived from a corpus). The unfilled template
passes. A filled corpus should FAIL loudly - that is the point: if this
script finds your PII, the tree is not publishable. If your filled corpus
somehow passes, your private-terms.txt blocklist is too thin.

Checks, over all git-tracked files:
  1. Binary documents tracked (.docx/.pdf/.xlsx/.zip/images) - should be gitignored.
  2. Email addresses (anything@domain, except example.com/example.org).
  3. Phone-shaped numbers (NA formats).
  4. Secret-shaped strings (AWS key IDs, private key blocks, common token prefixes).
  5. Terms from private-terms.txt, one per line, case-insensitive - keep YOUR
     blocklist there (your name, employers, clients); the file itself is gitignored.
  6. Leftover FICTIONAL EXAMPLE markers (unfilled template files). Warning by
     default; pass --no-fictional to make it a failure once your corpus is filled.

Exit code 0 = clean, 1 = findings.

Usage:
    python3 scripts/validate_corpus.py [--no-fictional]
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()

BINARY_EXTS = {".docx", ".pdf", ".xlsx", ".xls", ".zip", ".png", ".jpg", ".jpeg", ".pptx"}

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@(?!example\.(?:com|org))[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"\b(?:\+?1[-.\s])?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b")
SECRET_RES = [
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),                  # AWS access key id
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),     # PEM private key
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),               # GitHub token
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),       # Slack token
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),              # generic sk- API key
]
# Built by concatenation so this script never flags itself if content-scanned.
FICTIONAL_MARKER = "FICTIONAL " + "EXAMPLE"


def tracked_files():
    try:
        out = subprocess.run(
            ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout
        return [ROOT / line for line in out.splitlines() if line.strip()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def main():
    strict_fictional = "--no-fictional" in sys.argv
    findings, warnings = [], []

    private_terms = []
    terms_file = ROOT / "private-terms.txt"
    if terms_file.exists():
        # Word-boundary match, so "vale" doesn't fire inside "equivalent".
        private_terms = [
            (t.strip(), re.compile(r"\b" + re.escape(t.strip()) + r"\b", re.IGNORECASE))
            for t in terms_file.read_text(encoding="utf-8").splitlines()
            if t.strip() and not t.startswith("#")
        ]
    else:
        warnings.append(
            "no private-terms.txt found - create one (gitignored) listing your name, "
            "employers, and clients so this check has teeth"
        )

    for path in tracked_files():
        rel = path.relative_to(ROOT)
        if path.suffix.lower() in BINARY_EXTS:
            findings.append(f"{rel}: binary document is git-tracked (should be gitignored)")
            continue
        if path.resolve() == SELF:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for lineno, line in enumerate(text.splitlines(), 1):
            for m in EMAIL_RE.finditer(line):
                findings.append(f"{rel}:{lineno}: email address: {m.group(0)}")
            for m in PHONE_RE.finditer(line):
                findings.append(f"{rel}:{lineno}: phone-shaped number: {m.group(0)}")
            for sre in SECRET_RES:
                if sre.search(line):
                    findings.append(f"{rel}:{lineno}: secret-shaped string ({sre.pattern[:24]}...)")
            for term, term_re in private_terms:
                # LICENSE copyright attribution is intentionally real - exempt.
                if rel.name != "LICENSE" and term_re.search(line):
                    findings.append(f"{rel}:{lineno}: private term: {term}")
            if FICTIONAL_MARKER in line:
                msg = f"{rel}:{lineno}: leftover {FICTIONAL_MARKER} marker (unfilled template)"
                (findings if strict_fictional else warnings).append(msg)

    for w in warnings:
        print(f"WARN  {w}")
    for f in findings:
        print(f"FAIL  {f}")
    print(f"\n{len(findings)} finding(s), {len(warnings)} warning(s).")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
