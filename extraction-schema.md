# Extraction Schema

## Source Priority

1. **DBD DataWarehouse** (HIGHEST) — official government data. Always start here.
2. **Company website** — self-reported but usually accurate for products/certs.
3. **News articles** — dated, verifiable, third-party.
4. **Industry directories** (GlobalFastener, Fasten.one, Fact-Link) — curated profiles.
5. **Social media** (Facebook, LinkedIn snippets) — useful for people and recent activity.
6. **Estimated** (LOWEST) — your inference from indirect evidence.

## Confidence Levels

- **High**: Verified from DBD or other official government source
- **Medium**: From company website, news article, or industry directory
- **Low**: Single unverified source (e.g., one LinkedIn snippet)
- **Estimated**: Your inference from indirect evidence
- **Unknown**: Not found after searching

## Categories (12 total)

### 1. Company Basics
- Legal name (English)
- Legal name (Thai)
- Trade name / brand name
- Tax ID (เลขทะเบียนนิติบุคคล) — 13 digits
- DBD registration status (Active / Dissolved / Liquidating)
- Company type (Co., Ltd. / Plc. / Partnership / Branch)
- Founding year
- Registered capital (THB)
- Paid-up capital (THB)
- Parent company (if subsidiary)
- Ownership structure (Thai family / 台商 / 陸商 / Japanese JV / MNC subsidiary / PE-backed)
- Registered address
- Province
- Industrial estate (if applicable)
- Website URL
- Facebook URL
- LinkedIn URL

### 2. Products & Manufacturing
- Primary products manufactured
- Manufacturing processes (injection molding, CNC, assembly, etc.)
- Industry classification
- Production capacity (if available)

### 3. Factory Locations
- Site name and address for each factory
- Province for each site
- Industrial estate for each site
- Factory size (sqm) if available

### 4. Employees
- Total employee count
- Estimate source and method
- MIS/IT staff count (if discoverable)

### 5. Financial Data
- Annual revenue (THB) — specify year
- Net profit (if available)
- Revenue trend (growing / stable / declining)
- Public listing status (SET / MAI / Private)

### 6. Technology & Systems
- Current ERP system (vendor + product)
- Other systems (MES, WMS, CRM, accounting)
- Evidence for each (job posting, subdomain, news article, employee profile)
- Digital maturity assessment (None / Low / Medium / High)

### 7. Key People
- Name (English + Thai + nickname if found)
- Job title
- Department
- Inferred decision role (守門員 / 決策者 / 核決者 / Unknown)
- Role confidence (always Low from OSINT)
- Contact info (only if publicly available — PDPA compliance)
- Source where found

### 8. BOI Status
- BOI promoted? (Yes / No / Unknown)
- BOI privileges (zone, tax exemption period)
- Bonded warehouse status
- Evidence source

### 9. Recent News (last 12 months)
- Date, headline, source URL
- Event type (Expansion / M&A / Leadership Change / Financial / Award / Product Launch)
- Sales implication (why this matters for Digiwin)
- Trigger type (不得不做 trigger? 不得不跟鼎捷做 trigger?)

### 10. Ownership Type
- Classification (Thai family / 台商 / 陸商 / Japanese JV / MNC / etc.)
- Evidence: director names that support this classification
- Parent company (if applicable)

### 11. Supply Chain
- Key customers (who do they sell to?)
- Key suppliers (who do they buy from?)
- Import sources (which countries?)
- Export destinations (which countries?)
- Export percentage of revenue
- ImportYeti data (if available)

### 12. Certifications
- ISO 9001 (Quality)
- ISO 14001 (Environmental)
- IATF 16949 (Automotive)
- ISO 45001 (Safety)
- GMP / HACCP (Food/pharma)
- Other certifications
- Source for each

### 13. Pain-to-Digiwin Product Mapping (Authoritative Reference)

This is the single source of truth for mapping company pain indicators to Digiwin products. SKILL.md and dbd-checklist.md reference this section — do not duplicate the table elsewhere.

