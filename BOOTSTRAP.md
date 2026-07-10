# Bootstrapping the Corpus from Historical Resumes

You don't start a corpus from a blank page. Most people sit on years of accumulated resume versions — dozens of them, each tailored to some job — plus old cover letters, LinkedIn exports, performance reviews, and project folders. Those contain hundreds of bullets you already wrote. The bootstrap is a **one-time distillation**: point an AI agent at that archive and extract it into the corpus files.

## How to run this (you don't do the phases — the agent does)

This file is written **for the AI agent**. Your part:

1. Put your old resumes, cover letters, and exports in a folder the agent can read.
2. Open your corpus folder in an AI coding agent (e.g. Claude Code) and say: *"Run BOOTSTRAP.md against `<that folder>`."*
3. Answer its questions. The agent does the reading, extraction, and drafting; **you are the verification gate** — expect batched confirm-or-correct questions in chat (Phases 3–5), not homework.

**Agent:** work the phases in order; where a fact isn't in the sources, write a `*[verify]*` or `*[to fill]*` marker and move on — never guess mandates, team sizes, or dates. **No archive to mine?** Skip Phases 1–2's mining and interview instead: walk the user role by role through the `01 - Career Spine.md` template in chat (mandate, achievements, numbers, stack), then continue from Phase 3 as normal — interview answers still need the same verification discipline.

The catch that shapes the whole process: **JD-tailored resumes inflate.** They stretch dates, round metrics up, borrow adjacent tools, and misattribute wins to whichever role the JD favored. So bootstrapping is extraction *plus verification* — the archive is a lead-generator, never a source of truth.

## Phase 0 — Gather sources (once)

Collect into one place: every archived resume version, old cover letters, a LinkedIn data export, performance reviews, and any project folders/emails that document side ventures. **Convert binaries to text once** — extracting the same .docx in every future session is the cost sink this repo's cost rules exist to prevent.

## Phase 1 — Seed the spine from 2-3 recent resumes with different lenses

Pick your most recent resumes that were tailored to *different kinds* of roles (e.g. one engineering-angled, one management-angled). **Different lenses surface different achievements** — the same role reads completely differently through each, and you want both sets of bullets in the spine.

Build `01 - Career Spine.md` from them: one entry per role, achievements in Context → Action → Result form, tagged. **Mark everything unverified at this stage** — the seed comment in the spine should say which resumes it came from, so later sessions know the provenance — and use `*[verify]*` markers for anything the resumes don't answer (mandate, team size, reporting line) rather than inventing it.

## Phase 2 — Mine the full archive into the Wins Bank

Now sweep everything else. For each archived resume: find any bullet containing a number, paste it into `04 - Quantified Wins Bank.md` in standard format, tag it, move on. Capture first, polish later — the goal is coverage (50-100 wins), not prose. Deduplicate as you go; the same win appears across many resume versions with drifting numbers, and **when versions disagree, that's a flag for Phase 3, not a choice for the agent to make silently.**

## Phase 3 — The verification pass (the step that makes the corpus trustworthy)

Sit with the user and go claim by claim. Batch the questions — "confirm or correct these 15 numbers" beats 15 interruptions. For each win:

- **Confirm, correct, or kill.** Cross-check against performance reviews or project notes where possible. Delete anything that turns out to be ATS decoration (a tool listed once for keyword-matching that was never actually used — kill it and add it to Known Gaps instead).
- **Fix attributions.** Mined bullets routinely land under the wrong role/era. When a metric belongs to one employer and could plausibly be misfiled under another, write an **attribution lock** on the win ("attribute to Role A, never Role B").
- **Apply the interview-math test.** A percentage that sounds great but doesn't survive a whiteboard recomputation in an interview gets replaced with **canonical resume phrasing** recorded on the win itself, with the legacy phrasing explicitly banned.
- **Log corrections in `HISTORY.md`** — the corpus keeps only the corrected fact; the history of the error lives in the log.

Annotate verified items ("user-confirmed [date]") so future sessions can tell validated facts from estimates.

## Phase 4 — Derive the Skills Matrix

Build `02 - Skills Matrix.md` *from* the verified spine and wins — every skill row cites its evidence. Then a second user pass: validate years/recency/proficiency, set the **do-not-overclaim ceilings**, and seed **Known Gaps** with everything recent JDs asked for that didn't survive Phase 3.

## Phase 5 — Set the rendering contract (style spec)

`09 - Resume Style Spec.md` ships with placeholders; fill it now so the first resume render has a contract to follow. Two routes:

- **User has a resume whose look they like:** parse that one document once, extract font, sizes, bold usage, and layout into the spec, and never parse a binary for formatting again. (This is the one sanctioned binary parse — it's what the spec exists to prevent from recurring.)
- **No reference resume:** propose the conventional defaults and ask for preferences in the same batched style as Phase 3 — e.g. *"I'll use Calibri throughout, 17pt name, 11.5pt section headings, 10.5pt body, 1-inch margins, 2-page target — want a different font or a 1-page target?"* Don't silently impose the defaults; the spec is the user's contract, so they should hear the choices once.

Either way, the phase ends with every placeholder in `09` replaced by a concrete value. The AI-tell rules already in the spec (em-dash scan, structural-bold-only) are not preferences — leave them.

## Phase 6 — Close the archive and arm the publish gate

Record in `HISTORY.md` that the archive is fully mined, with the date. From then on, **no session ever re-reads the archive** — everything useful is in the corpus as text, and re-parsing old binaries is pure cost. The archive can be compressed or deleted.

Then arm the publish gate: **generate `private-terms.txt`** (it's gitignored — it never leaves the machine) from the corpus you just filled — the user's names, employers, clients, cities, and email/phone fragments, one term per line. That file is the blocklist `scripts/validate_corpus.py` scans for, and building it from the filled corpus means the gate knows exactly what a leak of *this* corpus looks like. Run the script once to confirm it now fails loudly — a filled corpus that passes the gate means the blocklist is too thin, not that the corpus is publishable.
