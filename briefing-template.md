# Briefing Template (v4)

Use this structure for the output. Every field must show Source and Confidence. Section headings marked **[INGEST]** are parsed by `database/ingest_md_to_db.py` — never rename them; see SKILL.md OUTPUT CONTRACT for the full boundary rules (forbidden headings, prose-only Key People, Date-first urgency columns, explicit Exports line, no 【推論】 in any pipe table).

Choose the template by company type: **A** operating · **B** greenfield · **C** SPV/unresolved · **D** partner/channel.

Every output (all templates) starts with the two banners:
```
> Research tier: QUICK | DEEP · v4 · deep sections: present | absent (run --deep)
> INTERNAL WORKING DOSSIER — Peter/DigiWin TH only; never forward; strip 【推論】 + fenced blocks before any external use
```

## Canonical 六要素 table (single source of truth — labels + FROZEN element_key)

| Label | element_key (frozen, matches DB reader) | OSINT Resolvable? |
|---|---|---|
| 上線時程 Timeline | `timeline` | Yes |
| 分段預算 Budget | `budget` | **No** (needs meeting) |
| 痛點需求 Requirements | `requirements` | Yes |
| 三角色決策 Decision | `decision_roles` | **No** (needs meeting; OSINT hypothesis stays `inferred`) |
| 競爭態勢 Competition | `competition` | Yes |
| 動機 L1 (不得不做) | `motivation_l1` | Yes |
| 動機 L2 (不得不跟鼎捷做) | `motivation_l2` | **No** (needs meeting) |

Never use the old 6-row MEDDIC-style variant. OSINT fills ≤4/7; the rest are `needs meeting`.

---

## Template A: Operating Company (has revenue history)

```markdown
# [Company Name] — Gold Standard
> Research tier: QUICK | DEEP · v4 · deep sections: present | absent (run --deep)
> INTERNAL WORKING DOSSIER — Peter/DigiWin TH only; never forward; strip 【推論】 + fenced blocks before any external use
> Generated: [date] | Confidence: [High/Medium/Low] | Sources checked: [X/12] | Company Type: Operating

## 60-SECOND PRE-CALL READ
> INTERNAL ONLY — never into customer-facing artifacts
> 痛 — [sharpest pain hypothesis + evidence] 【推論 from …】
> 錢 — [size read + affordability one-liner] 【DBD】
> 急 — [#1 dated urgency trigger] 【公開/DBD】
> Fit — [incumbent verdict one-liner + product-fit hint (facts only)]
> 決策 — [who decides + AUTHORITY CHECK result]
> ASK: 1) […] 2) […] 3) […]

## Phase A — Identity Resolution
| Searched | Result |
|---|---|
| | |

## Phase B — Company Profile
| Field | Value | Source | Confidence |
|-------|-------|--------|------------|
| Legal Name (EN) | | | |
| Legal Name (TH) | | | |
| Tax ID | | DBD | High |
| Founded / Registered | | | |
| Reg. Capital (THB) | | | |
| TSIC (registration-time AND latest) | | | |
| Address / Province / Industrial Estate | | | |
| Website / Facebook | | | |
| BOI Promoted | | | |
| Ownership Type | | Evidence: [director names] | |

## Phase B+ — Deep Website Crawl
[Products/solutions per sub-page · certifications · plants & capacity · leadership · group pages — every claim traced to its page URL (Gate #8)]

## What They Make
[Products, processes, capacity, factory locations, certifications]

## Directors
| Name | Position | Other directorships (deep) |
|------|----------|------------------------------|
| | | |
Signing authority: [name(s) + binding conditions] 【DBD】
(If paywalled: write the prose line `Directors: PENDING (paywalled)` — and keep Key People prose-only.)

## Ownership Analysis
**Classification**: [Thai family / 台商 / 陸商 / Japanese JV / MNC]
**Evidence**: [director names / parent]
**Confidence**: [ ]

## Phase C–E — DBD 5-Year Financials
[Balance sheet table · income statement table · ratios (Revenue YoY, margins, D/E, Inventory/Assets, SG&A%) · written trend analysis, numbered, each point with evidence]

### Financial Pain Signals (question-form ONLY — never declarative loss claims)
> INTERNAL ONLY — never into customer-facing artifacts
> [e.g. "Inventory is 42% of assets and grew 2× faster than revenue — IF even 1% of that is dead stock, that's ฿X–Y tied up (assumption: industry norm ~25%). Worth asking how they count it?"] — each ฿ figure NAMES its assumption. KSF3 flag: pain candidate clears / does not clear ฿1M THB (arithmetic shown).

## Technology & Systems   [INGEST — ONE table, confirmed rows only]
| System Type | Vendor/Product | Evidence (dated) | Confidence |
|-------------|---------------|------------------|------------|
| | | | High/Medium only |
> No confirmed signal found after job-post + website + news sweep. *(← no-signal goes HERE as blockquote, never as a row)*

## ERP Incumbent Read 【推論】   *(deep; non-ingested)*
> INTERNAL ONLY — never into customer-facing artifacts
> **Verdict (4-state):** displacement / greenfield / recently-purchased-or-implementing (→ complement play: eMES/WMS) / in-family TIPTOP (→ upgrade-expansion play)
> **EOL / renewal hints:** [dated] · **Active-evaluation signals:** [evaluation-in-progress rows, dated]
*(QUICK tier: `> Deep module not run — rerun with --deep.`)*

## Group Structure & Decision Map   *(deep; members as TABLE ROWS — never headings)*
| Entity (col-1 must not start with Export/Tax ID/etc.) | Relation | Signals (≥2 required, else "possible, unverified") | Source |
|---|---|---|---|
Exports: [real markets, or exactly `Exports: not found`]
> INTERNAL ONLY — never into customer-facing artifacts
> Decision-map hypothesis: 守門員=[…] 決策者=[…] 核決者=[…] (Low confidence, `inferred` — never higher from OSINT)
*(QUICK tier: `> Deep module not run — rerun with --deep.`)*

## Urgency Signals & Timing Triggers   *(deep; Date-first columns)*
| Date | Trigger | Evidence | Source |
|------|---------|----------|--------|
| 2026-.. | [System EOL — …, new factory, BOI approval, hiring surge, IPO/แปรสภาพ…] | | 【公開】 |
*(≥3 rows or the line "no timing trigger found". QUICK tier: placeholder blockquote.)*

## Warm Base & Nearby References
> INTERNAL ONLY — never into customer-facing artifacts
> [3–5 lines, each 【DB】-tagged + direct|distributor-tagged. Live deals NEVER named ("an active opportunity in the same estate — ask Peter"); signed customers named only if reference-approved.]

## Key People   [INGEST-adjacent — PROSE ONLY, no tables, no bullets]
[Prose paragraphs: names, titles, inferred roles at Low confidence with public source URLs.]
AUTHORITY CHECK: [name] — on / NOT on DBD director list; signatory = [X]; stage cap C2 until the signatory engages.

## Supply Chain & Trade
[Customers, suppliers, export markets, ImportYeti. Interpretation: China imports → BOI module; JP/DE exports → traceability; seasonal spikes → APS **(T100/Dinghua tier ONLY — iGP = LRP + 異常報表)**.]

## Recent News (last 12 months)
| Date | Headline | Type | Sales Implication |
|------|----------|------|-------------------|

## Competitive Landscape
[4-state verdict recap + active-evaluation status. Thai SME default competitor = Excel/paper/none.]

## Digiwin Fit Assessment
**Fit Score**: [HIGH / MEDIUM / LOW / DISQUALIFIED] · **OSINT Recommended Stage**: [E / C2-candidate] · **Actual Pipeline Stage**: [if known]
### Why [SCORE]
1. …
### 六要素 Status
[Use the canonical 7-row table above — labels + frozen keys, ≤4/7 from OSINT]
### Pain → Digiwin Product
| Pain Indicator | Evidence | Recommended Product |
|---------------|----------|---------------------|
[Company-specific rows from extraction-schema §13 — never the generic table]

## Discovery Priorities (ask THESE first)
1–5, ordered.

## Key Sales Angles (say THESE)
1–5, each evidence-backed.

## Reflection Summary
- Sources checked: [X/12] · Data gaps · Contradictions · Entity anomalies · Additional searches run · Overall confidence
- (deep) Module STATUS: D1 [OK/PARTIAL/FAILED] · D2 […] · D3 […] · D4 […]

## All Sources
| # | Source Type | URL/Query | Data Obtained |
|---|-----------|-----------|---------------|
[Must include specific sub-page URLs — Gate #8]
```