| Pain Indicator | Evidence to Look For | Recommended Product | Pain-in-฿ question form (named assumption; INTERNAL) |
|---------------|---------------------|---------------------|-------------------------------------------------------|
| New factory / multi-site | Multiple registrations, group companies | T100 or Workflow (multi-entity ERP) | — |
| BOI promoted | BOI search results, investment privileges | BOI/EPE compliance module **(auto-trigger HIGH fit score)** | "One BOI reconciliation gap can mean supplementary tax — a peer eliminated ฿10M+/yr exposure. How long does each audit prep take your team?" |
| IATF 16949 / ISO certification | Certification on website, DBD TSIC auto parts | MES + QMS | — |
| High labor cost pressure | SG&A trend, job postings, factory news | **APS (T100/Dinghua tier ONLY — iGP answer = LRP + 異常報表; NEVER promise auto-scheduling on iGP)** | "IF scheduling gaps idle even 3% of machine-hours (assumption: industry planning-loss norm), that's ฿[rev×ratio range]/yr — how do you schedule today?" |
| Excel/paper-based production | No ERP in job postings, no IT roles | Core ERP (Workflow) | "What does one month-end close cost in overtime days × people?" |
| Warehouse problems / inventory inaccuracy | Inventory >40% of assets, inventory growing faster than revenue | WMS (sFLS), FIFO compliance | "IF even 1–2% of that ฿[inventory] is dead/expired stock (assumption stated), that's ฿[X–Y] tied up — when was the last full count that matched the books?" |
| Export-heavy / customer audit requirements | ImportYeti data, export %, international customers | EDI + traceability | "What does one failed customer audit or delayed 驗廠 cost you in orders?" |
| IPO preparation | SET/MAI filings, Plc. conversion, prospectus | Internal Controls + Financial Consolidation | — |
| Group company / multi-entity | Multiple DBD entities, shared directors | Financial Consolidation (T100) | — |
| BOI bonded warehouse | BOI promotion with import duty exemption | Inventory control + bonded warehouse module | — |
| Automotive tier supplier | IATF 16949, auto TSIC, Japanese/Western customers | EDI + quality-documentation modules | "At annual price-down time, do you negotiate with actual per-part cost or averages?" |
| Food/pharma manufacturing | GMP/HACCP cert, food/pharma TSIC | GMP/HACCP traceability | "If a lot is questioned, how many hours to trace it end-to-end — and how much product would you pull while you look?" |
| SG&A explosion | SG&A as % of revenue trending up, >20% | Financial analytics, cost allocation | "SG&A grew [X]pp faster than revenue — which line item would you look at first if you could see it weekly?" |
| Thin gross margin (<5%) | DBD income statement, margin compression | Cost accounting, margin analysis by product/customer | "At [X]% net margin, one mispriced product line can erase the year — do you know margin per SKU today or per company?" |
| Greenfield factory in construction | New registration, zero revenue, large PP&E | Full ERP + MES from day one | — |
| China imports / material sourcing | ImportYeti, trade data, BoM complexity | Multi-currency procurement | — |
| Japan/Germany exports | ImportYeti, quality requirements | Traceability, lot tracking | — |
| Seasonal demand spikes | Trade data patterns, industry seasonality | **APS/demand planning (T100/Dinghua tier ONLY — iGP = LRP + exception reports)** | — |
| Piece-rate / per-worker pay (งานเหมา) | Labor-intensive TSIC, piece-rate job posts, KPI/bonus mentions | **eMES Phase 2** (worker tap/scan, per-piece ACTUAL cost — never SFC/SFT) | "Do you pay piece-rate on counted actuals or estimates — and who checks?" |
| Per-individual efficiency / real-time floor asks | "ดูประสิทธิภาพรายบุคคล", "real-time ถึงไหนแล้ว" phrasing in posts/news | **eMES Phase 2** (Phase-1 ERP cannot deliver worker-level data) | — |

**Usage rules**: (1) Select ONLY the rows that apply to THIS company based on actual evidence — never copy the whole table. (2) The ฿-question column is INTERNAL-fenced material: always a validating QUESTION with its assumption named, rendered as a range — never a declarative loss claim (VP veto class). (3) KSF3 sizing: state the arithmetic and the flag `clears / does not clear ฿1M THB` — never a numeric score.

### 14. DBD Fallback Source Coverage Matrix

When DBD DataWarehouse is unavailable (529/WAF), use these alternatives. Not all sources provide the same data:

| Data Field | DBD | Creden.co | DataForThai | Longdo Biz |
|-----------|-----|-----------|-------------|------------|
| Tax ID | ✅ | ✅ | ✅ | ❌ |
| Registration date | ✅ | ✅ | ✅ | ❌ |
| Capital | ✅ | ✅ | ✅ | ✅ |
| Directors | ✅ | ✅ | ❌ | ❌ |
| Signing authority | ✅ | ❌ | ❌ | ❌ |
| TSIC code | ✅ | ✅ | ✅ | ❌ |
| Business objective | ✅ | ❌ | ❌ | ❌ |
| 5-year balance sheet | ✅ | Summary only | ❌ | ❌ |
| 5-year income statement | ✅ | Summary only | ❌ | ❌ |
| Related companies | ✅ | ❌ | ❌ | ❌ |
| Investment by nationality | ✅ | ❌ | ❌ | ❌ |

**Key**: Creden provides company profile + summary financials (latest year only). DataForThai provides registration data but no financials. Longdo Biz is minimal. For full 5-year financials, DBD DataWarehouse has no substitute.

### 15. ERP Name Pack + Detection Heuristics (D1 / Search 6)

Check every tech/job/news hit against this pack. Every evidence line carries a DATE; >24 months → confidence auto-Low + a "confirm current system" discovery question.

