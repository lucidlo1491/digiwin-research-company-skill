# Model-Tier Harness — the delegation discipline
*Why this exists: on 2026-06-13 a research workflow spawned 105 top-tier agents,
burned 4.57M tokens, and hit the spend cap — doing work (source-verification)
that a cheap model does identically. The PhD fetched coffee because nobody wrote
the job description. This file is the job-description discipline.*

## The principle
A senior worker doesn't hand a junior a vague task — they write **what good
output looks like** so the junior can execute and self-check. Token efficiency
isn't "use cheap models"; it's **specify tightly enough that cheap models
succeed.** A well-specified task on Haiku beats a vague task on Opus.

## The tier policy (law)
| Work | Tier | Test |
|---|---|---|
| Interviews, architecture, plans, synthesis, taste | TOP (Opus/Fable) | "If this is wrong, does everything downstream break?" → yes |
| Adversarial review, red teams, final gates | TOP | The skeptic's value IS judgment — never cheap |
| Implementation from a complete spec | SONNET | Plan supplies the code/contract; agent transcribes+wires |
| Spec-compliance checks, source verification, fetch, extract | HAIKU/SONNET | Checklist comparison, not judgment |
| Mechanical: file moves, screenshots, doc regen, smoke runs | HAIKU | "Could a careful intern do it from the instructions?" → yes |
| Pipeline runtime (extraction, translation, narrative) | GEMINI FLASH (thinking off) | already RUNBOOK law |

**Applies to workflow agents too** — `agent(prompt, {model: 'haiku'})`, not just
my direct dispatches. The research burn happened because workflow jurors
inherited the session model. Every fan-out names its tier.

## The delegation spec — every handed-down task carries these 4 things
A task is only ready to delegate when I can write all four. If I can't, the task
isn't specified enough yet — that's MY job to finish first, not the junior's.

1. **OUTCOME** — the exact artifact + shape (schema/format), not a goal.
2. **QUALITY BAR** — the checkable definition of done the junior self-verifies against.
3. **INPUTS** — everything needed, curated; never "go find context."
4. **GUARDRAILS** — what not to do, what to do when stuck.

## Worked example — the research verification task (what SHOULD have been written)
> **Agent:** verify-claim · **Model:** HAIKU · **Outcome:** one VERDICT object
> `{refuted: bool, evidence: str, confidence: high|med|low, counterSource?: str}`.
> **Quality bar:** (a) read ONLY the supplied source text + claim — no new
> searches; (b) `refuted=true` only if the source text contradicts or fails to
> support the claim; (c) `evidence` quotes the source span you judged on; (d)
> default `refuted=false` when the source supports it, `confidence=low` when
> ambiguous. **Inputs:** the claim string + the fetched source text (supplied —
> do not re-fetch). **Guardrails:** no web access; if the source is empty/
> unreadable return `refuted=false, confidence=low, evidence="source
> unavailable"`; never spend more than one read.

That spec runs on Haiku at ~1/15th the cost and is MORE reliable than an
unspecified Opus juror, because the bar is explicit. Three of those per claim =
the same 3-vote rigor, ~$0.02 instead of ~$3.

## The proof (the ledger)
Every delegated dispatch logs one line to `docs/token-ledger.csv`:
`date,task,tier,tokens,outcome,review_verdict`. After any multi-agent effort I
report: % tokens by tier · cost vs all-top-tier baseline · review pass-rate per
tier (proving quality held). If a cheaper tier's pass-rate drops, the ledger
shows it and the policy moves that task class up a tier. Measured, not asserted.

## The standing rule (→ CLAUDE.md)
Before spawning any agent or workflow: name its tier and write its 4-part spec.
Top tier is for judgment; everything specifiable enough to checklist goes cheaper.
Vague-and-expensive is the failure mode — specified-and-cheap is the target.
