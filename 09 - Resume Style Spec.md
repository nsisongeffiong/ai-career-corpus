# Resume Style Spec — Canonical Rendering Contract

The exact .docx formatting for every generated resume. **Read this; never reverse-engineer formatting by parsing an existing .docx** (wasteful and fragile). Derive it once from your best reference resume, then treat this file as the contract.

## Page & font

- **Font:** [e.g. Calibri] throughout
- **Name:** [e.g. 17pt], bold
- **Section headings:** [e.g. 11.5pt], bold, with a bottom border/rule under the heading
- **Body text (bullets, summary, competencies, certs):** [e.g. 10.5pt], plain
- **Margins:** 1 inch all sides (standard)
- **Length target:** [1 or 2] pages

## What is BOLD (structure only)

1. Name (top of document)
2. Section headings: `SUMMARY`, `CORE COMPETENCIES`, `PROFESSIONAL EXPERIENCE`, `EDUCATION`, `CERTIFICATIONS`, `ADDITIONAL EXPERIENCE`
3. Each job's `Company — Title` line, and its date (date right-tabbed on the same line)
4. Each degree-name line (institution stays plain)

## What is PLAIN (never bold)

- Contact line · summary paragraph · competencies list · **all experience bullets, including every keyword and metric inside them** · location lines (italic) · institution names · certifications list

**The bold mistake to never repeat:** adding inline bold to keywords/metrics inside bullets, on top of the structural bold, reads as keyword-stuffing. Drafting markdown must NOT put `**…**` on in-bullet text at all — drop draft-level inline emphasis entirely so the markdown draft and the rendered .docx always match, with no stripping step to get wrong.

## Layout conventions

- **Contact:** centered, up to TWO separate lines (each its own paragraph — NEVER chain everything onto one line; it overflows and wraps ugly):
  - **Line 1 (always):** `[phone]  |  [email]  |  [City, Region]  |  linkedin.com/in/[handle]`
  - **Line 2 (only for engineering / technical / content roles):** `github.com/[handle]  |  [yoursite.com]`
  - Values are canonical from `00 - Contact and Header.md`.
- **Experience entry order:** `Company — Title` (bold) with date right-tabbed; **location on the next line, italic, full region name**
- **Dates:** `MMM YYYY – MMM YYYY` (en dash); current role ends "Present"
- **Education:** degree name bold, institution plain, year present
- **Section heading text** exactly as listed above (ATS parsers key on these)

## Punctuation — NO em dashes (AI tell)

**Zero em dashes (—, U+2014) in PROSE** — the summary paragraph, every experience bullet, the competencies list, and all cover-letter sentences. Heavy em-dash use is one of the most recognizable signatures of AI-generated text; a recruiter clocks it instantly. The corpus content (Spine/Wins) is written with em dashes for internal readability — **the drafter must convert them when composing**, not copy them through. Rewrite each with: a period (two sentences), a comma, parentheses, or a colon.

- **Structural separators are exempt:** the experience-header `Company — Title` and the education `Degree — Institution` lines may keep their em dash (typography, not prose). These are the only places an em dash is allowed.
- **Clean deterministic check:** all structural lines (name, headings, headers, degrees) are bold; all prose (summary, bullets, competencies, certs) is not. So **prose em-dashes = em dashes in NON-BOLD paragraphs, and that must be 0.**
- **En dashes (–, U+2013)** only in ranges — dates "Sep 2024 – Present", comp "$120,000 – $140,000". Never as a sentence connector.
- **Mandatory render-time check** (like the metadata scrub in `CLAUDE.md`): scan `word/document.xml` for U+2014; **the count must equal the number of structural header lines — i.e., zero in prose.** Any em dash inside a bullet, the summary, or a cover-letter sentence = rewrite and re-render before the draft is done. Experience shows the rule alone fails repeatedly (drafts kept shipping with double-digit em-dash counts until the scan was made mandatory); only the deterministic check holds.

## ATS rules (also in CLAUDE.md)

- No tables, columns, text boxes, headers/footers, images, graphics
- Contact in the body, not a header/footer
- Author/title metadata set to the candidate's name (never "python-docx")
- .docx unless the posting asks for PDF

## Generation note

python-docx renders this spec directly — no need to read any existing .docx. If a reusable generator script is saved, keep it in this corpus folder, not in temp.
