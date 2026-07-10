# Operational History

Generation log and operational records. **Generation sessions never read this file to produce an artifact** — it exists so the working files (`CLAUDE.md`, the numbered corpus files) stay lean, and so forensic questions ("when did we correct that metric?", "which archive was already mined?") have answers.

What belongs here:

- **Generation log** — one line per artifact generated: date, company/role, which STAR story the cover letter spent, anything flagged.
- **Corrections log** — when a fact in the corpus is corrected (a metric re-verified, an attribution fixed), record the old value, the new value, and why. The corpus files keep only the corrected fact; the history of the error lives here.
- **Mining records** — which archives/sources have been fully mined into the corpus, and when, so no future session re-reads them.
- **Incident log** — when a generation rule fails in practice (e.g. a draft ships with an AI tell, a fabricated detail slips through), record it and note which hard check was added in response. Rules become checks by accumulating incidents.

---

## Generation log

| Date | Artifact | Target | Notes |
|---|---|---|---|
| | | | |

## Corrections log

| Date | File | Old → New | Why |
|---|---|---|---|
| | | | |

## Mining records

- [ ] [Source] — mined [date] — never re-read

## Incident log

<!-- FICTIONAL EXAMPLE rows below — delete and replace with your own. They show the pattern: an incident is only "closed" when it produces a deterministic check, not a stronger rule. -->

| Date | What failed | Check added |
|---|---|---|
| 20XX-03 | Resume shipped with 17 em dashes despite the no-em-dash rule | Mandatory post-render U+2014 scan of `word/document.xml`; count in prose must be 0 |
| 20XX-04 | Cover letter confidently used the client's *plausible but wrong* legal name | Grounding rule hardened: company-side facts only from the JD or the user, never model knowledge |
| 20XX-05 | Draft bolded keywords inside bullets; read as keyword-stuffing | Bold banned from drafting markdown entirely, so draft == render with no stripping step |
