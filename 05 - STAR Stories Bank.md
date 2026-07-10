# STAR Stories Bank

5-10 strong behavioral interview stories, written once and reused across interviews. Most behavioral questions reduce to 8-10 underlying themes; cover them well and you're prepared for ~90% of behavioral interviews.

**Format:** Situation → Task → Action → Result.

**Aim for stories that:**
- Are recent (last 3-5 years where possible)
- Have a clear, measurable outcome
- Show *you* did the thing — use "I" not "we"
- Last 2-3 minutes spoken out loud (~300-400 words written)

**Give each story a resume-bullet form** — the one-line compressed version — so cover-letter sessions can spend a story in 2-3 sentences without re-deriving it. When a cover letter uses a story, the agent tells you which one it spent (you may want to hold it for the interview instead).

---

## Themes to cover

Aim to have at least one strong story for each:

- [ ] **Leadership** — led a team or initiative without formal authority
- [ ] **Conflict** — handled disagreement with a peer/manager/stakeholder
- [ ] **Failure** — something that didn't work and what you learned
- [ ] **Ambiguity** — solved a problem when the path wasn't clear
- [ ] **Change/adaptability** — adapted to a major shift (technology, org, market)
- [ ] **Stakeholder management** — navigated competing priorities or difficult stakeholders
- [ ] **Tight deadline / pressure** — delivered under stress
- [ ] **Innovation / initiative** — proposed and shipped something new
- [ ] **Mentorship** — grew someone else's capability
- [ ] **Cross-functional collaboration** — worked across functions/silos

---

## Template

### Story Title: [Memorable name — "The ColdFusion Migration," "The Angry VP," etc.]

**Themes:** [Leadership, Conflict, etc.]
**Year / Role:** [YYYY at Company]
**Best for questions like:** [e.g., "Tell me about a time you handled conflict"]

**Situation** (1-2 sentences):
[Where you were, the context, the stakes]

**Task** (1 sentence):
[What you specifically needed to accomplish]

**Action** (3-5 sentences — the meat):
- [What you did, step by step]
- [Why you chose that approach]
- [What was hard about it]

**Result** (1-2 sentences, quantified):
[The outcome — numbers if possible. If it didn't go well, what you learned.]

**Reflection / What I'd do differently:** [Optional but powerful]

**Resume-bullet form:** [The whole story compressed to one honest bullet.]

---

## Stories

<!-- FICTIONAL EXAMPLE — delete and replace with your own. -->

### Story Title: The Runbook Rescue

**Themes:** Ambiguity, Initiative, Tight deadline / pressure
**Year / Role:** 2023, Platform Engineer @ Contoso
**Best for questions like:** "Tell me about a time you turned around a failing process" / "delivered under pressure"

**Situation:**
Contoso's flagship release was failing roughly one deploy in five, each failure costing an evening of engineer time, and the biggest client (Fabrikam) had escalated. The release runbook was 40 manual steps maintained by one person who had just resigned.

**Task:**
Stabilize releases before the next quarterly contract review — about ten weeks out.

**Action:**
- Spent the first two weeks *not* automating: shadowed three releases end-to-end and logged where each failure actually originated (most came from two environment-drift steps, not the twenty steps everyone blamed).
- Codified environments in Terraform first, eliminating the drift class entirely.
- Then built the pipeline in GitHub Actions with automated rollback, migrating one release stage per week so there was never a big-bang cutover.
- Wrote the new runbook as pipeline documentation, so the process and its docs could no longer diverge.

**Result:**
Release time dropped from 4 hours to 20 minutes and the failure rate fell below 2%. The client review passed without the reliability agenda item.

**Reflection / What I'd do differently:**
The two diagnostic weeks felt slow and were the whole ballgame — automating the original process would have automated its failure modes too.

**Resume-bullet form:** "Stabilized a failing release process under a 10-week client deadline — diagnosed environment drift as the root cause, codified environments in Terraform, and replaced a 40-step manual runbook with a GitHub Actions pipeline, cutting release time from 4 hours to 20 minutes at under 2% failure."
