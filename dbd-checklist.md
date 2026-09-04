# DBD DataWarehouse Research Checklist

## Mandatory Steps — Do ALL steps for EVERY company. No skipping.

### Phase A: Search & Identify

- [ ] A1: Navigate to datawarehouse.dbd.go.th
- [ ] A2: Close warning dialog (button "ปิด")
- [ ] A3: Search company name using the **Search Fallback Chain**:
  1. Thai name (if known)
  2. Thai transliteration variant 1 (if Chinese input)
  3. Thai transliteration variant 2 (if Chinese input)
  4. English name
  5. Web search → find registered Thai name → retry DBD
  6. Search by Tax ID / registration number (if found from web)
  7. Try alternative sources: data.creden.co, dataforthai.com
- [ ] A4: Record search results table (ALL companies found):
  - Tax ID, Company Name, Status, TSIC Code, Province, Capital, Revenue, Profit, Assets, Equity
- [ ] A5: Identify related companies (same group, same family name, JV partners)
- [ ] A6: **Anomaly check on search results**:
  - Multiple entities with similar names? → may be group companies
  - Entity with status "แปรสภาพ"? → converted Ltd → Plc., check OLD entity for historical data
  - Entity with status "เลิก"? → dissolved predecessor, note for context
- [ ] A7: Click the TARGET company row to open full profile

### Phase B: Company Profile

- [ ] B1: Record ชื่อนิติบุคคล (Legal name — Thai AND English if shown)
- [ ] B2: Record เลขทะเบียนนิติบุคคล (Tax ID)
- [ ] B3: Record ประเภทนิติบุคคล (Company type: บจก. / บมจ. / หจก.)
- [ ] B4: Record สถานะ (Status)
- [ ] B5: Record วันที่จดทะเบียน (Registration date)
- [ ] B6: Record ทุนจดทะเบียน (Registered capital)
- [ ] B7: Record กลุ่มธุรกิจ (Business group: ผลิต/ขายส่ง/บริการ)
- [ ] B8: Record ขนาดธุรกิจ (Business size: S/M/L)
- [ ] B9: Record ที่ตั้ง (Address)
- [ ] B10: Record ALL กรรมการ (Directors) with full names
- [ ] B11: Record กรรมการลงชื่อผูกพัน (Signing authority — who can sign)
- [ ] B12: Record ประเภทธุรกิจ (TSIC code + description) — BOTH registration AND latest filing
- [ ] B13: Record วัตถุประสงค์ (Business objective)
- [ ] B14: Record ปีที่ส่งงบการเงิน (Years of financial filings available)
- [ ] B15: Record สัดส่วนการลงทุน (Investment by nationality) — if shown
- [ ] B16: **SPV Detection Check**: Does the profile show ALL of these red flags?
  - Single director
  - Zero or near-zero revenue
  - Very new registration (< 2 years)
  - Large capital relative to operations
  - If YES → flag as POSSIBLE SPV, search for related operating entity

### Phase C: 5-Year Balance Sheet (งบแสดงฐานะการเงิน)

- [ ] C1: Click "ข้อมูลงบการเงิน" tab
- [ ] C2: Confirm "งบแสดงฐานะการเงิน" is showing (default view)
- [ ] C3: Record for ALL available years (typically 2563-2567 / 2020-2024):
  - ลูกหนี้การค้าสุทธิ (Trade receivables)
  - สินค้าคงเหลือ (Inventory)
  - สินทรัพย์หมุนเวียน (Current assets)
  - ที่ดิน อาคารและอุปกรณ์ (PP&E)
  - สินทรัพย์ไม่หมุนเวียน (Non-current assets)
  - สินทรัพย์รวม (Total assets)
  - หนี้สินหมุนเวียน (Current liabilities)
  - หนี้สินไม่หมุนเวียน (Non-current liabilities)
  - หนี้สินรวม (Total liabilities)
  - ส่วนของผู้ถือหุ้น (Equity)
- [ ] C4: **If fewer than 5 years**: Check if company is newly registered or if entity was converted (see A6)
- [ ] C5: **If entity was converted**: Navigate to OLD entity and extract its historical financials too

### Phase D: 5-Year Income Statement (งบกำไรขาดทุน)

- [ ] D1: Click "งบกำไรขาดทุน" button
- [ ] D2: Record for ALL available years:
  - รายได้หลัก (Main revenue)
  - รายได้รวม (Total revenue)
  - ต้นทุนขาย (COGS)
  - กำไร(ขาดทุน) ขั้นต้น (Gross profit) — if available
  - ค่าใช้จ่ายในการขายและบริหาร (SG&A)
  - รายจ่ายรวม (Total expenses)
  - ดอกเบี้ยจ่าย (Interest expense)
  - กำไร(ขาดทุน) ก่อนภาษี (Pre-tax profit)
  - ภาษีเงินได้ (Income tax)
  - กำไร(ขาดทุน) สุทธิ (Net profit)
