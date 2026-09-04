# digiwin-research-company

A "skill" that teaches an AI assistant (Claude Code) how to do the homework on a Thai factory before a
salesperson visits it. Written so anyone can follow, even with no sales or AI background.

---

## 1. What is a skill?

Imagine hiring a very smart assistant who has read every book in the world but has never worked at your
company. On day one they don't know your customers, your products, or the mistakes your team learned
the hard way.

A **skill** is a folder of instructions you hand to that assistant: *"When I ask for this job, here is
exactly how we do it, step by step, and here are the traps."* The assistant reads it and does the job that
way. If the skill has a checker script, the job is not finished until the checker passes.

## 2. The job this skill does

You type:

```
/digiwin-research-company <company name>          (quick, about 10 minutes)
/digiwin-research-company <company name> --deep   (deep, 35–55 minutes, several helpers in parallel)
```

and the assistant writes a report about that company: its official registration, who the directors are,
five years of revenue and profit, what it makes, what software it probably runs already, what its likely
headaches are, and how our factory software could help. Use the deep version before any first visit.

## 3. Where the facts come from

- **DBD**, Thailand's government business registry (the single most valuable source: registration,
  capital, directors, financial statements, related companies). `dbd-checklist.md` says exactly which pages
  to open, in which order.
- The company's own **website**, every product/solution/news page two or three clicks deep, not just the
  home page. The real information hides deep.
- **News, job ads, LinkedIn snippets, Facebook**, and **U.S. shipping records** (which tell you who their
  export customers are and therefore which quality rules they already live under).
- **Local voice**: Thai forums and reviews, how people talk about the company.

Every fact in the report says where it came from. Guesses are allowed but must wear a tag, 【推論】
("inference"), and stay in clearly marked sections that never reach a customer.

## 4. What makes it careful

- **Never invents.** If the registry is blank, the report is blank there.
- **Chinese names in Thai** can be spelled many ways; the skill tries each spelling, then the English name,
  then the web, before it gives up.
- **Spots odd companies:** a "shell" with capital but no factory, a company that changed its legal form
  (so the old records are under another name), a brand-new factory still being built.
- **Stops early** when a company is too small or dissolved, so nobody wastes an hour.
- **Protects the database.** The finished report is loaded into a company database by a strict parser.
  `scripts/check_contract.py` refuses any report whose shape would corrupt that database.
- **Asks the experts.** When a judgement call cannot be grounded in evidence, the skill asks the company's
  in-house AI of senior sales experts (called NOVA) and tags the answer as advice, not fact.

## 5. Files

| File | What it is |
|---|---|
| `SKILL.md` | The full procedure |
| `extraction-schema.md` | The list of facts to collect, plus the table that maps a factory's pain to the product that fixes it |
| `dbd-checklist.md` | The registry pages to open, in order |
| `briefing-template.md` | The shape of the finished report |
| `nova-knowledge.md` | Rules of thumb learned from senior sales experts (advice, not facts) |
| `nova-live-consultation.md` | How to ask a live expert when unsure |
| `batch-mode.md`, `industry-sweep.md` | Researching many companies at once |
| `scripts/check_contract.py`, `scripts/check_contract.sh` | The checker that gates every report |
| `scripts/batch_depth_gate.py` | The checker for batch runs |
| `supporting/model-tier-harness.md` | Which size of AI helper to use for which sub-job (the skill refers to it when it spawns helpers) |
| `supporting/importyeti-capability-review.md` | How to read U.S. shipping records and what they tell you about a factory's customers |
| `supporting/partner-extraction-schema.md` | The sister skill's schema for *partner* companies; this skill hands off to it when a company turns out to be a reseller, not a factory |

## 6. Install and use

1. Install Claude Code.
2. Copy this folder to `~/.claude/skills/digiwin-research-company/`.
3. In a session, type `/digiwin-research-company <company>`.
4. It expects a MySQL database for the reports and a browser it can drive for the registry. It tells you
   what is missing when you run it.

## 7. House rules

- No fact without a source; blanks stay blank; guesses are labelled.
- Open every page; never trust a name.
- Run the checker before saying "done".
- One legal entity per report; sister companies get their own reports.

## 8. Glossary

| Word | Plain meaning |
|---|---|
| **ERP** | Software that runs a company's paperwork: orders, purchases, stock, money |
| **MES** | Software that runs the factory floor, minute by minute |
| **DBD** | Thailand's Department of Business Development, the company registry |
| **OSINT** | Research using only public information |
| **NOVA** | The company's in-house AI trained on senior sales experts |
| **【推論】** | "Inference": a labelled guess |

*Private repository. DigiWin Thailand, 2026.*
