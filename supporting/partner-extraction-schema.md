# Partner Extraction Schema — what to collect on a partner/distributor candidate (v1)

Ten categories. Each carries: what to extract → which Template P slot it fills → evidence patterns → search strings. Calibrated by NOVA due-diligence tiers (partner-knowledge §11.8): **Tier 1 = desk (this skill's job, filters ~70%) · Tier 2 = meeting-only · Tier 3 = pilot-only** — the last two become Discovery Priorities, never fabricated dossier facts.

## §1 Company basics (= sell-to rigor, unchanged)
Legal names TH/EN, Tax ID, type, status, registration date, capital, TSIC reg+latest, address/province, website/FB/LINE OA, phone/email. → Phase B. Source: DBD (follow `~/.claude/skills/digiwin-research-company/dbd-checklist.md` Phases A–F verbatim; Phase G on --deep). **No <5M capital disqualification** — micro = "betting on person, not company" flag (Topnotch precedent). DQ only: dissolved/liquidating, integrity red line.

## §2 Carried vendor lines & authorizations
Brands/products they resell or integrate, authorization level (certified partner / project-based / informal), since when. → Carried Vendor Lines table (col-1 = brand name, Rule-10-safe).
- Evidence: website /partners /products pages; vendor logos; press releases; **rival vendors' own certified-partner directories** (SAP PartnerEdge finder, Odoo partner list, Microsoft partner directory, Epicor partner page); Thai gov procurement/tender records (which brand do they win with).
- Search: `"[company]" authorized distributor OR partner OR reseller` · `"[company]" ตัวแทนจำหน่าย OR พาร์ทเนอร์ OR ผู้แทนจำหน่าย` · `site:sap.com OR site:odoo.com "[company]"` · check §5 conflict pack.

## §3 Install base & customer references
Named customers, case studies, reference sites, segments and provinces served, project types. → Carried Vendor Lines (customer/case table) + `market_access` dim evidence.
- Evidence: /portfolio /our-customers /case-study pages (crawl EACH, Gate-#8 discipline); FB posts tagging client sites; tender awards.
- Search: `"[company]" ผลงาน OR ลูกค้าของเรา OR case study` · `"[company]" โครงการ OR ติดตั้ง site:facebook.com`.
- Anonymous portfolios ("a leading logistics company") = weak signal — record but status ≤ partial (COMMIT pattern).
- **Third-party reputation modality (NOVA 考官 N1 — Thai low-web-profile SIs are desk-invisible):** sweep what CAN be swept passively (industry-association member lists, rival-vendor channel pages, tender records, review sites), then emit the un-sweepable checks as **Discovery Priorities Tier-1.5 Peter-phone tasks** — never impersonate or contact from the research loop. **Targeting rule (NOVA PQ12 — 打草驚蛇 + Kreng Jai):** prioritize NON-competing third-party suppliers who worked non-ERP projects with the candidate (hardware vendors, cloud-infra providers) and probe 交付態度 + 付款信用 — more truthful than asking their customers directly, and doesn't tip the tight Thai IT/SI circle.

## §4 Bench & delivery capability
Headcount (est.), roles split (sales/presales/consultants/engineers), staff certifications ("Bench certs" label per Rule 10), languages TH/EN/中文, service model (L1/L2 support, project delivery, on-call), hiring activity. → Bench & Delivery Capability table + `technical_deliverability` + 顧問段.
- **Their job posts = GROWTH/COMMITMENT signal (inverted from sell-to D1** where job posts reveal the incumbent stack).
- Evidence: /about /team pages; LinkedIn company headcount (snippets only); JobThai/JobsDB postings; FB team photos; training-academy pages.
- Search: `"[company]" สมัครงาน OR รับสมัคร วิศวกร OR ที่ปรึกษา` · `"[company]" site:linkedin.com/company` · `"[company]" อบรม OR training academy`.

## §5 Vendor-line name pack + CONFLICT pack
**Rival-line name pack** (any hit in §2 → `CONFLICT-CANDIDATE` flag): SAP (B1/ByDesign) · Oracle NetSuite · Microsoft Dynamics/BC · Epicor ⚠ active-in-TH · Infor · Odoo · Kingdee 金蝶 · Yonyou 用友 · Express/WINSpeed/Formula/Mac-5 (TH local ERP) · WMS rivals (Manhattan, Blue Yonder, local WMS) · MES rivals (Siemens Opcenter, local SCADA-MES) · **TIPTOP = DigiWin family (friendly)**.
**Internal conflict roster** (proposed scope tested against EVERY row — memory `reference_distributor_candidates_7` is the source of truth; verify before citing):
| Entity | Tax ID | Status |
|---|---|---|
| SMK Automation | 0115549006382 | SIGNED — eMES DA HDDL-2026-SMK-001 |
| Scada Automation | 0105543080998 | locked-7 A類 |
| ADTESO | (Samutprakarn) | locked-7 A類 |
| IBAC | (see memory) | locked-7 B類 |
| The Accounting of Sudthicha | (independent) | locked-7 B類 |
| Topnotch | 0105568098114 | locked-7 B類 micro |
| DotLinkCloud | (see memory) | locked-7 edge |
| Vow Squad | 0105568123348 | locked-7 edge |
| PLIC Corporation | 0105539024132 | WMS distributor/VAR candidate (scope w/ VP) |
| A&M (Thailand) | 0105568062632 | alliance track |
| 象田 Xiangtian | (supplier) | supplier_partner — NOT a distributor |
→ Conflict Exposure fence + `Conflict check:` line. Overlap = escalate, never silently resolve.
**Competitor-line decision tree (NOVA PQ8):** rival is mainstay + overlapping → REFUSE flag · rival marginalized → sign-with-exclusivity-clause note · complementary → firewall/segmentation note.

## §6 Territory & segment coverage
Provinces/estates served, branch offices, industry niches with real domain knowledge (from §3 cases), customer-size band they sell into. → `market_access` dim + Conflict Exposure (territory test).
- Evidence: /contact branches; case-study locations; FB check-ins.
- Search: `"[company]" สาขา OR branch` · case locations from §3.

## §7 Partner economics signals
Their pricing culture (high-end vs price-fighter), deal sizes they handle, existing margin structures if public, MDF/co-marketing behavior (do they run events?). → `economics` dim + Engagement & Economics Hypothesis fence.
- Evidence: tender award amounts; event sponsorships; the brands they carry (SAP-line = high-ticket culture — NOVA PQ8 tier-1); their published packages/prices.
- Benchmarks for the hypothesis: partner-knowledge §11.4 (tiers/rebates/minimum viable ≈ 4-5 deals yr-1) + §6 SMK actuals for Thailand.

## §8 Partnership decision process
Who signs (DBD directors vs the champion), owner's public posture, parent-company approval layers (A&M US-approval pattern; Japanese-MD pattern at PLIC), succession/2nd-gen roles. → `decision_process` dim + Key People prose + AUTHORITY CHECK (DA-signing framing).
- Evidence: DBD director list + signing rule (Phase B); /about leadership; news interviews.
- PASSIVE OSINT only — no LINE adds, no connection requests; people-claims carry public source URLs; never minors/personal-life detail.

## §9 Financial credibility (channel lens)
DBD 5-yr revenue/profit/equity/D-E, asset profile (investing integrator like PLIC PPE-3× vs asset-light), cash runway read. → Phase C–E + `financial_credibility` dim + Activation Readiness fence.
- **The question is NEVER "can they buy ERP" — it is "can they carry payroll through the SMK activation clock (+1/+3/+5mo) and survive to yr-1 3 orders"** (≈ 1 sales + 1-2 consultants dedicated; NOVA §11.4: yr-1 breakeven ≈ $120K USD revenue ≈ 4-5 deals).
- Micro/dormant books (COMMIT pattern) → capability lives in the person, not the entity — say so. **定版 warning (PQ14): micro/dormant credibility CAPS technical_deliverability + exclusivity_conflict at lowest rating; no-agency-record + asset-poor → conflict read = 安全底細不明 (shell risk), never a neutral "inferred"; referral engagement = first deal 100% prepaid.**

## §10 Commitment & motivation signals (dated, like sell-to §16)
| Signal | Reads as |
|---|---|
| Hosting sector events/webinars/forums | Market-building investment (COMMIT's hospital forum) |
| Training academy / certification investments | Enablement-ready DNA |
| Inbound approach to DigiWin (who called whom, what they asked) | `motivation` evidence — decode 中間商 vs co-sell |
| Hiring software/consultant roles | Capability-gap closing on their side |
| New office/branch/capital increase | Growth commitment 【DBD】 |
| Owner personally in the room vs delegate | 企圖 (NOVA PQ1: owner attention is scored) |
| "不想養人 / 輕資產" statements, refuses training | Permanent-referral-only flag (NOVA PQ7) |
Every signal DATED + source-tagged. → `motivation` + `capability_gap` dims + 60-SECOND READ.

## Per-dim evidence guide (what CONFIRMED looks like — examples from real cases)
| dim_key | ≥2 evidence patterns | TH search | EN search |
|---|---|---|---|
| `motivation` | inbound call/visit record; owner quote in meeting; event they invited us to | `"[company]" ร่วมมือ OR พันธมิตร` | `"[company]" partnership announcement` |
| `capability_gap` | absent capability on /services vs their stated ambition; hiring for it; PLIC "no software team" | `"[company]" รับสมัคร นักพัฒนา OR ที่ปรึกษา ERP` | `"[company]" careers software consultant` |
| `market_access` | named client roster; tender wins; estate/province branch map | `"[company]" ลูกค้าของเรา OR ผลงาน` | `"[company]" clients case study` |
| `economics` | published reseller terms; tender pricing; carried-brand tier pages | `"[company]" ราคา OR แพ็กเกจ` | `"[company]" reseller program terms` |
| `exclusivity_conflict` | rival partner-directory listing; tender records by brand; §5 roster overlap | `"[company]" ตัวแทน SAP OR Oracle OR Epicor` | `site:<rival>.com "[company]"` |
| `decision_process` | DBD signing rule; /about leadership; press interviews naming decision-maker | `"[company]" กรรมการ OR ผู้บริหาร` | `"[company]" managing director founder` |
| `financial_credibility` | DBD Phase C–E; capital events; DBD status | (DBD DataWarehouse) | (DBD DataWarehouse) |
| `technical_deliverability` | bench certs on /about; delivered-project tech detail; vendor certifications; **Thai-localization Go/No-Go: evidence of Thai tax/report/UI delivery + Thai-language support (absence on an ERP-ambition candidate = blocking sub-check, NOVA 考官 N3)** | `"[company]" ใบรับรอง OR ผ่านการอบรม OR ภาษีไทย ระบบ` | `"[company]" certified engineers PLC SCADA Thai localization` |

## Slot ↔ category matrix (audit anchor)
| Template P slot | Fed by |
|---|---|
| 60-SECOND PARTNER READ | all §1–§10 (synthesis) |
| Phase A | run log |
| Phase B / Directors / Ownership / Phase C–D | §1, §8, §9 |
| Phase E Financial Credibility Read | §9 |
| Carried Vendor Lines & Install Base | §2, §3, §5 |
| Technology & Systems | §1 (their own stack — usually no-signal) |
| Products & Services (What They Do) | §1, §3 |
| Certifications | §1 |
| Bench & Delivery Capability | §4 |
| Partner Assessment (8 dims + lines) | §2–§10 per the dim guide |
| Engagement & Economics Hypothesis | §7, §10 + partner-knowledge §5/§11.4 |
| Conflict Exposure | §5, §6 |
| Activation Readiness | §4, §9 + partner-knowledge §6/§11.2 |
| Key People + AUTHORITY CHECK | §8 |
| Group Structure & Decision Map (optional) | §1, §8 |
| Warm Base | MySQL cross-ref |
| Discovery Priorities | every Tier-2/Tier-3 gap from §1–§10 |
| Reflection Summary / Sources | run audit |