- [ ] D3: **If entity was converted**: Combine old + new entity data into continuous series

### Phase E: Financial Trend Analysis

**For OPERATING companies (with revenue history)**:

- [ ] E1: Calculate for each year:
  - Profit margin (Net profit / Revenue)
  - Gross margin (Gross profit / Revenue)
  - D/E ratio (Total debt / Equity)
  - Inventory as % of assets
  - Revenue YoY growth
  - SG&A as % of revenue
  - Current ratio (Current assets / Current liabilities)
- [ ] E2: Identify KEY TRENDS:
  - Revenue: growing / stable / declining?
  - Profit: improving / stable / deteriorating?
  - Inventory: growing faster than revenue? (BFC pattern = WMS opportunity)
  - SG&A: growing faster than revenue? (NutritionProfess pattern = cost analytics opportunity)
  - Debt: increasing or decreasing?
  - PP&E: investing or depreciating?
  - Interest burden vs net profit
- [ ] E3: Map financial trends to Digiwin pain points using the authoritative Pain-Product mapping in `extraction-schema.md` Section 13. Select ONLY rows that apply to THIS company based on actual evidence.

**For GREENFIELD companies (pre-revenue)**:

- [ ] E1g: Calculate:
  - Capital deployment rate (how much of registered capital is now in assets?)
  - PP&E build-out (% of total assets in fixed assets)
  - Burn rate (monthly SG&A / operating loss)
  - Months of runway (current assets / monthly burn)
- [ ] E2g: Assess production readiness:
  - PP&E >50% of total assets? → factory likely built, commissioning phase
  - PP&E <20% of total assets? → still in planning/early construction
  - Inventory appearing? → trial production may have started
  - Revenue appearing? → early sales / trial shipments
- [ ] E3g: Map to Digiwin opportunity using `extraction-schema.md` Section 13 (Pain-Product mapping). Key greenfield rows: "Greenfield factory in construction", "Group company / multi-entity", "BOI promoted".

### Phase F: Save Gold Standard

- [ ] F1: Write complete gold standard file at `docs/gold-standard-[company-id].md`
- [ ] F2: Include ALL of:
  - Search strategy and results (what worked, what didn't — for skill learning)
  - Full company profile (all Phase B fields)
  - Ownership analysis with evidence
  - Complete financials (all Phase C + D data, all years)
  - Trend analysis (Phase E calculations and interpretation)
  - Pain → Product mapping
  - Fit assessment with score and reasoning
  - 六要素 status (what's known vs unknown)
  - All sources with URLs
- [ ] F3: Flag any entity anomalies (SPV, conversion, greenfield) prominently at the top

## Completion Rule
**Do NOT report "finished" until ALL checkboxes in phases A through F are complete.**
**If any phase is blocked (e.g., WAF), note it explicitly and attempt workaround (Creden.co, DataForThai) before marking as blocked.**

## Fallback Sources (when DBD has issues)

| Source | URL | What it provides | When to use |
|--------|-----|-----------------|-------------|
| Creden.co | data.creden.co | DBD mirror, cleaner UI | DBD financial tabs broken |
| DataForThai | dataforthai.com | Company profiles, registration numbers | Finding correct Thai name |
| Longdo Biz | longdo.com/biz | Company directory | Basic verification |
| SET/MAI | set.or.th | Listed company filings | For public companies |

## Phase G: Director Cross-Holdings & Group Capture (DEEP tier only)

Run after Phase F, while the DBD browser session is still open.

- [ ] G1. For EACH director from Phase B: search the director's name on DBD (and creden.co/dataforthai as fallback). Record every other company where the name appears: company name, tax ID, status, TSIC, role. **One line per hit, with source.** (Thai given-name+surname collisions are common — these are RAW HITS, not confirmed relations.)
- [ ] G2. Capture the DBD "related companies" listing for the target (if shown) — these ARE registry-confirmed relations.
- [ ] G3. Shared-address sweep: search the registered address; record co-located entities.
- [ ] G4. Both-TSIC rule (restated): capture registration-time AND latest-filing TSIC for the target AND any confirmed related entity — the delta is sales intel (business drift).
- [ ] G5. Authority-check outputs: from Phase B's director list + signing conditions, produce the material for the dossier's `AUTHORITY CHECK:` lines — full legal-signatory name(s), binding conditions (จำนวนกรรมการ ลงชื่อร่วม / ตราประทับ), and which known CONTACTS are / are not on the registry list.
- [ ] G6. Hand ALL raw hits to the orchestrator — the ≥2-independent-signals rule and the group tree are built top-tier (extraction-schema §17), never in this phase.
