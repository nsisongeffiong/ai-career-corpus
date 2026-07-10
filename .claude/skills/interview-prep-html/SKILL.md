---
name: interview-prep-html
description: >
  Render interview prep packs as a single self-contained HTML file instead of
  markdown. Trigger for any interview-prep deliverable from this corpus:
  prepping for a specific interview, compiling STAR stories against a JD, or
  building a study sheet of talking points, gaps, and questions. The output is
  one .html file that opens directly in a browser with no network needed.
---

# Interview Prep — HTML Pack

Prep packs get studied the night before and skimmed on a phone minutes before an interview. A styled, navigable single page beats a markdown wall of text. This skill is scoped to that one deliverable.

*Adapted from the general `html-artifacts` skill, itself distilled from Thariq Shihipar's "The Unreasonable Effectiveness of HTML" (Anthropic Claude Code team, May 2026).*

**Any agent can use this file** — it is plain instructions. Claude Code discovers it automatically as a project skill; point other agents at it explicitly when producing interview prep.

## Output contract

One `Interview Prep.html` in the role's Per-Application folder (which is gitignored — prep is private). It must:

1. Open directly in any browser with **no network** (interview buildings have bad signal): all CSS/JS inline, system font stack, no CDN links, no external images.
2. Carry `<meta name="viewport" content="width=device-width, initial-scale=1">` — it will be read on a phone.
3. Give the gist in 60 seconds of scanning, and hold the depth for a full study pass.

## Grounding rules (non-negotiable, and precisely scoped)

- **Claims about the candidate** come ONLY from the corpus files — experience, numbers, tools, certs. The HTML is a rendering, never a new source of truth.
- **Claims about the company/role** come ONLY from the JD or the user.
- **General technical knowledge is allowed and expected** — teaching content (protocol explanations, tool comparisons, cheat-sheet definitions) is what makes the pack useful. Keep it visually and verbally distinct from claims about the candidate: "the standard stack is X" teaches; "I have used X" claims, and must be corpus-backed.
- Where a strong answer needs a story the corpus doesn't hold, **do not invent it** — emit a "personalize this" framework card (structure + what makes the answer land) and surface it in the final checklist.
- The em-dash ban does NOT apply — private study material, never submitted.

## Content blocks (include what the interview type warrants)

Weight by interview type: technical interviews get domain Q&A sections; behavioral get STAR depth; most senior-role packs need both.

- **Header strip:** company · role · interview date/format if known.
- **TL;DR box:** the winning frame in 3-4 sentences — the differentiator, what to expect, the exposed flanks.
- **How to use this pack + legend:** one paragraph; define the tags (below).
- **JD ↔ corpus mapping table:** each key requirement → the corpus evidence → a strength tag (`STRONG` / `FRAME IT` / `GAP`). Include a callout for any equivalence the interviewer may not know (e.g. a held cert that IS the requested exam code) — say it early.
- **Domain Q&A sections** (technical prep, organized by the JD's themes): each anticipated question as a collapsible card with a **model answer written in first person**, grounded in corpus facts where it claims, teaching where it explains — plus an optional italic *why this works* note, and an honest-bridge line for anything near a gap ("bridging beats bluffing").
- **STAR deep-dives:** the stories most likely to be probed, full Situation/Task/Action/Result inside collapsibles, 2-line condensed version visible. **Flag any story the cover letter already spent.**
- **Gap section:** each gap the JD exposes → the prepared answer, including a **minimum viable answer** script for likely probe questions (enough fluency not to freeze, an honest bridge past the edge of real depth).
- **Rapid-fire cheat sheet:** a term → 30-second-version table for vocabulary the role assumes but the corpus lacks depth in.
- **Questions to ask them:** each with a parenthetical note on what asking it signals.
- **Final prep checklist callout:** the numbered actions only the user can do — personalize the flagged story, rehearse the key numbers aloud, memorize the bridge sentences.

## Tagging

Use small colored pills, defined once in the legend: `CORE` (near-certain to come up) / `LIKELY` / `GAP` (prepare a bridge) on questions and sections; `STRONG` / `FRAME IT` / `GAP` in the mapping table.

## Design defaults

- Body text ≥15px, line-height ≥1.6, max content width ~900px.
- Native `<details>/<summary>` for Q&A and story cards; open the single most important card by default.
- Pills, tables, and left-border callouts (warning / info / success) as the visual grammar; monospace for commands and tool names.
- **Sticky sidebar TOC with scroll-spy** when the pack exceeds ~6 sections (a ~10-line IntersectionObserver script earns its keep); hide it at phone width via media query. Below ~6 sections, jump links at the top suffice.
- Dark or light theme both fine; respect `prefers-color-scheme` when trivial. One readable theme beats two mediocre ones.

## Checklist before delivering

- [ ] Opens locally with no errors and no network
- [ ] Readable at phone width (TOC collapses, tables don't overflow)
- [ ] Every collapsible opens; TOC/jump links track correctly
- [ ] Every first-person claim traces to a corpus fact; teaching content clearly not self-claims
- [ ] "Personalize this" cards + spent-story flags present where applicable
- [ ] Final checklist tells the user exactly what to rehearse
- [ ] The gist lands in 60 seconds
