# Job Search Profile

The targeting definition — the single place that defines "a good role for me." **No automation required:** paste any JD into an AI session and ask it to score the role against this profile (per the rubric below). If you do automate scouting later, this same file becomes the scout's filter and the scorer's rubric. Keep it current either way.

> **Privacy note:** in a filled corpus this file contains compensation floors and location strategy — it is exactly the kind of file the injection-defense rules in `CLAUDE.md` keep OUT of context while reading untrusted JDs, beyond the minimum the scorer needs.

## Work authorization

[e.g. "Citizen — no sponsorship required." Note how to treat clearance-eligibility mentions: flag, don't auto-reject.]

## Target titles (tiered)

**Tier 1 — strongest fit, lead with these:**
[Title] · [Title] · [Title]

**Tier 2 — strong fit with a caveat (note the caveat):**
[Title] · [Title]

**Tier 3 — adjacent / emerging (note the differentiator that makes them viable):**
[Title] · [Title]

**Title keywords for scout matching:** [comma-separated lowercase keywords a deterministic script can match against posting titles]

## Seniority

[e.g. "N+ years → senior IC, lead, or manager band. Skip junior/intermediate; skip levels that require an org-leadership track record not yet on record."]

## Locations

[Preference order, e.g. Remote → Hybrid → Onsite, with the acceptable geography per tier.]
- **Dealbreakers:** [locations/arrangements to auto-reject]
- If a relocation goal drives the preferences, record it here for the scorer — and note that **the motive never appears in artifacts** (no "X is an easy drive from Y" logistics in letters).

## Industries

[Preferences and exclusions — or "cross-industry experience is a strength; no exclusions."]

## Strong-fit skill signals (JD mentions → score UP)

[The keyword list from `02 - Skills Matrix.md` at proficiency ≥3.]

## Gap / avoid signals (JD requires → score DOWN + flag honestly; never fabricate)

[Mirror the Known Gaps section of `02 - Skills Matrix.md`, plus:]
- [Credential you lack when required as active/mandatory]
- ["X+ years managing direct reports" if you have no formal reports — flag, don't auto-pursue]

## Hard dealbreakers (auto-reject)

- **Current employer.** Never scout, score, or surface roles at [current employer], including all its entities/subsidiaries.
- [Location dealbreakers from above]
- Unpaid / commission-only · [minimum contract length] · requires a credential you lack that's non-negotiable

## Compensation

- **Permanent (FTE): floor [currency + amount]/yr base.**
- **Contract: floor [currency + amount]/hr.**
- Many postings omit comp — when present, the scorer flags clearly-below-floor roles (don't auto-reject on comp alone; a great role slightly below floor is still worth surfacing with a note).

## Target companies (for direct ATS-board polling — Greenhouse/Lever/Ashby)

[Named companies whose public ATS boards the scout polls directly — clean JSON endpoints, no scraping. Add companies anytime; this list is the scout's deep-targeting input.]

## Scoring rubric (how the scorer ranks a found role, 0–100)

1. **Title/seniority match** (25) — Tier 1 = full, Tier 2 = high, Tier 3 = moderate, off-target = reject.
2. **Skill coverage** (35) — % of the JD's must-have skills present in the Skills Matrix at proficiency ≥3. Produce the ATS coverage table here.
3. **Location fit** (15) — score per the Locations preference order; dealbreaker locations = reject.
4. **Gap penalty** (−, up to −25) — subtract for each hard-gap signal the JD requires; if a hard dealbreaker requirement appears, reject outright.
5. **Differentiator bonus** (+10) — role values [your cross-cutting differentiators, e.g. cross-industry experience, AI adoption, founder experience].

**Output per role:** fit % · one-line rationale · ATS coverage table · honesty gaps · recommendation (Pursue / Stretch-worth-it / Skip). Rank the day's roles; never inflate a score to make a role look better than it is — an honest "Skip" saves the user's time, which is the whole point.

## Pipeline mechanics

This section is a **reference design** — no scout code ships with this repo. Implement it however you like (or delete this section and score roles manually); what matters is the contract between stages:

- **Scout** (deterministic script): polls target-company ATS boards → writes `queue.md`, `roles.json`, and a compact `roles_digest.json` (the scorer reads the digest — a fraction of the tokens).
- **Score** (LLM): read the digest + this profile + `02 Skills Matrix` → apply rubric → write `scored.md`. Be honest: the scout matches keywords, so flag roles that keyword-match but aren't actually the candidate's lane.
- **Draft**: greenlit roles → resume/cover-letter workflow in `CLAUDE.md`.
- **Track**: an applications tracker file, one row per application.
- No auto-submit anywhere in the pipeline — a human reviews every artifact and clicks every Apply button.
