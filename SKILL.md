---
name: digiwin-research-company
description: >
  Use when investigating a prospective or unknown manufacturing company before a
  sales meeting, or adding one to the pipeline. Triggers: "research [company]",
  "look up / who is [company]", "prep for the meeting with [company]", "company
  intel on [company]", "design doc for [company]", "deep research [company]" or
  "--deep" (deep tier), a fresh name card, or any unfamiliar company in the
  leads sheet / Drive Inbox that needs DBD registry + deep-website investigation
  before a sales call.
---

# /digiwin-research-company (v4)

Research a Thai manufacturing company for Digiwin ERP sales preparation. Two tiers: **QUICK** (default, ~10 min triage) and **DEEP** (`--deep`, 35–55 min, 4 parallel research agents — run before any first visit, for C2-candidates, or when Peter says so).

## Context

You are helping Peter Lo, Head of Distributor at Digiwin Thailand, research a prospective company before a sales meeting. Digiwin sells manufacturing ERP with 44 years of expertise and 55,000+ clients. Peter needs to understand the company well enough to position Digiwin as the right ERP partner.

Companion files (in **this skill's directory**, `~/.claude/skills/digiwin-research-company/`):
- `extraction-schema.md` — data points to collect + the authoritative pain→product table (§13), ERP name pack (§15), urgency taxonomy (§16), group-map method (§17)
- `dbd-checklist.md` — mandatory DBD DataWarehouse extraction steps (Phases A–F; Phase G in deep tier)
- `briefing-template.md` — output formats (A operating / B greenfield / C SPV-unresolved; partner Template D retired → /research-partner) + the canonical 六要素 table
- `scripts/check_contract.py` — the REQUIRED output-contract checker (Gate mechanization)
- `nova-knowledge.md` — DigiWin institutional priors elicited from the NOVA agent (entry wedges, incumbent base rates, ROI benchmarks, qualification gates/red-flag formulas, trigger rankings, family-firm authority playbook). READ at Step 5; priors sharpen hypotheses and deal structure but NEVER substitute for evidence — tag reliance 【推論 calibrated by NOVA KB <date>】 and keep it inside internal fences.
- `nova-live-consultation.md` — **MANDATORY in-loop procedure: ask the LIVE NOVA agent (Playwright/Teams) whenever a judgment call cannot be grounded in run-evidence or the cached KB** (Peter, 2026-07-17: "ask NOVA whenever you have questions, ask where you need to, so you are undoubtedly confident"). The cached `nova-knowledge.md` is priors; the queue is for later; this is real-time. Read at Step 4/5 and consult AS the residual questions surface. Tag answers 【NOVA live <date>】 inside internal fences; encode durable priors back into `nova-knowledge.md`.

**Environment:** assumes cwd = `/Users/peterlo/digiwin_automation` (repo root) — `docs/`, `database/`, `docs/token-ledger.csv` are repo-relative. **MySQL must be up even for the Gate-#13 dry-run** (`~/.my.cnf`); if it's down, the run can complete but the dossier CANNOT be promoted (Gate #13 INCONCLUSIVE).

## Step 0: Tier, Output Banners & Audience

**Tier selection:** `--deep` anywhere in the arguments (or "deep research") = DEEP tier. Otherwise QUICK.

**Every output file starts with these two blockquote lines (greppable, in this order):**
```
> Research tier: QUICK | DEEP · v4 · deep sections: present | absent (run --deep)
> INTERNAL WORKING DOSSIER — Peter/DigiWin TH only; never forward; strip 【推論】 + fenced blocks before any external use
```
The gold standard is an **internal working dossier** — it contains inference (【推論】), decision-role hypotheses and pipeline context that must never reach a customer, HQ colleagues outside the deal, or any forwarded artifact. Blockquote lines are parser-invisible (verified against the ingest parser).

## OUTPUT CONTRACT — ingest-boundary rules (LOAD-BEARING; violations corrupt the DB/Sheet)

The gold standard feeds `database/ingest_md_to_db.py` (deterministic parser) → MySQL → the nightly Google-Sheet sync. These rules were red-team-verified against the live parser (2026-07-09). **check_contract.py enforces them.**

1. **Required headings, verbatim (never rename):** `## Directors` · `## Key People` · `## Ownership …` · `## Technology & Systems` · `## What They Make` (or `## Products …`) · `## Certifications …` · `## Sources` (or `All Sources`). Row labels the parser matches: Tax ID / Legal name (TH/EN) / Website / Facebook / Company type / Signing authority.
2. **FORBIDDEN headings at any level ##–####:** any heading beginning `Entity N`, `Primary target`, `Secondary target`, or `Sibling` — the parser SPLITS the file on these, discards everything before the first match, and mints bogus company rows. Group members are always TABLE ROWS, never headings.
3. **Inference NEVER as rows inside ingested sections.** `## Technology & Systems` = ONE table, only evidence-backed named systems (confidence High/Medium, dated evidence). No-signal is a **blockquote line under the table**, never a row (a row is only acceptable if the vendor cell literally starts with `Unknown`). Verdicts/EOL-hints are prose in the non-ingested `## ERP Incumbent Read 【推論】` section.
4. **Key People = prose paragraphs ONLY. Never pipe tables, never bullet lists.** (KP tables ingest as registry *directors* unconditionally — the exact corruption the authority-check exists to prevent.) When DBD directors are paywalled, write the prose line `Directors: PENDING (paywalled)`.
5. **`## Directors`:** the directors table is the FIRST table in its section. Extra columns (e.g. "Other directorships") are safe. **Keep the labelled line `Signing authority: <name(s)>`** — a Signing column is invisible to the parser. Sibling/candidate tax-ids never appear in a row whose first cell matches `Tax ID / Juristic ID / เลขทะเบียน` — and NEVER write `Tax ID (current)` for anything but the primary entity.
6. **New-table first-column discipline:** col-1 text must never match the parser's whole-file label regexes (`erp\b`, `export\b`, `certification`, `tax id`, `^website`, `facebook`, `company type`). Hence: `## Urgency Signals & Timing Triggers` columns are `| Date | Trigger | Evidence | Source |` (Date first), and system-EOL triggers are written "System EOL — …" (never "ERP …" in any cell that could lead a row).
7. **When `## Group Structure & Decision Map` exists, the dossier MUST carry an explicit exports line** — either real markets or exactly `Exports: not found` (the parser's exact null token; "none found" would ingest as a region). Otherwise a group-member name containing "Export/Trading" gets scavenged into export_markets (proven).
8. **THIRD-PARTY IDENTITY (added 2026-08-31 — the Sun Robotics burn).** EVERY third party named
   anywhere in the dossier — referring partner, distributor, JV entity, supplier, named customer,
   sister company — is resolved to its **13-digit tax ID**, or carries the literal token
   `UNRESOLVED` beside its first mention. A name that arrived as a nickname in field intel
   ("Sunrobot") is NOT an identification. Resolve it BEFORE any strategy is built on it: a whole
   channel strategy was written against the wrong legal entity because this rule did not exist.
   Two similarly named companies are two rows, never merged. Enforced by `osint_redlines.py`.

9. **RELATIONSHIP CLAIMS CARRY EVIDENCE, exactly as system claims do (added 2026-08-31).** Any claim
   that X is Y's parent / subsidiary / JV partner / supplier / distributor / customer carries a
   **source and a date**, and states its grade. **A company's own marketing or About page is NOT
   sufficient evidence of a commercial relationship** — it is self-description, grade it
   【公開-自述】 and say so in the sentence. Ownership is proved by a shareholder register
   (shd.dbd.go.th or a paid หนังสือรับรอง), never by "they announced a JV together". Absent that,
   write the inference AS an inference. The systems rule already demands a date on every evidence
   line and auto-downgrades anything over 24 months; relationships get the same discipline.

10. **STORY SPINE — `## 主角與主線` (added 2026-08-31, from VK's research method).** Every dossier
    carries a story spine, written LAST, after the arms and the self-consistency pass. Two parts:

    - **主角 = the company.** Not the founder, not the industry.
    - **主線 = what is going wrong for them, and why they cannot fix it themselves.** One paragraph,
      plain spoken language, no jargon and no section numbers. For Bosch: *a plant that made money
      for years, was sold, fell over, and now has two thirds of its assets asleep in a warehouse it
      runs on paper - and its new German owner is about to notice.*

    Then the **30-second telling** — VK's small-granularity test, and the hardest one to fake: one
    hook, three points, one closing line, written the way you would say it to a colleague in the car.
    If it cannot be told in 30 seconds, the research is not yet understood, and no amount of
    correct data compensates. This block is what the OSINT report opens with.

    A dossier with a complete Phase A-E and no story spine is an unread file. Peter, 2026-08-31:
    the report must make someone WANT to read it, and must carry them to what to do next.

11. **File placement:** drafts are written to `docs/_eval/gold-standard-<id>.md.draft` and only `mv`-promoted to `docs/gold-standard-<id>.md` after ALL gates pass — a glob-matching filename is auto-committed to the DB by the nightly launchd job whether gated or not. Backups/eval copies must never match the `docs/gold-standard-*.md` glob (use `docs/_eval/archive/` or `*.md.bkp`).

## Step 0.5: PRIOR CONTACT PROBE — run BEFORE any searching (added 2026-08-31)

```
python3 tools/prior_contact.py "<company name>"
```

**Peter records every phone call.** 48 graded meetings sit in `digiwin_osint.meetings` with their
audio and transcript paths, and this skill never looked at one of them: its only transcript
touchpoint was `--reconcile`, which fires AFTER a meeting for a company that already has a promoted
dossier. So research was built assuming no prior contact while the customer's own words were already
on disk. (Its own Asia Poly Sacks burn is the same defect facing the other way: the dossier carried
a stale hypothesis for 18 days after the MD resolved it on a call.)

The probe returns one of two verdicts, and they lead to different research:

- **RECORDED** — a transcript or meeting note exists. **READ IT FIRST.** It outranks every OSINT
  inference in this dossier: what the customer said about his own systems, his own pain and his own
  timing is primary evidence, and any OSINT inference it contradicts is CORRECTED, not averaged.
  Research then fills the gaps the conversation left, and the dossier records what he said with
  【電話/會議 <date>】. If the probe finds AUDIO that was never transcribed, transcribe it — do not
  research around it.
- **COLD** — no prior contact. Research builds the whole picture, and the first-visit deck's job is
  to EARN his framing rather than reflect it.

⚠ The probe also sweeps `transcripts/` and the Obsidian `Meetings/` folder, because a recording may
exist that was never registered in the meetings table — proven on Alumet and Mazuma, where files
existed with no DB row.

## Step 1: Parse Input & Classify Company Type

From the company name:
1. Determine the **input language**: Thai, English, or Chinese
2. Generate name variants for search:
   - English variants: with/without "Co., Ltd.", "Thailand", "Company Limited"
   - Thai variants: if Chinese name given, generate **multiple Thai transliterations** (see Transliteration Guide below)
   - Chinese variants: simplified + traditional if applicable
3. Guess domain: `[company].co.th`, `[company].com`, `[company]thai.com`
4. **Check Obsidian vault first**: `obsidian search query="[company name]"` — may already have data
5. **Check existing gold standards**: look in `docs/gold-standard-*.md` for prior research
6. Create `company_id`: lowercase, replace spaces with hyphens, strip "co-ltd" / "company-limited" / "thailand"

### Chinese-to-Thai Transliteration Guide (CRITICAL for 華商 companies)

When the input is a Chinese company name, you MUST try **multiple Thai transliterations** because:
- Chinese phonemes map to Thai inconsistently
- Different translators produce different spellings
- DBD search is exact-match, so one wrong vowel = zero results

**Common variations to try**:

| Chinese Sound | Thai Variant 1 | Thai Variant 2 | Thai Variant 3 | Example |
|--------------|----------------|----------------|----------------|---------|
| héng (恒) | เฮง | เหิง | เห็ง | 恒立 → เฮงลี่ OR เหิงลี่ |
| zhōng (中) | จง | จ้ง | — | 中力 → จงลี่ OR จงหลี |
| jùn (駿) | จวิน | จุ้น | จวิ้น | 駿馬 → จวินหม่า OR จวิ้นม่า |
| xīng (興) | ซิง | ชิง | — | 興嘉 → ซิงเจีย |
| lì (力/立) | ลี่ | หลี | — | 恒立 → เหิงลี่ (หลี used!) |

**Search fallback chain** (try in this order):
1. Thai name (if known)
2. First Thai transliteration variant
3. Second Thai transliteration variant
4. English name on DBD
5. Web search for "[Chinese name] Thailand" to find the registered Thai name
6. Web search for "[English name] Thailand DBD" or "dataforthai" or "creden.co"
7. Search by Tax ID or registration number (if found from web)

**NEVER give up after one failed search.** The Sitthinon case needed English name. The NutritionProfess case needed the company website. The Hengli case needed 3 transliteration attempts + web search.

## Step 1.5: Partner-Target Detector (route channel candidates to /research-partner)

This skill researches SELL-TO prospects only. Partner/distributor/SI/alliance candidates go to **`/research-partner`** (sibling skill — 8-dim capability read, NOT the sell-to ruler). Signals, checked here and re-checked after DBD Phase B:
- **s1 — Peter's phrasing** contains distributor / partner / channel / 經銷 / 通路 / reseller / SI / co-sell → **hand off outright.**
- **s3 — roster match**: the name matches the partner roster (locked-7 + SMK + PLIC + A&M + Wecon + 象田 — see `~/.claude/skills/research-partner/partner-extraction-schema.md` §5, or live `companies WHERE channel_role<>'prospect'`) → **hand off outright.**
- **s2 — TSIC** ∈ wholesale-software / IT-services / consulting (46510, 46104, 62011–62099, 70209) **AND s4 — website self-describes** as SI / integrator / consultant / reseller → **STOP and AskUserQuestion** ("this looks like a channel candidate, not a sell-to — research as partner?"; the COMMIT rule, 2026-07-17).
- s2 alone (e.g. a trading company) → continue sell-to, note it in the dossier.
A manufacturing prospect (TSIC 2xxxx–3xxxx, business group ผลิต) NEVER routes to partner unless s1/s3 fire.

## Step 2: DBD DataWarehouse (FOUNDATION — always do this FIRST)

DBD DataWarehouse (datawarehouse.dbd.go.th) is the **single most valuable source** for Thai company research. It provides official government-registered data: Tax ID, capital, directors, 5-year financials (revenue, profit, assets, debt), related companies, and business classification. All other research builds on top of this foundation.

### DBD Search Strategy

**Primary method — Playwright browser**:
1. Navigate to https://datawarehouse.dbd.go.th/
2. Close any warning dialog (button "ปิด")
3. Accept cookies if prompted (button "ยอมรับทั้งหมด")
4. Type company name in search box, press Enter
5. If results found → proceed to profile extraction (see dbd-checklist.md)
6. If NO results → try next name variant from the fallback chain

**If DBD Playwright fails** (WAF blocks, site bugs, redirects):
- Try alternative sources for the same data:
  - **data.creden.co** — mirrors DBD data with cleaner interface
  - **dataforthai.com** — another DBD mirror, good for finding registration numbers
  - **longdo.com/biz** — company directory with some DBD data
- Note the limitation in the output and retry DBD later

**Follow the complete DBD checklist** in `dbd-checklist.md` for all extraction steps. **Deep tier also runs Phase G** (per-director cross-holdings + related-companies capture).

### Critical: Detect Entity Anomalies

After extracting DBD data, check for these patterns:

#### SPV / Holding Entity Detection
If ALL of these are true, flag as **POSSIBLE SPV** (not the operating company):
- Zero or near-zero revenue
- Zero inventory
- Zero PP&E (no factory, no equipment)
- Single director
- Large registered capital relative to actual assets
- Very new registration date

**Action**: Search for related entities by director name, address, or parent company. The real operating company is probably registered under a different name.

**Example**: MST Consumer Products — 100M capital, zero revenue, zero PP&E. The SPV entity was found but the actual manufacturing operation runs under a different legal entity.

#### Entity Conversion Detection (Ltd → Plc.)
If the company shows:
- Status "แปรสภาพ" (Converted)
- Very recent registration date for a company that's clearly been operating for years
- Only 1-2 years of financial data despite being described as established

**Action**: Search for the OLD entity (the original บจก./Co., Ltd.) to get historical financials. Combine both entities' data for a continuous financial series.

**Example**: NutritionProfess — converted from บจก. to บมจ. in June 2567. Historical financials (2562-2566) were under the old entity 0105556117593; only 2567 was under the new Plc. entity 0107567000287.

#### Greenfield / Pre-Revenue Detection
If the company shows:
- Registration date within last 2 years
- Zero or near-zero revenue
- Large PP&E growth (factory construction)
- Operating losses (pre-production SG&A burn)

**Action**: Use the **Greenfield Analysis Template** instead of standard trend analysis:
- Focus on: capital deployed, PP&E build-out, burn rate, production timeline
- Sales angle: "Implement ERP BEFORE production ramp-up"
- Parent company analysis becomes critical (who's funding this?)

**Examples**: Hengli (250M, metal mfg), Junma (1.625B, tire cord), Zhongli (150M, auto parts) — all greenfield factories in construction/commissioning phase.

### Early Disqualification Gate (immediately after DBD Phase B)

After extracting DBD Phase B data, check BEFORE running web searches:
- Registered capital < 5M THB → **DISQUALIFIED** (too small for ERP)
- TSIC code is pure retail/services (no manufacturing indicators) → **FLAG** but continue
- Company status = dissolved/liquidating → **DISQUALIFIED**
- Company is a known Digiwin customer → flag as **EXISTING CUSTOMER**

**If DISQUALIFIED**: Produce an abbreviated gold standard (Header + Phase A-B + Fit Assessment with "DISQUALIFIED" + reason). Skip enrichment. This saves significant effort on obvious non-targets (e.g., DD-UTECH: 1M capital wholesale broker).

**If FLAGGED but not disqualified** (e.g., non-manufacturing TSIC): Continue research — many pipeline companies turn out to be wholesale/trading despite assumptions (Mitsuya, Chia Tai, Toyota Tsusho, NutritionProfess).

### Disambiguation Strategy (when DBD returns >5 results)

If DBD search returns many results, filter in this order:
1. **Province** — if known from pipeline data
2. **TSIC code** — 2xxxx = manufacturing (prioritize these)
3. **Registered capital** — >5M THB (skip micro-entities)
4. **Status** — Active only (skip dissolved/liquidating)
5. **Business group** — ผลิต (manufacturing) over ขายส่ง/บริการ

If still ambiguous after filtering, flag as **AMBIGUOUS — NEEDS DISAMBIGUATION** and present top 3 candidates for Peter to choose.

### SOURCE QUALITY FILTER — apply to every web result before citing it

Added 2026-08-31 from VK's research method. We already grade EVIDENCE; we never graded the SOURCE
it came from, and thin pages made it into dossiers as a result.

**Discard on any one of these:**
- under ~500 words
- all bullet points, no argued paragraphs
- no clear conclusion and no visible reasoning
- reads as AI-generated: every point plausible, none carried through
- a list of company names or codes with no analysis

**Keep:** concrete numbers (revenue, share, volumes) · a complete line of reasoning · an explicit
conclusion the author commits to · long structured industry or company analysis.

A discarded source may still be a POINTER — follow its links to the primary document, then cite that.
Registry and filing sources (DBD, BOI, customs) are exempt: they are records, not arguments.

### VISUAL ASSETS — collect them during the crawl (added 2026-08-31)

The first-visit deck mandates a REAL logo and real plant photos, and nobody was gathering them, so
every deck started that hunt from zero. The crawl is already on the site when those assets are in
front of it.

Save to `docs/company-assets/<company-id>/` and record each one in `## Sources` with the page URL it
came from — **the link matters as much as the file**, so a later user can verify it is genuinely
theirs and current. Collect: the logo (highest resolution available), plant or building exterior,
production floor, any certificate image, product shots. Never fabricate or substitute a stock image
for a client's real asset.

### INDUSTRY BRIEF — owned here, not by the deck (added 2026-08-31)

`/digiwin-research-company` owns the industry layer and it is REUSABLE across every company in that
sub-industry. Protocol: `industry-sweep.md` in this skill directory. Index and briefs live in
`docs/industry-briefs/` (see its `INDEX.md`).

- **Standard step for a sub-industry we have NOT briefed before.** Never for the company itself:
  NotebookLM cannot reach DBD, ImportYeti or directors, and its trial run produced confident garbage
  alongside gold. Breadth from the sweep, entity truth from DBD. Sighted triage stays mandatory.
- **Reuse if a brief exists, is under 6 months old, and no regulation in it has moved.** Spot-refresh
  rather than re-run.
- The sub-industry is the EXACT one - woven-PP/FIBC, not "plastics"; PCBA, not "electronics".

### Search 2: Company Profile (Web)
```
WebSearch: "[Company] Thailand" manufacturing OR factory OR products
```
Looking for: overview, industry, products, history, location — to supplement DBD data

### Search 3: Thai-Language Intelligence
```
WebSearch: "[Company Thai Name]" ทุนจดทะเบียน OR ผู้ถือหุ้น OR โรงงาน OR ผู้บริหาร
```
Looking for: additional details not in DBD — shareholder details, factory descriptions, management profiles

### Search 4: Facebook (search BEFORE LinkedIn for Thai companies)
```
WebSearch: "[Company]" site:facebook.com Thailand
```
Looking for: company page, factory photos, product posts, employee count clues, job postings

### Search 5: LinkedIn (snippets only — do NOT WebFetch LinkedIn)
```
WebSearch: "[Company]" site:linkedin.com/company
```
Looking for: employee count, industry classification, headquarters, specialties

### Search 6: Technology Stack + Job Postings (Gate #9)
```
WebSearch: "[Company] Thailand" ERP OR SAP OR Oracle OR Epicor OR Express OR software OR ระบบ
WebSearch: "[Company]" สมัครงาน IT OR ERP OR programmer OR เจ้าหน้าที่ระบบ
```
Check hits against the **ERP name pack** (extraction-schema.md §15): SAP (B1/ECC/S4) · Oracle/NetSuite · Dynamics/BC · **Epicor ⚠ active-in-TH** · Infor · IFS · **Express (TH SME leader)** · WINSpeed · Formula/CD-Organizer · Mac-5 · Odoo · Kingdee 金蝶 · Yonyou 用友 · **TIPTOP (= DigiWin family — friendly!)** · บัญชีสำเร็จรูป · Excel-only. State confidence; date every piece of evidence. (Quick tier = this one search pass = Gate #9-lite. Deep tier expands this into Agent D1.)

### Search 7: News & Growth Signals
```
WebSearch: "[Company] Thailand" news OR expansion OR factory OR ขยาย OR โรงงานใหม่ 2025 OR 2026
```
Looking for: new factories, M&A, leadership changes, awards, financial results

### Search 8: Import/Export Data — US customers & their standards regime (rebuilt 2026-08-11)

**Why this step is worth real effort:** ImportYeti carries **U.S. CBP bills of lading** — a legal
customs filing, same evidence class as a DBD record. The buyer list tells us **what compliance
regime the prospect already has to survive**, and that regime *is* the pain an ERP/MES is bought
for. This is the highest-leverage OSINT we have for exporters.

**Capture (browser, not scripted).** importyeti.com sits behind a Cloudflare bot check: headless is
blocked and an automated headed profile passes only intermittently. **Do not build a retry loop
against that check.** Read the page in Peter's own browser (Chrome extension) or use the site's own
CSV export buttons, then hand the values to the formatter:

```
https://www.importyeti.com/search?q=<company>          # then open the supplier page
python3 tools/importyeti_section.py capture.json       # -> the dossier section
python3 tools/importyeti_section.py --self-test        # regression (Innovalues fixture)
```

**Rules — each one exists because getting it wrong is visible to the client:**

1. **Match by ADDRESS against the DBD record, never by name.** Name search is fuzzy. Check
   "also exports under N names/addresses" first, or an alias entity will make volume look wrong.
2. **Drop freight forwarders from the customer list.** Any consignee containing Logistics /
   Forwarding / Freight / Cargo / Brokerage is a shipping agent. Calling one a "customer" in
   front of the client is an obvious, credibility-destroying error. The tool classifies these.
3. **Est. Shipping Spend is modelled — read the coverage %.** Below ~40%, do not quote it.
4. **Standards regime is a HYPOTHESIS, written as one.** Automotive buyers ⇒ IATF 16949 / PPAP /
   traceability / 8D; medical ⇒ ISO 13485; food ⇒ FSMA/HACCP; toys ⇒ CPSIA. Ask the client to
   confirm; never assert it at them.
5. **No match ≠ does not export — say why it may be absent.** Ocean freight only (air invisible),
   US-bound only (nothing on domestic/intra-Asia/EU/JP), and selling via a **trading intermediary
   hides the maker**. The tool renders these reasons automatically. *~88 existing dossiers say
   "ImportYeti: no data found" with no such qualifier — re-word when next touched.*
6. Free tier = **U.S. Imports** only. US Exports / MX / Customs Clearance are paid.

Also capture when present: shipment time series + YoY trend (a decline is a live discovery item —
for INNOVALUES it corroborated the unexplained 2024 revenue drop already in the dossier),
HS-code product breakdown, and the per-buyer activity sparkline.

Worked example + full capability review: `docs/research-fragments/importyeti-capability-review.md`.
Reference section rendered into `docs/gold-standard-innovalues.md`.

### Search 8.5: Community & Social Sentiment (Thai-local voice — added 2026-07-18 per Peter)
```
WebSearch: site:pantip.com "[Company Thai Name]"
WebSearch: "[Company Thai Name]" รีวิว OR ดีไหม OR ประสบการณ์ OR บริการ
WebSearch: "[Company Thai Name]" ฟ้อง OR คดี OR โกง OR ค้างจ่าย OR ประท้วง OR ไฟไหม้ OR เลิกจ้าง
```
How local people talk about the company: Pantip/forum threads, Facebook page + public group mentions, Google Maps reviews (if agent-side fetch is blocked, pull via main-loop Playwright like DBD), employer reviews (JobsDB/JobThai), TikTok/YouTube, LINE OA presence. **Evidence tier 【公開-社群】 = sentiment-grade, NEVER fact-grade**: reviews and forum claims are perceptions/allegations — write "reviewers allege/say", never restate as established fact; they shape approach and door-openers, not the factual record. PASSIVE ONLY: no login, no posting, no joining groups, no contacting anyone, no minors/personal detail, nothing defamatory ever reaches a customer-facing artifact. B2C-facing companies (consumer brands, retail service) yield rich signal; pure B2B exporters may only yield employer reviews — report absence honestly. Quick tier = this one pass; deep tier expands into Agent D5.

### Search 9: BOI Status
```
WebSearch: "[Company]" BOI OR "Board of Investment" OR ส่งเสริมการลงทุน OR promoted
```
Looking for: BOI promotion, investment privileges, zone, tax benefits

## Step 2.5: Warm-Base Cross-Reference (main loop — read-only local MySQL)

We already know 157+ companies. Cross-reference the target against our own base (SELECT-only via `~/.my.cnf`, database `digiwin_osint` — **never write from the research loop**):
1. **Shared directors:** each director NAME extracted this run vs `directors` table (`SELECT c.name_en, d.name FROM directors d JOIN companies c ON c.id=d.company_id WHERE d.name LIKE …`).
2. **Same industrial estate / province:** `companies WHERE industrial_estate = … OR province = …`.
3. **Group overlap:** `related_entities` + any TIPTOP-family entities.

Output → `## Warm Base & Nearby References` (3–5 lines, each tagged 【DB】), INSIDE the INTERNAL fence:
- **Live pipeline deals are NEVER named** (deals live in the Google Sheet, not here): write "an active opportunity in the same estate — ask Peter", never the company name.
- Signed customers may be named ONLY if reference-approved; otherwise "a DigiWin client 2km away (reference approval TBC)".
- Tag every hit `direct|distributor` — never blend the two books.
- MySQL down → write `> Warm base: DB unavailable — skipped` and continue (never fail the run).

## Step 3: Enrichment — QUICK tier (default)

Based on URLs found in Step 2, fetch the most valuable pages:

1. **Company website — MANDATORY DEEP CRAWL (2–3 levels, not just the homepage).** The website is where most of the real intel lives — and a homepage-only skim repeatedly misses the most decision-relevant facts (Peter, 2026-06-30). The discipline:
   - **a. Map the site first.** WebFetch the homepage AND ask it to return *every* nav link / page URL (about, products, **solutions/services**, capabilities, certifications, news/blog, careers, contact, sustainability, group/subsidiaries). Real sites hide detail under `/product-services/<x>`, `/solutions/<x>` sub-paths — find them.
   - **b. Drill EVERY solution/product/service page individually** — not the menu label, the actual page. For a multi-solution company, fetch each solution's own page. (PLIC burn 2026-06-30: I read the warehouse menu but not the pages — missed that their construction arm **builds factories**, and that their "WMS" is generic/not a real product. Both were on the site, 2 clicks deep.)
   - **c. Also crawl: /about (history, milestones, leadership names, JV/parent), /news (expansion, new plant, automation/ERP, awards, ESG = timing triggers), /contact (all phones/emails/branches), and any group/subsidiary pages (each legal entity).**
   - **d. Verify per page + quote verbatim.** Trace every claim to the page that said it; correct earlier assumptions against what the page actually states (Win Chance burn 2026-06-30: "OEM with Heinz client" was actually an **ex-Heinz JV + exclusive Heinz APAC co-packer** — only the /about page revealed it).
   - Extract: full product/solution catalog, certifications (ISO/IATF/GMP/BRC/HACCP…), factory/plant list & capacity, management/leadership names, group structure, partner/distributor brands, export markets, contact details.
   - **ALSO**: verify the correct registered company name (NutritionProfess lesson — website revealed the correct spelling when pipeline had it wrong).
2. **Facebook page** — WebFetch if found (often the BEST source for Thai SMEs)
   - Extract: recent posts, factory photos, product images, employee mentions, job listings
3. **ImportYeti page** — WebFetch if found
   - Extract: products shipped, US customers, shipment frequency, HS codes
   - **Interpret trade data**: China imports = BOI module need. Japan/Germany exports = traceability requirement. Seasonal spikes = APS opportunity (T100/Dinghua tier ONLY — iGP has NO APS; the iGP answer is LRP + 異常報表).
4. **News articles** — WebFetch the 1-2 most sales-relevant articles
   - Extract: expansion plans, financial data, leadership changes, partnerships

Deep-tier sections that a quick run does not produce get blockquote placeholders in the output: `> Deep module not run — rerun with --deep for ERP-incumbent sweep / group map / urgency timeline.`

## Step 3D: DEEP tier — parallel research fan-out

After Step 2/2.5 (DBD + warm base stay in the main loop), dispatch **4 parallel research agents in ONE message** (Agent tool, `model: sonnet` each — tier-disciplined per docs/model-tier-harness.md; log all dispatches to `docs/token-ledger.csv`). Every agent prompt carries a 4-part spec (outcome · quality bar · inputs · guardrails) and this fragment contract:

**Fragment contract (all agents):** write your full findings to `docs/research-fragments/<company-id>/d<N>-<topic>.md` (≤500 lines; every line source-attributable; the file starts with the INTERNAL banner). Return to the orchestrator only a ≤15-line summary: counts, headline findings, confidence. **The file MUST end with `STATUS: OK | PARTIAL | FAILED` plus the list of searches actually run.** A missing fragment file ≡ FAILED. On FAILED: orchestrator retries once; still failing → the corresponding dossier section carries a visible `MODULE FAILED (D<N>) — rerun --deep` banner and the matching gate FAILS (a crash is never recorded as "no signal"). **Cutoff: at 75 minutes total run time, ship PARTIAL with banners rather than looping.**

- **Agent D1 — ERP incumbent & IT footprint (evidence collection only).** **FIRST ACTION, before any
  press/vendor/LinkedIn sweep: find the company's OWN employer page on JobThai (`jobthai.com/th/company/<id>`,
  reachable via `WebSearch jobthai <company>`) and WebFetch EVERY live posting body verbatim — not search
  snippets ABOUT the company, the posting text ITSELF.** A job spec is the only public document the company
  writes about its own systems, and it must be accurate or the hire fails, so it names the incumbent when
  press, vendor case studies and LinkedIn all show nothing. (ALUMET 2026-08-05: D1 ran 30 searches and
  concluded "zero named systems"; the company's own Programmer Specialist posting said "พัฒนาและปรับปรุงระบบ
  **SAP Business One** โดยเน้นการใช้ Service Layer" — plus legacy Delphi/C#, SQL Server, MQTT/Modbus and an
  AI brief. A same-day Planning Manager posting handed over the operational pain in the company's own words:
  ~100 SKUs/day, 10+ changeovers/day.) Postings also reveal **intent**: an IoT/OT or AI hire alongside the
  ERP role means 自建情結 — they plan to build it themselves, which changes positioning from sell-to-gap to
  sell-the-standard-data-base. Then sweep: Thai job boards (JobThai/JobsDB + `สมัครงาน IT / เจ้าหน้าที่ ERP / ผู้ดูแลระบบ`), LinkedIn snippets, FB careers posts, website tech clues (careers pages, screenshots, news), SI/accounting-firm relationships (Thai SMEs often buy what their firm carries), and **active-evaluation signals** (`"[company]" ERP implementation / โครงการ ERP / go-live`, vendor case studies naming the company → record as row type `evaluation-in-progress`). Check every hit against the §15 name pack. **Every evidence line carries a DATE; evidence >24 months old → confidence auto-Low + generate a discovery question ("confirm current system — signal is stale").** Output fragment = candidate rows for `## Technology & Systems` (only named systems w/ evidence + confidence) + raw material for the verdict (see contract rule 3 — verdict itself is written by the orchestrator as prose in `## ERP Incumbent Read 【推論】`, **four states**: `displacement / greenfield / recently-purchased-or-implementing (→ complement play: eMES/WMS) / in-family TIPTOP (→ upgrade-expansion play)`).
- **Agent D2 — decision-maker & group map (raw evidence only; PASSIVE OSINT).** Per-director cross-holding searches (DBD/creden/dataforthai), shared-address hits, DBD related-companies listings, succession signals (2nd-gen roles on /about, news, FB), key-people public presence. **Guardrails: passive lookups only — no LINE adds, no FB follows, no connection requests; LinkedIn snippets only; family members recorded by ROLE relevance only ("2nd-gen Managing Director per /about"), never minors, never personal-life detail; every people-claim carries its public source URL.** The ORCHESTRATOR (top tier) builds the group tree + 守門員/決策者/核決者 hypothesis from the raw hits: a sister-entity claim requires **≥2 independent signals** (shared director AND shared address, or an explicit DBD related-companies listing); a single name match stays "possible, unverified". The role hypothesis NEVER lifts 三角色決策 above `inferred`.
- **Agent D3 — money & urgency.** Build the dated trigger timeline (see §16 taxonomy): new factory/land purchase, BOI approvals, expansion/hiring surges, IPO/แปรสภาพ, **System EOL** (write "System EOL — …", never "ERP" leading a cell), e-Tax/CBAM regulation, relocation — every item DATED + source-tagged. From the DBD ratios already extracted: draft 2–4 **pain-in-฿ candidates as validating QUESTIONS** (Nova pain-translation form) with explicit-assumption RANGES — "IF inventory error is even 1% of COGS → ฿X–Y/yr — worth checking?" — each figure names its assumption; never a declarative loss claim. KSF3 output = arithmetic flag (`pain candidate clears / does not clear ฿1M THB`), never a score. Plus a 3-line **budget-capacity read** 【推論 from DBD】 (capital events, equity/cash one-liner, tier-affordability hypothesis).
- **Agent D4 — website deep crawl.** Same Gate-#8 discipline as Step 3 (map → drill every page → verify + quote verbatim, ≤10 verbatim lines per page), written to the fragment file.
- **Agent D5 — community & sentiment sweep (added 2026-07-18 per Peter).** The Thai-local voice: Pantip/forum threads, Facebook page + public group mentions, Google Maps reviews (agent tries search-snippet + proxy routes; if blocked, the ORCHESTRATOR pulls Maps via main-loop Playwright and appends to the fragment), employer reviews (JobsDB/JobThai/งานดีมั้ย), TikTok/YouTube mentions, LINE OA presence, and the Thai negative-news pack (ฟ้อง/คดี/โกง/ค้างจ่าย/ประท้วง/ไฟไหม้/เลิกจ้าง/แรงงาน). Fragment: `d5-community-sentiment.md`. Everything tagged **【公開-社群】= sentiment-grade, never fact-grade** — quote verbatim with URL + date, phrase claims as "reviewers allege/say", separate B2C consumer voice from B2B service chatter from employee voice. Guardrails: PASSIVE only — no login/posting/joining/contacting, no minors or private-person detail; defamatory material never leaves internal fences. Absence is a finding ("no local footprint" ≈ B2B-only or below-radar — say which).

**Synthesis (orchestrator, top tier):** read fragments ONE FILE AT A TIME; contradiction-check every fragment claim against DBD; merge into the dossier per the OUTPUT CONTRACT; **then run the SELF-CONSISTENCY PASS before the gates.**

> **SELF-CONSISTENCY PASS (added 2026-08-31 — the Bosch head/tail burn).** Merging is not synthesis.
> Re-read the dossier END TO END and reconcile every section written BEFORE the arms ran against
> what the arms actually found. The gates cannot catch this: they check structure, not agreement.
> Bosch was promoted and ingested carrying "Financials PENDING", "Fit LOW-MEDIUM", "Stage E" and
> "no named local contact exists" in its tail, while its head carried the adjudicated opposite in
> all four. Sections most likely to be stale: Phase C/D · Phase E · Technology & Systems · Key
> People · Fit Assessment · 六要素 · Reflection Summary · the Phase A search log. If a fragment
> overturned a premise, say so explicitly and date it — a superseded conclusion left standing reads
> as a live one to whoever opens the file next month. Enforced (partially) by `osint_redlines.py`
> red line 2; the rest is your read.

Then gates. Fragment retention: after the dossier passes gates, delete fragments or archive to `docs/_eval/archive/<company-id>/`. A hypothesis that failed the ≥2-signal test survives ONLY as the dossier's explicit "possible, unverified" line — never as a loose fragment.

## Step 4: Self-Reflection

**CRITICAL: Do not skip this step. This is what separates good research from lazy research.**

Before generating the briefing, pause and systematically check your work:

### Coverage Check
For each category, write what you found or "NOT FOUND":
- **DBD DataWarehouse data (CRITICAL)**: Tax ID, registration date, capital, directors, status, TSIC code, business size: ___
- **DBD Financial data (CRITICAL)**: 5-year revenue, profit, assets, debt, inventory, equity: ___
- Company basics (name EN/TH, founding year, address, website): ___
- What they manufacture (products, processes): ___
- Factory locations and size: ___
- Employee count or estimate: ___
- Current ERP/IT systems: ___
- Key people beyond DBD directors (managers, titles, roles): ___
- BOI promotion status: ___
- Recent news (last 12 months): ___
- Ownership type (Thai family / 台商 / Japanese JV / MNC): ___
- Supply chain (customers, suppliers, export markets): ___
- Certifications (ISO, IATF, GMP): ___
- Related companies (from DBD search results): ___

**If DBD data is missing, this is a CRITICAL gap. Try harder before proceeding.**

### Anomaly Check
- Is this entity an **SPV/holding company**? (zero revenue + zero inventory + zero PP&E)
- Is this a **converted entity**? (Ltd → Plc., check for old entity historical data)
- Is this a **greenfield factory**? (new registration, pre-revenue, large PP&E build)
- Is this company **actually a manufacturer**? (many pipeline companies are wholesale/trading despite assumptions)
- Does the **industry match expectations**? (Junma was assumed food but was actually tire cord; Xingjia was assumed bio but may be steel)

### Gap Filling
For EACH category marked "NOT FOUND" or weak:
1. Think: what specific search query could fill this gap?
2. Run that additional search NOW.
3. If still not found after the additional search, mark as "Unknown — Discovery Priority for meeting."
4. Do NOT mark something as "Unknown" without trying at least one additional targeted search.

### Contradiction Check
- Compare data across sources. Do any conflict?
  (e.g., website says 500 employees but LinkedIn snippet says 50)
- If contradictions exist: note both values, flag the lower-confidence source, explain the discrepancy.
- **Revenue estimates from non-DBD sources (ExportHub, Growjo, etc.) are often wildly wrong** — BFC showed $5-10M on ExportHub but actual DBD revenue was $58M (2.05B THB). ALWAYS trust DBD over third-party estimates.

### Evidence Audit
- Every claim MUST have a source (URL or search query that found it) — tag lines 【DBD】/【公開】/【推論】/【電話】/【DB】.
- Any "facts" that are actually your assumptions? Downgrade confidence to "Estimated" and tag 【推論】.
- Every 【推論】 in a sales section must NAME the facts it derives from.
- Ownership type MUST cite director names or parent company evidence — never guess without evidence.

### Completeness Score
Count how many of the 12 categories have data: X/12.
If below 6/12: you likely need more searches. Try harder before proceeding.

## Step 5: Generate Briefing

**NOVA calibration + LIVE consultation + gap capture (both tiers):** before writing the sales sections, read `nova-knowledge.md` and apply its priors (wedge choice, incumbent hypothesis, ROI ranges, qualification gates/red flags, trigger weights, authority playbook) — always inside internal fences, always tagged. **Then, whenever an inference cannot be grounded in either run evidence or the cached KB, ASK THE LIVE NOVA AGENT (do not guess, do not merely queue).** Follow `nova-live-consultation.md`: open the Playwright/Teams driver, `+ 新對話` in 南高-商機助手, send a self-contained question (ASCII hyphen only — em-dash triggers the WAF 403), capture the answer verbatim via the job API to `docs/research-fragments/<company-id>/nova-live-<date>.md`, tag reliance 【NOVA live <date>】 inside internal fences. Bias toward asking: Peter's rule is "ask whenever, ask where you need to, so you are undoubtedly confident." Encode durable, generalizable answers back into `nova-knowledge.md` (new §N). If the live agent is unreachable, fall back: append the GENERALIZED question to `docs/nova-queue.md` and note it. Footer line: `NOVA live consulted: N (<topics>) · KB updated: §N|none · queued: N`.

Output the briefing using the template in `briefing-template.md` (A operating / B greenfield / C SPV-unresolved). Distributor/SI/co-sell candidates → **`/research-partner`** (Template D retired 2026-07-17).

**`## 60-SECOND PRE-CALL READ` — mandatory, both tiers, directly under the two header banners.** Rendered entirely as a blockquote INSIDE an INTERNAL fence, ≤12 lines, in the 痛→錢→急→Fit→決策 order:
1. 痛 — sharpest pain hypothesis + its evidence
2. 錢 — money read (size + affordability one-liner)
3. 急 — #1 dated urgency trigger
4. Fit — incumbent verdict one-liner + product-fit hint (facts only — the full T100-vs-iGP call stays with `/select-t100-vs-workflow`)
5. 決策 — who decides + AUTHORITY CHECK result
Then the top-3 discovery questions. **Partner-looking targets do NOT get a sell-to read — hand off to `/research-partner`** (Step 1.5 detector; 通路案 ≠ sell-to).

**INTERNAL fence convention:** the fence is the exact blockquote line `> INTERNAL ONLY — never into customer-facing artifacts` opening the block (content indented as blockquote below it). **Exactly SIX fenced blocks** in a deep dossier: ① 60-second read ② ERP Incumbent Read ③ decision-map hypothesis ④ pain-in-฿ ⑤ budget-capacity read ⑥ warm base. (Deck skills skip fenced blocks when synthesizing OSINT.)

Key rules:
- Every field must show its source and confidence level
- Decision roles are always INFERRED (confidence: Low) — never claim certainty from OSINT. **AUTHORITY CHECK (mandatory, in prose-only Key People):** for every named contact — `AUTHORITY CHECK: <name> — on / NOT on DBD director list; signatory = <X>; stage cap C2 until the signatory engages.` (TN Advance burn: the "decision maker" wasn't the legal signatory.)
- Talking points must be SPECIFIC and evidence-backed — never generic
- Discovery Priorities come BEFORE Talking Points (know what to ASK before what to SAY)
- The Reflection Summary must be included — it shows Peter how thorough the research was

### 六要素 Status table — canonical set (single source of truth)
Seven rows, with FROZEN element_key strings (they match the DB reader's FIELD() order — never change them):

| Label | element_key |
|---|---|
| 上線時程 | `timeline` |
| 分段預算 | `budget` |
| 痛點需求 | `requirements` |
| 三角色決策 | `decision_roles` |
| 競爭態勢 | `competition` |
| 動機 L1 | `motivation_l1` |
| 動機 L2 | `motivation_l2` |

OSINT structurally fills ≤4/7; the rest are marked `needs meeting` — never fabricated. (The old MEDDIC-style 6-row variant is dead — do not use it.)

### Disqualification Check
Disqualification should have been caught at the Early Disqualification Gate in Step 2. If a company reaches Step 5 and shows disqualification signals missed earlier (e.g., < 30 employees discovered during enrichment), flag it now.

### Stage Recommendation (OSINT vs Pipeline)
Two separate fields — do NOT confuse them:
- **OSINT Recommended Stage**: What OSINT evidence supports. Only two options:
  - **E** = fits target profile, no pain indicators found
  - **C2-candidate** = concrete pain indicators found (Digiwin sees latent need the customer may not recognize)
- **Actual Pipeline Stage**: If the company is already in Peter's pipeline (check Obsidian/Google Sheet), note the current stage separately. A company can be at pipeline stage D while OSINT recommends C2-candidate.

**Never** recommend D or higher from OSINT alone — D requires actual customer contact.

### Pain-to-Digiwin Product Mapping
Use the authoritative mapping table in `extraction-schema.md` (Section 13). Apply it to THIS company's specific evidence — never copy the generic table into the output. Remember: **APS rows are T100/Dinghua tier ONLY** (iGP = LRP + 異常報表, 嚴禁自動排產); worker-level/per-piece actuals = **eMES Phase 2** (never SFC/SFT).

### Ownership Type Detection
Use director names and company structure as evidence:
- Thai surnames (สมชาย, พิสุทธิ์) → Thai-owned. Pitch: respect hierarchy, find real 核決者
- Chinese surnames (張, 李, 王, 陳) → likely 台商 or 陸商. Pitch: Mandarin, reference Taiwan HQ
- Japanese names (田中, 鈴木) → Japanese JV. Pitch: quality/traceability emphasis
- Western names or multinational parent → MNC subsidiary. Pitch: cost vs global suites
- **American-registered but Chinese directors** → US holding company for Chinese group (Zhongli pattern). Pitch: Mandarin + international standards

### Competitive Landscape
The most common "competitor" for Thai SMEs is NOT a global suite — it's **Excel / paper / no system at all.**
- If incumbent system found → four-state verdict (see D1): displacement / greenfield / recently-purchased (complement play) / in-family TIPTOP (upgrade play)
- If **Odoo** → common among small Chinese-owned companies. Pitch: manufacturing depth (BOM/costing)
- Always check active evaluation: news, "ERP implementation" job posts, vendor case studies (Epicor is hunting in our exact segment — TN Advance 6/29)

## Step 6: QA Checklist (MANDATORY — do NOT skip)

**Run QA on the DRAFT (in `docs/_eval/`) BEFORE promoting.** Every gold standard MUST pass before it reaches `docs/`. Batch processing is NO excuse for quality drops.

### Mechanical check (REQUIRED — run both commands)
```bash
python3 ~/.claude/skills/digiwin-research-company/scripts/check_contract.py docs/_eval/gold-standard-<id>.md.draft [--deep]
python3 database/ingest_md_to_db.py --file "$(pwd)/docs/_eval/gold-standard-<id>.md.draft"
```
The dry-run prints one line per entity in this format (quote for assertions):
```
gold-standard-x.md.draft   0105512345678 [NEW   ] dir= 3 cert= 2 exp= 1 tech= 1 src= 8 own=TH pd=Y
```
**Gate #13 asserts:** exactly ONE output line with no `»` label (= 1 entity, no split) · `dir=`≥1 OR check_contract verified `Directors: PENDING` · `tech=` equals the count of confirmed rows exactly (0 when no-signal blockquote) · `src=`≥5 · `skipped 0 files`. MySQL down → Gate #13 INCONCLUSIVE → do NOT promote.

### Section Completeness Check
Verify the output contains ALL of these sections (mark ✅ or ❌):

- [ ] **Header banners**: tier line + INTERNAL WORKING DOSSIER line
- [ ] **60-SECOND PRE-CALL READ** (fenced, ≤12 lines, 痛→錢→急→Fit→決策; Template-D: 8-dim partner read)
- [ ] **Phase A**: Search results table (what was searched, what was found)
- [ ] **Phase B**: Company profile table (legal name, Tax ID, registration date, capital, TSIC, address, business group, size)
- [ ] **Directors**: table first-in-section + labelled `Signing authority:` line
- [ ] **Ownership Analysis**: Nationality breakdown with evidence (director names)
- [ ] **Phase C**: Balance sheet (all available years)
- [ ] **Phase D**: Income statement (all available years)
- [ ] **Phase E**: Financial Trend Analysis (ratios + written trends + company-specific pain→product per §13)
- [ ] **Technology & Systems** (one table, confirmed rows only) + **ERP Incumbent Read 【推論】** (deep)
- [ ] **Group Structure & Decision Map** (deep; members as rows) + **Urgency Signals & Timing Triggers** (deep; Date-first columns)
- [ ] **Warm Base & Nearby References** (fenced) or DB-unavailable line
- [ ] **Key People — prose only** with AUTHORITY CHECK line(s)
- [ ] **Fit Assessment table** + "Why [SCORE]" reasoning
- [ ] **Key Sales Angles** (3-5, evidence-backed) · **Discovery Priorities** (3-5)
- [ ] **六要素 Status table** (canonical 7 rows, frozen keys)
- [ ] **Reflection Summary** (all 6 subfields) · **Sources table** (with sub-page URLs — Gate #8)

### Hard-Fail Quality Gates (FAIL if ANY true)
1. ❌ No Fit Assessment table → FAIL (even "PENDING" is better than blank)
2. ❌ Generic pain→product mapping (same text as 5+ other files) → REWRITE with company-specific evidence
3. ❌ No Discovery Priorities section → FAIL (minimum 3 questions for operating companies)
4. ❌ No Key Sales Angles → FAIL (minimum 3 evidence-backed talking points)
5. ❌ Fit score contradicts evidence → REVISE
6. ❌ No Reflection Summary (all 6 subfields) → FAIL
7. ❌ BOI status not searched → FAIL
8. ❌ Website not deep-crawled when one exists → FAIL (sub-page URLs in Sources; Win Chance + PLIC burns)
9. ❌ **ERP-incumbent search not evidenced** → FAIL. Technology section must show ≥1 evidenced row OR the blockquote "No signal found after job-post + website + news sweep". Deep tier: D1 fragment STATUS must be OK (FAILED ≠ no-signal).
10. ❌ **AUTHORITY CHECK line missing** from Key People → FAIL.
11. ❌ (deep) **Urgency timeline missing/undated/untagged** → FAIL. Every row `Date | Trigger | Evidence | Source` with a year + 【tag】; ≥3 triggers or explicit "no timing trigger found". D3 STATUS OK required.
12. ❌ **Source-tag audit**: any row of the two NEW tables untagged, or a 【推論】 that doesn't name its source facts (spot-check 5 claims elsewhere) → FAIL.
13. ❌ **Ingest dry-run contract** (above) not green → FAIL / INCONCLUSIVE (MySQL down) → no promote.
14. ❌ **INTERNAL fences ≠ 6** on a deep dossier (① 60s read ② incumbent read ③ decision map ④ pain-in-฿ ⑤ budget capacity ⑥ warm base) → FAIL.

### Special Cases
- **DISQUALIFIED companies**: Still need Fit Assessment table with clear "DISQUALIFIED" + reason. Must be scannable within 5 seconds. Discovery Priorities and Sales Angles are N/A.
- **NOT FOUND companies**: Need "UNRESOLVABLE" label + specific action items for Peter (Tax ID, Thai name, name card)
- **AMBIGUOUS companies**: Need "AMBIGUOUS — NEEDS DISAMBIGUATION" + what Peter needs to provide
- **SPV/Holding entities**: Need WARNING banner at top + action items to find real operating entity
- **Unconfirmed identity**: Need WARNING banner with confidence level + verification steps
- **Greenfield (pre-revenue)**: Use Greenfield template (B) from briefing-template.md
- **Partner/channel candidates**: hand off to `/research-partner` (Template D retired)

## Step 7: Gate-Then-Atomic-Promote

**Never write a glob-matching filename before gates pass** (the nightly launchd job auto-commits every `docs/gold-standard-*.md` to MySQL at 02:00, gated or not).

1. Draft lives at `docs/_eval/gold-standard-<id>.md.draft` throughout Steps 5–6.
2. All gates green → if `docs/gold-standard-<id>.md` already exists, back it up to `docs/_eval/archive/gold-standard-<id>-<date>.md.bkp` (NEVER a glob-matching name).
3. `mv docs/_eval/gold-standard-<id>.md.draft docs/gold-standard-<id>.md`
4. Clean/archive fragments (deep tier).
5. Print the footer next-actions block:
```
NEXT ACTIONS
1. Ingest (dry-run first):  python3 database/ingest_md_to_db.py            # review counts
2. Commit:                  python3 database/ingest_md_to_db.py --commit
3. Sheet sync:              python3 database/sync_osint_to_sheet.py
4. Financials (versioned):  python3 database/refresh_financials_from_dbd.py --taxid <id> --headed
5. (deep) Forwardable Nova packet? → say "nova packet for <company>"
```

## Step 7.5: Post-Meeting Reconciliation (`--reconcile` — added 2026-08-11, Peter's "shrink the gap")

**The dossier must LEARN from every meeting, or it silently rots on exactly the facts that matter most.**
(Proven on Asia Poly Sacks: the dossier carried "AX scope unresolved, likely displacement, CFO-first" for
18 days AFTER the MD had personally resolved it on a call — "I use AX, leave ERP to one side" — because
nothing flowed back. The deck, the DB, and the Sheet all read the stale hypothesis.)

**Trigger:** a graded FPM transcript, a Peter-relayed call/meeting summary, or field intel exists for a
company that already has a promoted gold standard. Run within 48h of the meeting. Invocation:
`/digiwin-research-company <company> --reconcile` (or Peter says "reconcile <company>").

**Scope — update ONLY what the meeting evidenced, tag everything 【電話/會議 <date>】:**
1. **Technology & Systems** — confirm/upgrade incumbent rows (confidence + scope) from the customer's own words.
2. **ERP Incumbent Read** — re-issue the 4-state verdict if the meeting moved it (e.g. likely-displacement →
   confirmed-complement); prior analysis is PRESERVED and re-labeled (e.g. "Phase-2 thesis"), never deleted.
3. **六要素 table** — upgrade statuses (inferred → stated/confirmed) row by row; each upgrade cites the meeting.
4. **Key People / decision channel** — confirmed roles, contact-channel facts (e.g. WhatsApp-only), name gotchas.
5. **Discovery Priorities** — mark ANSWERED items (keep them, labeled, at the bottom); promote the next
   evidence asks to the top.
6. **Key Sales Angles + 60-second read** — resequence to the post-meeting play.
**NEVER touch:** DBD-owned data (capital/TSIC/financials — the DBD refresh owns those), the original OSINT
evidence trail, or anything the meeting did not actually evidence.

**NOVA rule:** any STRATEGY flip implied by the meeting (entry play, stage grading, wedge) goes to the LIVE
NOVA agent before it is written — the meeting supplies facts; NOVA rules on the play. Tag 【NOVA live <date>】,
capture verbatim to `docs/research-fragments/<id>/nova-live-<date>.md`.

**Gates are NOT waived:** edit a draft copy in `docs/_eval/`, run `check_contract.py --deep` + the ingest
dry-run (Gate #13 assertions), then backup-and-atomic-promote (Step 7) → `ingest --commit` → `sync_osint_to_sheet.py`.
Append a dated **Reconciliation** paragraph to the Reflection Summary (what moved, which meeting, which NOVA job).

Worked example: `docs/gold-standard-asia-poly-sacks.md` reconciliation of 2026-08-11 (call 2026-07-24 +
NOVA job 66a5b3a4: C2→C1 regrade, CFO-first retired, Trojan-horse escalation script).

## Step 8: Batch Processing Protocol

**BATCH-MODE CONTRACT (MANDATORY — read `batch-mode.md` in this skill's directory before ANY multi-company or unattended/overnight run).** The 5 invariants, in one line each: ① batch never changes the per-company protocol — `--deep` always means full D1→D2→D3→D4→D5 + fresh NOVA, no compressed/combined agents; ② agents strictly sequential, one alive at a time (Peter's standing rule); ③ depth beats coverage — fewer companies at full depth, never all at reduced depth (queue the rest, list the queue in the report); ④ <25 min/company = defect signal, stop and audit; ⑤ report per-company wall-clock + dispatch mode + any deviation proactively. **Before promoting each company: `python3 ~/.claude/skills/digiwin-research-company/scripts/batch_depth_gate.py <company-id>`** (asserts 4 fragments with STATUS + search logs, sequential mtimes, NOVA capture) — depth-gate FAIL = no promote. Origin: the 2026-07-17 overnight compression burn (all 5 upgraded dossiers had missed decision-changing facts).

When processing multiple companies in a session:

### Ordering Priority
Research companies in this order:
1. **Pipeline D-stage companies** (already have contact — research is urgent for next meeting)
2. **Expected HIGH-fit** (Chinese/Japanese manufacturers near industrial estates, >50M capital)
3. **Clear name/identity** (easy to find on DBD — quick wins)
4. **Ambiguous/unclear** (may need Peter's input — save for end)

### Session Limits
- **Recommended batch size**: 3-5 companies per session (quick tier); deep tier is ONE company per run
- **Quality tracking**: After each company, note elapsed time and quality score. If quality drops (missing sections, thinner analysis), STOP and finish remaining companies in next session
- **DBD rate limiting**: If DBD returns 429/529 errors, wait 5 minutes between searches. If persistent, switch to Creden/DataForThai for remaining companies
- **Playwright session**: Restart the browser every 3 companies to avoid stale sessions

### Quality Rule
- Each company MUST independently pass the QA checklist (Step 6)
- Quality of company N must equal quality of company 1 — no degradation allowed
- If DBD data is unavailable (529 error, site bugs), note it explicitly and use fallback sources
- If a file cannot pass QA due to missing data, mark it as "INCOMPLETE — needs retry" with specific gaps listed
