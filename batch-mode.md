# Batch Mode Contract — SDD + Acceptance Criteria (v1, 2026-07-18)

Why this file exists: the 2026-07-17 overnight batch compressed DEEP runs (D1–D4 → 2 combined
agents, 12 min/company vs ~30 min baseline) and violated Peter's no-parallel rule. The A/B
re-run (PTTGC) and the 5-dossier upgrade proved compressed = triage-grade: verdicts held, but
decision-changing facts were missed in ALL five (headline: Nextronics' parent runs DigiWin
TIPTOP GP 5.X — invisible at compressed depth). This contract makes that failure structurally
impossible to repeat silently.

## SDD — how batch deep runs work

### Invariant 1 — batch NEVER changes the per-company protocol
A batch changes HOW MANY companies are researched, never HOW each one is researched.
Per company, `--deep` ALWAYS means: DBD Phases A–E(+G) → warm base → D1 → D2 → D3 → D4 →
D5 (community & sentiment, added 2026-07-18) → fresh NOVA live query → synthesis → gates →
atomic promote → ingest --commit → ledger row.
There is no "batch tier" between QUICK and DEEP. Compressed/combined agents are FORBIDDEN
unless Peter explicitly orders a triage tier by name — and then the output banner and report
must say "TRIAGE — not deep" on every dossier.

### Invariant 2 — sequential agents (Peter's standing rule)
Within a company, D1–D4 are dispatched ONE at a time; each waits for the prior fragment's
STATUS line. Never two research agents alive simultaneously — not within a company, not
across companies. Kill each agent immediately after consuming its output.

### Invariant 3 — depth beats coverage
If the time budget cannot fit N companies at full depth, do FEWER companies at full depth
and queue the rest — never all companies at reduced depth. Order the queue by Peter's stated
priority, else by expected fit. The morning report lists the un-run queue explicitly.

### Invariant 4 — baseline self-check
Known baseline: ~30 min/company full deep (sequential agents + NOVA). If a company completes
in <25 min, STOP and audit that company's artifacts against the acceptance criteria below
before starting the next one. Faster-than-baseline is a defect signal, not a win.

### Invariant 5 — honest reporting
The batch report MUST state, per company: wall-clock minutes, agent count and dispatch mode
(sequential), fragment STATUS values (OK/PARTIAL/FAILED), NOVA job id, gate result. Any
deviation from this contract is disclosed in the report's first section, not on interrogation.

## Acceptance Criteria (per company, deep tier — mechanical where possible)

| # | Criterion | Check |
|---|---|---|
| AC1 | 5 fragment files exist: `docs/research-fragments/<id>/d1-*.md … d5-*.md` (d5 required for runs from 2026-07-18; earlier promoted runs grandfathered) | batch_depth_gate.py |
| AC2 | Each fragment ends with `STATUS: OK|PARTIAL|FAILED` and contains a search/fetch log with ≥8 entries | batch_depth_gate.py |
| AC3 | Fragments were produced sequentially: mtime(d1) ≤ mtime(d2) ≤ mtime(d3) ≤ mtime(d4) | batch_depth_gate.py |
| AC4 | `nova-live-<date>*.md` exists, contains a job id + verbatim capture ≥800 chars | batch_depth_gate.py |
| AC5 | `check_contract.py --deep` ALL PASS + ingest dry-run exactly 1 entity | existing gates |
| AC6 | Wall-clock ≥25 min OR a written justification line in the ledger/report | orchestrator judgment + report |
| AC7 | Any fragment STATUS ≠ OK carries the visible MODULE FAILED/PARTIAL note in the dossier | orchestrator judgment |

## QA setup

Run BEFORE promoting each company in ANY batch or unattended run (and any solo deep run):

```bash
python3 ~/.claude/skills/digiwin-research-company/scripts/batch_depth_gate.py <company-id>
# then the existing gates:
python3 ~/.claude/skills/digiwin-research-company/scripts/check_contract.py docs/_eval/gold-standard-<id>.md.draft --deep
python3 database/ingest_md_to_db.py --file "$(pwd)/docs/_eval/gold-standard-<id>.md.draft"
```

batch_depth_gate.py exits non-zero on any AC1–AC4 failure and names the missing artifact.
A company that fails the depth gate is NOT promoted — it goes back for the missing modules,
or into the un-run queue with its state documented. Fragments are archived to
`docs/_eval/archive/<id>/` only AFTER promotion, so the gate always sees a live run's files.

## Trilingual OSINT doc — the deliverable standard (added 2026-08-29)

Every completed company gets a 3-tab Google Doc (English / 中文 / ไทย) that is an
**entry-strategy briefing**, not a facts dump and not a customer handout. Reference:
the ALUMET doc (`15TE8eqceZZqQLfuml3LaDiqGyefpSIEd1iurTapoTPw`) — its own header says
"Facts and analysis separated throughout": separated, NOT removed.

MECHANICAL GATE (run BEFORE writing the link into the master sheet):
```bash
python3 tools/osint_doc_gate.py <docId>       # must ALL PASS
python3 tools/osint_doc_gate.py --calibrate   # proves the gate still passes its reference
```
Checks: ~14k chars EN / ~5.5k ZH / ~14k TH · >=9 numbered sections · analysis-marker
density (Consequence/因此/สิ่งที่ต้องทำ …) · as-of date + verify note · and a LEAK check
that no INTERNAL fence, 【推論】 tag, NOVA verbatim or 六要素 internals reach the doc.

BURN (2026-08-29): TNM's first doc shipped at 4.5k chars, facts only — no executive
summary, no consequences, no entry strategy — because the standard lived only inside an
example document. Peter caught it. The gate now encodes it.