---

## Template B: Greenfield Company (pre-revenue, factory in construction)

Same banners + 60-SECOND READ (痛 = launch-readiness risk; 急 = production-start date). Then:

```markdown
# [Company Name] 🏗️ GREENFIELD — Gold Standard
[banners + 60-second read]

## Phase A / Phase B [as Template A]

## Parent Company Profile
| Field | Value |
|-------|-------|
| Name / HQ / Website / Core business / Scale / Certifications | |
> Parent analysis is CRITICAL — they fund the investment and often dictate the ERP choice.

## Factory Build-Out Status
| Metric | Value | Assessment |
|--------|-------|------------|
| Reg. capital / Total assets / PP&E (% assets) / Burn rate / Revenue / Est. production start | | |

## Directors [as Template A, incl. Signing authority line]

## Digiwin Fit Assessment
**Fit Score**: [HIGH — greenfield = ideal ERP timing] · **OSINT Recommended Stage**: [E / C2-candidate]
### Why greenfield = ideal timing
- No incumbent to displace · clean implementation · configure during construction, ready Day 1 · parent may already run DigiWin/competitor
### Pain → Digiwin Product [§13 rows: new-factory launch → full ERP; BOI; multi-currency; parent consolidation]

## Key Sales Angles / Discovery Priorities / Reflection / All Sources [as A]
```

---

## Template C: SPV / Identity Unresolved

```markdown
# [Company Name] ⚠️ SPV DETECTED — Gold Standard
[banners]
> Confidence: LOW — entity may not be the operating company

## ⚠️ Entity Warning
[red flags: zero revenue/inventory/PP&E, single director…]
## What We Found  [DBD data for the SPV]
## Recommended Next Steps
1. Search director name(s) on DBD for related operating entities
2. Search the address for co-located companies
3. Confirm correct entity with [contact]
## Sources
```

---

## Template D: RETIRED → use /research-partner (2026-07-17)

Partner/distributor/SI/co-sell/alliance candidates are researched by the sibling skill
**`/research-partner`** (`~/.claude/skills/research-partner/`) with Template P: the frozen
8-dim Partner Assessment, activation-readiness vs the SMK precedent, live conflict-roster
enumeration, and its own contract checker + `partner_assessments` DB ingest. Do NOT write a
partner dossier with this skill's templates — 通路案 ≠ sell-to (checker-enforced both ways).