| Name (variants) | What it implies | Play |
|---|---|---|
| SAP S/4HANA, ECC | Global-mandate enterprise | Plant-level COMPLEMENT (eMES/WMS) — never core displacement |
| SAP Business One (B1) | SME edition; often a LOCAL plant choice | Displacement possible; authority may be local (verify) |
| Oracle / NetSuite | Enterprise or cloud SME | EOL/renewal timing matters — Oracle EOL = 動機-L1 trigger |
| Dynamics 365 / BC | Mid-market, SI-led | Check SI relationship; recently-implemented = complement play |
| **Epicor** ⚠ | **Actively hunting in TH Tier-1/2 precision mfg (beat us at TN Advance 2026-06-29)** | If present/evaluating → competitive urgency; escalate to Peter |
| Infor / IFS | Mid-enterprise niches | Displacement case-by-case |
| **Express (เอ็กซ์เพรส)** | **TH SME accounting market leader** — accounting-only, no mfg depth | Classic upgrade path: accounting → mfg ERP |
| WINSpeed / Formula / CD-Organizer / Mac-5 / Prosoft | Thai/local accounting-ERP packages | Same upgrade path; their accounting FIRM often drove the choice |
| Odoo | Small Chinese-owned cos commonly | Pitch manufacturing depth (BOM/costing) |
| Kingdee 金蝶 / Yonyou 用友 | PRC-owned plants | Mandarin pitch; group-mandate check |
| **TIPTOP** | **= DigiWin family — FRIENDLY base** | In-family: upgrade/expansion play (T100 path), never "displacement" framing |
| บัญชีสำเร็จรูป / "ใช้ Excel" / none | No system | Greenfield play — the most common TH SME reality |
| "ERP Implementation Consultant/PM" job posts, SI project news, vendor case study naming them | **evaluation-in-progress / recently purchased** | Window may have closed → complement play (eMES/WMS); find out WHAT and WHEN |

Also sweep: the company's **SI / accounting firm / audit firm** relationships (Thai SMEs frequently buy what their firm carries) — record as evidence rows with the firm named.

### 16. Urgency-Trigger Taxonomy (D3) — Date-first table, every row tagged

Output table columns are ALWAYS `| Date | Trigger | Evidence | Source |` (Date first — boundary rule). System-EOL triggers are written "System EOL — …" (never "ERP" leading a cell).

| Trigger | → 動機-L1 mapping | Evidence patterns / Thai search strings |
|---|---|---|
| New factory / land purchase / plant expansion | 新廠非做不可 | โรงงานใหม่ / ขยายโรงงาน / ซื้อที่ดิน; PP&E jump in DBD |
| BOI approval / new promotion | Compliance + investment window | บีโอไอ อนุมัติ / ส่งเสริมการลงทุน + year |
| Hiring surge (production/IT) | Growth outpacing systems | สมัครงานจำนวนมาก; JobThai counts |
| IPO / แปรสภาพ (Ltd→Plc) | Audit-grade systems required | DBD status; SET/MAI news |
| System EOL — (vendor sunset, WinXP-era, unsupported) | 系統斷炊非做不可 | vendor EOL notices; "ระบบเก่า" complaints |
| Regulation: e-Tax phase-in, CBAM (exporters to EU) | Compliance deadline | กรมสรรพากร e-Tax; CBAM + industry |
| Relocation / lease expiry | Move = re-implementation moment | ย้ายโรงงาน news |
| Succession / 2nd-gen taking over | 接班要制度 | ทายาท/รุ่นสอง on /about, news |
| Major customer win / 驗廠 requirement | Customer-forced upgrade | got new OEM customer; audit requirement mentions |

≥3 dated candidate triggers or the explicit line "no timing trigger found".

### 17. Group-Map Method (D2) — evidence rules

1. **Collect (Sonnet agent, passive only):** per-director DBD/creden/dataforthai cross-holding searches; shared-address hits; DBD "related companies" listings; succession/role signals from public pages. Every line carries its public source URL. No LINE adds, no FB follows, no connection requests; LinkedIn snippets only; family by ROLE relevance only, never minors/personal-life.
2. **Synthesize (orchestrator, top tier):** a sister-entity claim requires **≥2 independent signals** (shared director AND shared address, or an explicit DBD related-companies listing). One name match = "possible, unverified" line only (Thai name collisions are common).
3. **Render:** group members as TABLE ROWS in `## Group Structure & Decision Map` — **never as headings** (forbidden-heading rule: `Entity N / Primary target / Secondary target / Sibling` split the ingest parser). Column-1 text must never start with words matching whole-file label regexes (`Export…, Tax ID, Website, Facebook…`) — prefix with the relation if needed ("Member — X Trading"). When this section exists, the dossier MUST carry an explicit `Exports:` line (real markets or exactly `Exports: not found`).
4. **One row per legal entity** (hard rule): every confirmed entity has its OWN DBD record; a sister becomes its own gold standard/DB row only after Peter confirms or DBD lists it — never from a name-collision guess.
5. Decision-map hypothesis (守門員/決策者/核決者) is INTERNAL-fenced, Low confidence, and never lifts 三角色決策 above `inferred`.
