# NOVA Knowledge Base — DigiWin institutional priors for Thai-market research

> Source of truth: DigiWin's internal NOVA agent (Teams › 鼎新數智 › 諾瓦Nova › 業務大學姐 › 南高-商機助手), elicitation thread "SKILL KNOWLEDGE BASE #1", 2026-07-10. Raw verbatim captures: `docs/research-fragments/_nova-kb/`. Every entry below is NOVA-sourced unless marked otherwise; tag dossier lines that lean on this file 【推論 calibrated by NOVA KB 2026-07-10】 and keep them INSIDE internal fences (never customer-facing).
> Status: Q1–Q17 fully captured (verbatim in `docs/research-fragments/_nova-kb/`) · **V1.0 formally signed off by NOVA 2026-07-13 (Q13–Q17 examiner loop: 「已足夠，准予正式定版發布」)** · new gaps accumulate in `docs/nova-queue.md`.
> Discipline: these are PRIORS, not facts about any specific company — they sharpen hypotheses and deal structure; they never substitute for evidence. Backtest note: Q4 gates are consistent with the TN-Advance loss profile (mid-size, active Epicor eval) and the EDH win (small, phased entry); no contradiction found yet.

## 1. Entry wedge by structure (Q1)

For Thai family SME groups shaped as **trading company + own/affiliated factory** (the dominant pattern):
- **Wedge = ERP first** (核心進銷存 + AR/AP + 基礎生產申報), specifically "貿易與工廠財務/進銷存數據一體化". The killer pain is 資訊斷層: front-line order desk disconnected from factory → wrong stock, slow delivery answers, "算不出真實利潤/成本".
- **Do NOT lead with MES or WMS** — premature before the ERP base is stable ("基礎不穩反而容易失敗").
- **3-year expand path**: Y1 ERP (治亂: stock ledger + AR/AP accurate, basic financials) → Y2 BPM e-approval + lightweight barcode WMS (控料: kills 人治 approvals; FIFO/counting for heavy materials) → Y3 MES (控產: shop-floor reporting, work-hours, mold management — only after ERP stock+BOM stable).
- **Reference case (usable)**: Thai steel/building-materials firm, 2nd-gen successor, revenue ~฿150M, ex-**Express** ("great for accounting, can't manage the factory") → DigiWin ERP (order↔stock link, auto-deduct on shipment) → +2yrs WMS with PDA scanning → stock accuracy 95%+, counting time −50%.

## 2. Incumbent base rates + first-call diagnosis (Q2)

Office stack, by frequency (Thai family manufacturers ฿50–500M revenue):
1. **Excel + paper + outsourced bookkeeping** — highest probability, especially <฿100M revenue
2. **Express** — most common Thai accounting package; standalone/LAN, NO production module
3. **WINSpeed / Formula** — mid-tier local ERP, fuller but aging C/S architecture
4. **SAP B1** — only near ฿300–500M with 2nd-gen or export needs

Shop floor, by frequency: paper + whiteboard (**>80%, the absolute mainstream**) → Excel scheduling by 生管 → small local custom/Access systems (maintenance-orphaned).

**First-call 1-minute diagnosis — never ask "what system do you use"; probe 作業場景:**
1. (office) "Monthly tax filing & financials — does your own accountant pull them from a system, or do you package data for an outsourced accounting firm?" → outsourced = paper/Excel/simple Express; in-house = follow up "Express or WINSpeed?"
2. (factory) "Does 生管 schedule production in Excel or does a system generate it? Is floor progress paper-logged or on screens?" → SME custom/legacy = always paper + re-keyed Excel
3. (owner/2nd-gen) "When traveling, can you see today's shipments & stock on your phone, or does someone photograph an Excel for you?" → photo-of-Excel = no real-time integration

**Per-incumbent entry strategy:**
| Incumbent | 痛點翻譯 (owner language) | Play |
|---|---|---|
| Excel+paper+outsourced | 帳實不符 → cash tied up, tax risk, can't price accurately | ERP: "one-click financials + 進銷存合一"; anti-fraud, reclaim family control |
| Express / WINSpeed | information islands; office↔floor disconnect; slow delivery answers | "the upgrade that manages the FACTORY" — BOM/materials/progress Express can't do |
| Local custom (orphaned) | 系統孤兒: developer gone, business-stop risk, can't scale | brand + permanence: listed APAC vendor, Thai team, standardized, succession-safe |

## 3. ROI benchmarks — conservative / typical / best (Q3)

ERP (revenue ฿50–500M band; SEA/TW implementation cases):
| KPI | Conservative | Typical | Best | Citable? |
|---|---|---|---|---|
| Stock accuracy | +10% | **+20–30%** | +50% | YES — kills "幽靈庫存" |
| Inventory days | −5% | **−15–25%** | −40% | YES — frees ฿1–5M working capital |
| DSO | −3–5 d | **−7–10 d** | −15 d+ | YES — cashflow/bad-debt control |
| Monthly close | −3 d | **−5–10 d** | −15 d | YES — "close by the 10th not the 20th" |
| Manual re-keying hours | −15% | **−30–40%** | −60% | INTERNAL ONLY |

WMS (own factory, multi-warehouse, heavy materials): counting time −20% / **−40–50%** / −70% (citable; "2 days → half a day, no stoppage") · picking/issue errors −30% / **−60–80%** / −95% (citable; barcode/QR kills rework) · locate/search time −25% / **−50%** / −80% (citable).
MES (metal fab/die-cast/stamping/assembly): full table in raw capture `q3-roi-benchmarks-raw.md`.
Rule: quote ranges as "DigiWin customers typically see…", never promise a specific company's number; internal-only rows never leave the fence. Origin caveat: only ~30–40% of these benchmarks are Thai-local — see §11 for the honest-origin script and citable Thai cases before pitching any figure as "Thai".

## 4. Qualification gates + financial red flags (Q4)

**iGP/Workflow tier**: Go = revenue ฿100–300M · 50–150 staff · registered capital ≥฿20M · single factory, standard BOM, messy stock, manual scheduling. Caution = ฿50–100M · 30–50 staff · capital ฿5–20M · trading+light outsourced mfg. No-Go = <฿50M · <30 staff · capital <฿5M · pure trading, no BOM.
**T100 tier**: Go = revenue ≥฿500M · ≥200 staff · capital ≥฿50M · group structure/multi-factory/BOI cross-border/bonded. Caution = ฿300–500M · 120–200. No-Go = <฿300M or <120 staff (no IT/PM capacity).

**Red-flag formulas (from 3-yr DBD pull — predict lost deals / stalled projects / bad debt):**
1. Net margin **< 1.5%** → payment installments get dragged
2. D/E **> 2.5×** → survival risk under market swings
3. DSO **> 120 days** → weak chain position, budget gets raided mid-project. ⚠️ Exception: construction-adjacent traders (building materials/steel structure) — 300–400d can be normal progress-billing + retention structure, NOT distress; read via §12 before red-flagging
4. Revenue decline **> 20% for 2 consecutive years** → ERP-as-last-gasp; project decapitates on layoffs
5. Registered capital **< 30% of total quote** → shareholders won't stand behind disputes

**Small-but-strategic combo** (No-Go-edge size but flagship value): SaaS/subscription iGP (−50%+ entry cost, no server/SQL) OR **BPM-first** (e-approval quick-win, 2–4 wk deploy, lowest complaint rate) OR **barcode-WMS lite** (stock+counting only; solves "倉庫找不到貨" with minimal people).

**Caution**: DBD revenue is often UNDER-reported (外包記帳 / 多套帳 tax practice) — cross-check physical factory scale (machines, truck traffic) before concluding a company is too small.

## 5. Timing-trigger conversion ranking (Q5 — key findings; full text pending re-capture)

- **Fastest converters in Thailand: e-Tax/compliance mandates and 二代接班 (2nd-gen succession)** — on either signal, launch 初訪流程 immediately and run 五要素補問 for the core intent.
- e-Tax/法規 → treat as C1-adjacent (顯性): ask who owns the compliance deadline; lock the CFO/管理層 with an "e-Tax 導入檢核表".
- 二代接班 → C2 (隱性): is the heir in a core role with budget latitude? Translate their "管理混亂" complaints into profit-leak/asset-risk reporting for the parents.
- 新建廠/搬廠 → C2→C1: where in the build is IT budgeted? Enter at the land/construction phase and lock software into the capex envelope.
- **Classic false positives**: revenue decline alone (no budget → wasted cycles) and hiring waves alone (may be replacement, not expansion) — corroborate before investing visits.

## 6. Family-firm authority playbook (Q6 — key findings; full text pending re-capture)

When the heir runs operations but parents hold DBD signing power: work BOTH, never bypass — 拉一派、打一派、安撫一派 is wrong framing; correct = **賦能** each layer:
- To entrenched elders/relatives holding purchasing/warehouse: sell "省力、免責、功勞" — the system scrubs suspicion off THEM and cuts their drudge work ("這些雜事交給電腦，您專注在協助董事長把採購決策和把關品質").
- To the 2nd-gen: transparent data as compliance/management tooling, standardized 數據輸入 while PRESERVING elders' approval rights (多關簽核、權限控管) — replace 人治 with process without a face-off.
- Stage discipline: if the signatory (一代) posture/budget latitude is unknown → drop back to C2 and re-probe; invite the 一代 into the visit at step 5–6 of 初訪七步驟 (探詢企圖/賦能窗口) to complete the decision chain early.

## 7. Multi-entity group: customer definition, quoting, iGP↔T100 boundary (Q7)

For trading-co + affiliated-factory + sister-co groups (dominant Thai 華人 tax/risk structure):
- **Customer = the entity with real financial/operational control (family holding)**, but **contract主簽方 = the invoicing/highest-revenue/cash-rich legal entity (usually the trading co)**. Never sign with a shell or loss-heavy sister (bad-debt risk).
- **Packaging**: preferred = ONE master contract (trading co) + named multi-entity licence scope. Tax-driven alternative: split software licences per entity, but keep implementation service in ONE contract (trading co or biggest factory) to avoid fragmenting the project.
- **iGP/Workflow capability edges**: multi-company via separate books (switch to change company); intercompany = manual/batch document transfer (NOT suited to frequent triangular trade); **no built-in consolidation** (Excel merge).
- **T100 golden thresholds (any one)**: intercompany docs **>30% of total documents** · frequent cross-entity/cross-border transfers & subcontracting · owner demands **automated group consolidation within 3–5 days of close**.
- **Sequence: trading entity FIRST, factory second** — faster (3–4 mo), standard flows, quick owner-visible wins (stock + AR clean), and sales orders are the clean demand source for later MPS/MRP. Exception: factory-first/parallel if the dominant pain is delivery delays/scrap AND a strong 2nd-gen/professional manager owns the plant.
- **Polite ownership probes** (never ask "do you own the factory?"): (a) tax/invoice angle — "trade→factory: internal transfer or VAT invoice?" (b) material-ownership angle — "客供料 or buy-and-sell-back?" Interpretation: VAT+buyout = treat as intercompany/subcontract flows; no-invoice transfer = economically one unit → model as multi-site/multi-warehouse regardless of shareholding.
- Deal risks: 防範隱形客製化 (profit-shifting transactions — steer to standard intercompany flows, refuse deep customs); target the CFO/senior accountant early (multi-entity pain lands on consolidation + tax compliance).

## 8. C2-candidate vs E — minimum evidence bar (Q8 — key findings; scoring-sheet table pending recapture)

- Pre-visit: score the target's DBD financials on NOVA's qualification sheet; **<6 points → position visit as 純關係建立與輪廓摸底, promise no Demo, no benefit estimates**.
- Conversion probes: listen for resonance on 結帳天數 / 人工重複登打 / 產能答交率 — on any vented complaint, log the 感性痛點 and prepare 痛點翻譯 with a quantified hypothesis for management.
- **False-C2 rule**: a new factory/land purchase alone NEVER justifies B or C1. Until 「非做不可的量化理由」 AND 「指派專案小組」 are confirmed, hold at C2 — else 業務一頭熱 idle-spin. (Matches the /digiwin-research-company rule: OSINT recommends at most C2-candidate.)

## 9. Objection library — Thai family SME, 9 objections (Q9)

Frame for ALL objections: 同理接納 → 視角轉換 (risk/opportunity) → 強力反問 — translate emotional refusal into owner P&L language. Full verbatim 話術 in `q9-objection-library-raw.md`; the 9:
1. **低毛利期不敢投資** (the big one): low-margin times are exactly when 不浪費 wins — do you know which products are NEGATIVE margin right now? If inventory days −10 released the cash, doesn't that fund the system?
2. **太貴 (vs Thai local)**: cheap ERP = cheap truck that breaks; you're buying assurance of go-live + correct costing, not software. "Cheap vendor or operations partner who cuts 5% production loss?"
3. **沒人力配合**: staff are busy BECAUSE 70% of time is re-keying/reconciling — the system diets their workload; will they get free by themselves as business grows?
4. **怕老員工抵制**: 抓大放小 staged rollout, Thai SOPs, seed users; counter-ask: what does staying paper-based do to competitiveness & 2nd-gen succession appeal?
5. **外包會計就夠了**: outsourced accounting = last month's autopsy; ERP = today's control (stock-outs, line stoppage, pricing floor). Can last month's report undo this month's scrap?
6. **自己人寫的系統還能用**: orphan-system risk — sole developer leaves, e-Tax/multi-entity needs arrive; who maintains it tomorrow?
7. **等新廠建好再說**: practice the processes in the OLD plant, carry mature digital flows into the new one — double-adaptation chaos stalls new-plant ramp for months otherwise.
8. **台灣/中國品牌疑慮**: Digiwin Software Thailand = local entity, Thai consultants, e-Tax compliant; offer Thai reference-site visits.
9. (Stage mapping table in raw file: 景氣/毛利 objection ⇒ C2→C1 conversion driver; 成本 objection ⇒ B-stage.)

## 10. Competitive plays per product line (Q10)

**ERP vs Epicor** (mid-market hunter, TN-Advance killer): recognition = customer talks Multi-site sync/SaaS/UD-Field flexibility, or asks about APAC-wide support. Play: 原廠在地直營 (Thai+Chinese consultants, no agency churn) vs expensive partner consultants; "best-practice套裝" vs "unlimited flexibility = your old bad habits imported + budget blowout". Comeback pattern: go to the **CFO** with e-Tax auto-reconciliation + one-click work-order actual costing (Epicor needs custom work for both). Loss lesson: never fight on IT specs/cloud flexibility — you lose to the international-brand halo; fight on time-to-standardized-costing.
**ERP vs Express upgrade**: recognition = "why are you 10× Express?" + veteran Thai accountant defending it. Play: 事前預防 vs 事後驗屍; Express allows negative stock → 帳實不符 = hidden cash bleed. Comeback pattern: bypass the accountant to the GM with the inventory-truth math ("books say ฿30M, warehouse holds ฿50M — how much is dead stock?"). Loss lesson: selling only to IT/accounting = project dies of "no urgent pain consensus".
**WMS vs local vendors** (30–40% of our price, "free PDA UI edits"): play = ERP+WMS single-source-of-truth real-time deduction vs batch-interface islands; FIFO enforcement/expiry lock-out/picking optimization vs mere scan-recording. Comeback = COO-level risk framing (batch/expiry mis-ship = lawsuit). Loss lesson: pitching only the warehouse manager loses to lowest price.
**MES vs local SI custom** ("we'll connect all 50 machines + write anything"): play = management outcomes (OEE, downtime pareto, WIP traceability, 黃金追溯) vs data-collection theater; productized/maintained vs spaghetti-code orphan. Comeback = CEO-level: "connection shows machines moving; can it tell you if THIS order ships on time, and which material batch/operator caused the defect spike?" Loss lesson: don't out-tech a tech-loving boss on connectivity — reframe to cost/schedule/traceability.

## 11. Thai-localness of benefit benchmarks + citable local cases (Q11)

- **Thai-local share of the §3 benefit benchmarks: ~30–40%**; the other 60–70% is the global blend (TW/CN/VN/MY, 50,000+ manufacturers). NEVER present the blended figures as Thai-local — Thai (especially Thai-national) managers reject TW/CN cases as 不接地氣 ("our 國情/員工 differ"); getting caught inflating localness burns the trust the number was meant to build.
- **When challenged 「這是泰國案例嗎？」— honest-first script (誠實起手 → 痛點共鳴 → 在地標竿)**: (1) admit the headline range is the Asia-wide base of ~50K manufacturers; (2) pivot: our Thai local clients hit the same range UNDER Thai conditions (high operator turnover, language gap on the floor); (3) anchor localization proof: Thai-speaking consultants, Thai-language UI/防呆 on the floor, Revenue Department e-Tax compliance — then bridge into a local case. ⚠️ The script's 「泰國本地有超過 [XX] 家客戶」 count is a PLACEHOLDER — Peter must confirm the real Thailand client count before this line goes into any deck or meeting (proper-noun/number gate).
- **Citable de-identified Thai cases** (real local implementations per NOVA; industry+scale+benefit only, no names):
  1. **Metal/auto-parts, Chonburi, ~350 pp, 2nd-gen family, Tier-1 supplier** — ERP + barcode + kanban: dispatch/misfeed errors −40% (Thai-language kanban replaced misread paper work orders; rework ≈0), month-end close 20d → 5d (fixed trading-entity↔factory 關聯交易 reconciliation).
  2. **Electronics/plastic-injection OEM, Samut Prakan, ~500 pp, multi-entity, Thai+Myanmar operators** — ERP + WMS: count accuracy → 98.5% and find-time −60% despite ~30%/yr warehouse turnover (Thai-UI PDA, day-one onboarding), obsolete stock −25% via enforced FIFO.
- Pre-empt probe (turns the challenge into discovery): ask what localization risk they actually fear — prior vendor failure on e-Tax/法令, or Thai-operator adoption — and what their floor's turnover/barcode status is; that determines which local case to lead with.

## 12. Project AR / retention money — long-DSO reading + pitch calibration (Q12)

For Thai building-materials/metal traders serving construction projects, extreme DSO (300–400d from DBD math) is usually **industry structure, not distress**: progress billing + 5–10% retention (保留金) released only after acceptance. NEVER pitch "your DSO is a problem" — 白目式 opener triggers "you don't know our industry" rejection.
- **DigiWin standard practice = 專案項目控制法**: split each contract into 預付款 / 進度款 1–N / 保留金. Reference case (usable, de-identified): large Thai steel-structure building-materials maker, Excel-tracked acceptance milestones, routinely missed collecting the 5% retention → system now auto-splits each shipment (e.g. 90% normal AR at 90d + 10% retention dated to the project acceptance milestone) and fires collection alerts when the milestone hits.
- **iGP/Workflow AR mechanics**: multi-segment payment terms + 預計收款日 per segment; the **AR aging must key on expected-collection-date (逾期天數), NOT invoice date** — that's what separates 「正常工程帳期」 (within contract terms, incl. undue retention) from true overdue/bad-debt risk (red-flag only when past the contractual acceptance-payment date).
- **Coach-style pitch (痛點翻譯)**: acknowledge the norm first ("we know progress billing + 5–10% retention is standard"), then target the REAL pain: with terms this long, *legitimate* retention and *genuinely overdue* money blur together, and finance misses retention that is already collectible but stuck on missing acceptance paperwork. Quantify: `missed/late retention per year × financing rate (5–7%) = pure lost profit`. The 400d splits into "contractual time (not a pain)" vs "post-acceptance admin black hole (the pain we fix)".
- Probes: (Boss) can finance precisely forecast 3–6-month cash-in; ever had a delayed milestone blow a bid-bond plan? (Finance/PM) how does a Change Order reach finance's billing schedule; ever discovered an uncollected 5% retention six months after project close?
- **Stage prior**: DBD-visible long DSO alone = C2-candidate (objective hidden pain, no confirmed intent). Implementation risk to flag in proposals: 工務↔財務 disconnect — retention alerts die if the site won't report progress; always bundle a simple site-reporting mechanism.

## 13. Nominee-director & informal-power reading (Q13 gap 1 + Q14)

DBD directors ≠ real power. Real decider (founder "advisor", matriarch controlling finance, family council) may not appear in the register at all. **Pre-visit default hypothesis: registered director ≠ 核決者; sketch a nominal-vs-real power map before every visit.** Observable nominee signals in DBD:
1. **Signing-authority configuration**: 3–5 registered directors but binding condition "any ONE director signs" naming A or B → A/B are the real operators, rest are figureheads. Reverse signal: "A + B jointly, C consents" = high-check-balance structure (JV or co-succeeding siblings) → expect VERY slow decisions.
2. **Cross-industry multi-directorship**: same person directing 5+ unrelated-industry companies → professional nominee (lawyer/accountant/group placeholder).
3. **Age + surname structure**: director aged ~25–30 sharing the major shareholder's surname → 2nd-gen figurehead-in-training; the operating power (1st gen) may be shareholder-only.
In-room confirmation (polite, via process not persons): ask which directors' approval flow the project must fit and whether their lens is ROI or compliance; ask whether the chairman/major shareholder joins key decisions personally or delegates fully. Feeds the AUTHORITY CHECK and decision-map fence.

## 14. Turning vested interests into allies; middle-manager resistance (Q13 gaps 3+5 + Q14)

- **Confidant accountant detection** (in-room): vague finance answers, "we report orally to the boss / 老闆娘 checks this personally", accountant tenure ≈ company age, same surname/in-law. **Incumbent-SI depth**: "the system was written by the boss's friend", "they're on call, boss trusts them".
- **Alliance scripts** (never displace, upgrade): accountant → 決策軍師 (automate the drudge work; they present margin analysis & cash forecasts instead of history); local SI → platform-app developer (build 特色應用 on our API platform instead of maintaining spaghetti). **NEVER say the system replaces people or reveals slackers** — that phrase triggers coalition sabotage that kills deals at C2/C1.
- **Middle-manager resistance prediction from OSINT**: chronic job postings for 生管/倉庫主管 with "high pressure tolerance / overtime / manual scheduling" = high turnover + defensive incumbents (防衛指數 high); veteran low-education supervisors (15y+ from the floor) = digitalization fear.
- **Pitch translation rule**: real-time data is NEVER pitched as visibility/monitoring. To 生管/廠長: 防塞單機制 (the SYSTEM says no to sales, not you) + responsibility clarification (no more scapegoating) + data to demand headcount/equipment. To warehouse: 鎖定責任 + on-time 下班. Surveillance narrative = collective revolt.

## 15. Kreng Jai false-positive filter + micro-commitment tests; BOI mechanics (Q13 gaps 2+4 + Q15)

- **Kreng Jai (เกรงใจ) rule**: first-visit smiles / "Very good" / nodding ≈ politeness, NOT intent. Behavior-level TRUE signals: cross-department managers pulled into the room · detail follow-ups on their own pain ("how does it deduct materials for our multi-step outsourcing?") · real report templates volunteered ≤24h · calendar out + "next time I'll bring <decision maker>" · asks about quote structure & budget source. Politeness noise: lone nodding contact, generic feature questions, "we'll evaluate", price-only ask.
- **Two micro-commitment tests, mandatory at first-visit close** (never just "how was the presentation?"): (1) info-cost — ask for 1–2 blank report templates (production daily / AR aging) by a named day; (2) time/relationship-cost — propose a 30-min demo with their Production Manager, offer two concrete slots. **Fail either (2 chases unanswered / PM perpetually busy) → FORCE stage D (nurturing), stop consultant resources, no free diagnosis, no custom demo.** This operationalizes the C2 evidence bar (§8) post-visit.
- **BOI mechanics**: (a) quotes/contracts MUST split Software License / Implementation Consulting / Hardware-Cloud — clients can't claim the digital-investment tax deduction on a bundled line; (b) conditional-contract clause "effective upon BOI approval" lowers signing anxiety; (c) **Tax-Holiday expiry −1~2yr = golden window** ("pay the tax office, or invest it in competitiveness"); new-plant BOI certificate = hard go-live deadline before BOI inspection (~3yr from certificate). First-visit probes: "how many years left on your Tax Holiday — should we split the quote for this year's filing?" / "what's the BOI inspection deadline driving your go-live?"

## 16. Two-books reality + infrastructure readiness (Q16) — V1.0 sign-off (Q17)

- **兩套帳/multi-entity reality trap**: DBD under-reporting often = two sets of books. If unaddressed, implementation dies when the system "can't handle" untaxed/cross-entity flows. CFO probe (first visit): "should multi-entity related-party transactions auto-eliminate in the system, or do some ledgers need physical segregation?" Position: **flexible-architecture provider, never moral police** — multi-ledger + permission isolation satisfies external audit (BOI/DBD) while protecting the owner's real internal data. **Hard compliance boundary (NOVA's own): NEVER help design tax-avoidance flows; provide the architecture, the client defines the process.**
- **Infrastructure hidden killer**: factory Wi-Fi/bandwidth/server/backup routinely inadequate → "your system is slow" → refusal to pay. **Before B stage: require the client's network topology + server spec sheet** (advanced micro-commitment test — also exposes incumbent-SI ownership). De-risk script: free "environment bandwidth stress test" so barcode scans deduct in one second, protecting the go-live schedule.
- **Execution disciplines (sign-off riders)**: (1) failed micro-commitment tests → forced D-downgrade in the pipeline, resist the "pipeline shrink" panic — it purges 毒瘤商機; (2) the two-books stance stays strictly neutral for legal safety.
- **NOVA verdict 2026-07-13: 「已足夠，准予正式定版發布」** — methodology V1.0 (Q1–Q17) formally approved by the examiner loop (Q13 audit → Q14/Q15 fills → Q16 re-check → Q17 stamp).

## 17. Greenfield 台商 — parent-in-Taiwan building its FIRST overseas (Thai) plant (live 2026-07-15, JUFAN run)

For a Taiwan-listed/OTC manufacturer standing up a first BOI greenfield plant in Thailand (parent funds it; ERP choice is a GROUP decision):
- **Stage = C2 (立-隱性) until the 立案三要項 clear**: (1) parent formally budgets the Thai ERP, (2) a Thai IT/finance project owner is named, (3) our side has confirmed the parent's current ERP brand + its group-standard-replication intent. A BOI approval + a go-live target alone do NOT lift above C2.
- **Parent-ERP-unknown triage — ~70% winnable greenfield / ~30% group-template extension.** Extension (30%) if parent runs SAP/Oracle/鼎新高階 + a strong Global-IT team that copies its template abroad. Winnable (70%) if parent runs an early 鼎新 system (易飛/易拓), a local ERP, or a big system it can't localise overseas — because Thai localisation (Thai UI, Revenue-Dept e-tax, BOI 免稅存貨帳) usually forces HQ to allow "local selection with API back to HQ". **Break-in point regardless of parent system = overseas compliance (Thai tax/BOI) + a 台泰 two-country service model HQ doesn't have to staff.** Always pull the parent's Taiwan 年報 to identify the ERP brand (is it a 鼎新/DigiWin user → in-family rollout).
- **Top-Down two-hand play**: (a) HQ (GM/CFO) — sell 上市櫃合併報表合規 + "母公司不必派 IT 駐泰，鼎捷台泰兩地雙語(中/泰/英)服務" to lower HQ management risk; (b) Thai build lead — hand over a BOI/tax 建廠 ERP 檢核清單, enter as consultant, let them recommend upward.
- **Greenfield timing — sign ~6–9 months before go-live; configure during the build.** Best entry = 土建動工~設備採購期 (ERP flow decides warehouse/Barcode layout + BOI 保稅倉 zoning). Back-calc: go-live → −1~2mo 模擬演練+期初開帳 → −~7mo Kick-off → −~9mo sign. Add a 2-month buffer for construction/equipment delay ("設備到了系統沒好，無法收料做工單").
- **Product/module — iGP (cloud, lightweight) start, reserve T100 for group integration** (T100/GP only if HQ demands tight vertical integration/consolidation). Phase-1 = 買賣+基礎製造 only: COP/PUR/INV/GL/AP/AR + **Thai Localization (VAT, WHT)** + BOM + SFC/MOC (simple work orders for BOI 進料加工). **No APS, no WMS in phase 1.**
- **BOI quote-split (same discipline as §15)**: 境外授權/服務 (Taiwan, parent signs — mind **15% WHT** on royalty remittance to Taiwan) vs 在地服務 (Thailand, Digiwin Software Thailand, **7% VAT**-deductible local invoice). ERP must separate BOI 免稅 vs Non-BOI 料件 and produce BOI-audit reports (帳實相符) or the annual audit → back-tax risk.
- **Risk**: Thai labour high turnover → if ERP lacks Thai UI or phase-1 is over-scoped (full T100 mfg), local staff resist and the system dies. Simplify phase 1.

## 18. eMES/WMS complement play on an ENTRENCHED SAP — large family exporter (live 2026-07-17, King Pac run)

For a large Thai family manufacturer that already runs SAP ERP and exports to Western/JP big-box retailers (the "we can't displace the ERP, we ride on top" case):
- **Position eMES/WMS as "SAP 的感知神經 / OT 層執行專家" — SAP's sensing nerve, its hands and feet — NEVER an ERP competitor.** We make SAP's finance + planning data more accurate; we do not replace it. This defuses the "we already have SAP" wall and the internal SAP-loyal IT faction.
- **Beat SAP's own MES (SAP DM/DMC) on TIME-TO-LAND + industry template, never on tech.** SAP DMC's weakness at a packaging/process plant = very high implementation cost and heavy customization for shop-floor logic (for plastics: roll-to-roll 母子卷 mother/child-roll traceability, 配方調撥 formula transfer, 餘料回用 scrap recycling), long and failure-prone. DigiWin's edge = an out-of-box **industry template** ("開箱即用"), 3-4 months to go-live, no change to the SAP core. The wedge sentence = "專屬行業工藝的開箱即用 + 極致 TCO".
- **Sequencing when both a compliance pain and a cost pain exist: COMPLIANCE first (door-knocker), COST/ROI second (budget-lock).** Export-audit traceability (BRC/GMP/AEO/C-TPAT) is a survival "非過不可" issue for a Tesco/Walmart supplier — audit failure = lost orders = immediate revenue loss, and it is the 2nd-gen's safety card → easiest 立案. Then material scrap/yield (resin often >70% of COGS) is the high-ROI story that persuades finance + the 1st-gen chairman to fund it.
- **Stalled IPO = a MES/WMS opening, not a dead signal.** A stalled Thai IPO is usually blocked by 帳實不符 (inventory inaccuracy) + internal-control non-compliance. Package the system as the **"IPO accelerator" + the 2nd-gen's 戰功牌 (achievement to prove succession)**. To the 2nd-gen MD: "digital transformation + data transparency to restart the IPO." To the 1st-gen chairman: "compliance-risk prevention + asset/inheritance protection (don't lose the export customers)."
- **Family-politics rule (2nd-gen operator vs 1st-gen signatory): NEVER take a side.** Frame every argument as **2nd-gen modernization = the spear (expansion, IPO), 1st-gen risk-control = the shield (compliance, preservation)** so both buy in. (Consistent with §6 賦能 each layer.)
- **Named risk: the SAP implementation partner will counter-pitch SAP DM/DMC the moment MES comes up.** Pre-empt by narrowing the client's evaluation complexity to industry-landing-speed + plastic-specific out-of-box functions (吹膜配方, 印刷套色套料).
- Stage discipline unchanged: even with strong audit + IPO pain, it stays **C2 until 立案三要項 clear** (timeline, named DigiWin project team, budget earmarked for us); push to C1 in the first visit.

## 19. PLC-ready thin-margin floor: sequencing + Dynamics AX displacement (live 2026-07-24, Asia Poly Sacks run)

For a Thai maker whose shop floor ALREADY has PLCs on most machines, where material is the dominant cost and margin is thin (here: PP woven-sack/FIBC exporter, resin ~86% of COGS, ~3% net margin, inventory ballooning):
- **A PLC-ready floor does NOT flip the "ERP-first" rule (§1). Go ERP+MES CORE first (inventory + cost); position the existing PLCs as the "MES 自動採集觸角" (auto-collection tentacles), NOT a standalone IoT/OEE lane.** OEE (稼動率) answers "is the machine moving" — irrelevant to the real pain of cash stuck in inventory + razor-thin margin; running machines faster without control just makes more unsellable stock / more scrap.
- **The land-and-expand "let a hardware/IoT distributor land machine-monitoring first, DigiWin brings MES/ERP later" play is a TRAP for this profile** (revises the IHI-style read for thin-margin material-heavy cases): the hardware vendor steers the project to kanban/OEE, misaligned with the owner's real cost-control pain, and once the budget is consumed on dashboards there is no ERP/MES budget left. (The IHI land-and-expand still holds where the ask genuinely IS IoT/Data-Flow and margin/material isn't the wound — profile-dependent.)
- **The winning story = "原料投入產出閉環控制" (material input-output closed-loop):** ERP holds resin purchase batch+price → MES controls 派工 and reads 擠出拉絲/圓織 output via the PLCs → auto precise back-flush + real-time waste alert → ERP produces 逐單實際成本. 痛點翻譯 to the owner: "原料產出率 (Yield) +1% = N 百萬 saved."
- **Dynamics AX displacement (Thai plastics/packaging) — 3 structural weaknesses = the破口:** (1) **BOM/料號 explosion** — spec permutations (size×load×moisture×print×handle) blow up AX's 品號 count; DigiWin 特徵件/dimension management = one 品號 + attributes. (2) **No per-order actual costing on volatile material** — AX standard/weighted-avg cost can't allocate a specific high/low-price resin batch to a specific work order; DigiWin 逐單實際成本 links the MES feed-batch (incl. scrap-recycling offset). (3) **Thai localisation + TCO** — AX2012 EOS, expensive D365 upgrade, MS Thai e-Tax needs 3rd-party custom; DigiWin = Thai local team + built-in e-Tax, far lower TCO. Never fight AX on IT specs / "Microsoft brand" — fight on time-to-standardized-costing + Thai compliance.
- **Entry order for this profile: CFO first** (AX-EOS risk + D365 cost + e-Tax + "I can fix the inventory reconciliation + can't-cost-per-order problem"), **MD second** (expand capacity WITHOUT letting inventory choke cashflow; release warehouse cash to protect/lift the thin margin), **生管/plant third** (use existing PLCs; MES auto-collects, kills manual reports). Even with direct MD contact + acute pains, stage stays **C2 (立-隱性) until 立案三要項 clear** (internal must-replace consensus + named project team + timeline).

## 20. Flexible/printed-packaging converter on a print-specialist MIS + SAP parent — COMPLEMENT play (live 2026-07-27, Dai-Ichi Packaging run)

For a high-margin, cash-rich flexible/printed-packaging converter (gravure print + multi-layer lamination + pouch/lid) that ALREADY runs a print-industry-specialist MIS (e.g. Sistrade) plus a legacy general ERP (e.g. Axapta), inside a group whose LISTED PARENT runs SAP:
- **This is a COMPLEMENT play (eMES/IIoT on top), NEVER an ERP displacement.** Pushing a full-ERP replacement here "無異於自殺" (NOVA). Two walls: (a) a print-specialist MIS owns the genuinely hard print economics — 凹版版胴/版費管理, 套色, multi-layer 溶劑與基材損耗動態折算, roll/rewinder process params — that a general ERP can't match without budget-busting customization; (b) the SAP parent's group-standardization gravity makes the ERP layer unwinnable.
- **Position DigiWin as "SAP/Sistrade 的最佳車間協同者" (best shop-floor co-worker), never a competitor.** Never criticize the incumbent MIS/ERP — that attacks the decision of the family/board that chose it. If the parent raises "standardize on SAP", immediately agree and position eMES as SAP's best shop-floor extension (順著水流走).
- **DigiWin's real edge = the shop floor the MIS/ERP serve weakly:** real-time **母子卷 (roll-to-roll) batch traceability + slitting genealogy + 投料防錯 + solvent/ink-recipe weighing control + barcoding + IIoT/OEE** integrating existing automation islands (ink-dispensing / conveyor / in-line QC). Weakness: any attempt to out-do the print-MIS on estimating/layout loses.
- **For a fat-margin cash-rich "no-pain" buyer, the entry reason is RISK + REGULATION + TIMING, never cost-saving:** food-grade export-audit traceability (Disney CoC / BRCGS / SEDEX — a slow or incomplete 母子卷 trace = recall + supplier de-listing), legacy-ERP end-of-support continuity, EU PPWR, BOI Industry-4.0 incentive timing, and a live re-tooling capex window (configure during the retool). 痛點翻譯: heterogeneous MIS↔ERP forces manual batch-number re-keying → ~15% human-error risk on 投料防錯/recipe → one solvent-residue/ink slip = MNC客訴 + full recall + audit-cert吊銷 = 百萬級 risk (frame as protecting audited-MNC revenue, not saving cost).
- **Product/phase order: Phase 1 eMES (traceability/compliance) → Phase 2 APS (答交 + OEE on frequent gravure changeovers).** Win an on-site "合規與追溯能力診斷" (diagnostic), NOT a system Demo; never open with a price.
- **JV / peer-co-owner governance:** where a co-owner is itself a peer packaging group (its own systems), probe whether it runs the same MIS — if so it will defend it; enrol it as the eMES 推手 (board face) rather than fight it. Decision = the operating-family MD + the co-owner family consensus, gated by parent-IT. Even with a hard EOL clock + audit pressure, stays **C2 (立-隱性)** until 立案三要項 clear.

## 21. ETO/project heavy-machinery greenfield + two-entity merger + Japanese-parent net-new (live 2026-07-27, Nikko Asia-Engineering run)

For an engineer-to-order (ETO) heavy-machinery maker (months-long builds, high WIP, negative gross margin during ramp) — e.g. a Japanese asphalt-plant maker's Thai greenfield with NO incumbent ERP:
- **This is T100 PROJECT-manufacturing with WBS project-lifecycle actual costing — NOT light iGP and NOT plain 生管.** The disease behind negative-GM + high WIP is **設計變更(ECN)造成的料件呆滯 + 工期延宕導致的現場工時失控**, not shop-floor scheduling. Structure = WBS project spine linking PLM (drawing/BOM/ECN change) → 採購 (long-lead mother-child-module procurement) → 現場 (milestone receipt + install) → 財務 (actual-cost 核銷), pulling the 4 cost lines: **估算 / 預算 / 實際 / 變更**. Un-closeable WIP = capital stuck in unfinished projects that can't stage-close = a risk on the parent's consolidated books. Killer first-visit cost question: 「長達數月的專案製造中，發生設計變更或工期延宕時，您能提早幾個月看見毛利預警，還是要等完工結帳(甚至交機數月後)才面對無法挽回的負毛利？」
- **A two-entity merger (mfg + sales + service into one book of record) is a top-tier ERP why-now.** Frame it as a compliance + profit-model DEFENSE, not a bookkeeping buy: a BOI-privileged mfg co + a normal-tax sales/service co merging = asset transfer + **BOI 保稅帳 transfer + transfer-pricing audit** exposure; if the merged books are hand-stitched in Excel → Revenue-Dept fines + BOI-revocation risk. **Make the pie bigger via equipment full-lifecycle service**: high-value long-life machinery → the maintenance + spares + 2nd-hand aftermarket is the multi-year 金雞母; **S/N履歷 (serial-number equipment traceability)** enables proactive preventive-maintenance + parts sales — fold project-mfg + service + spares into ONE system now.
- **Japanese-parent-gravity net-new** (100% Japanese greenfield; parent likely on a Japanese ERP OBIC/GLOVIA/Mcframe): break in on the Japanese ERP's Thai death spot — **weak Thai e-Tax + BOI 保稅/原料帳 localization** (astronomical customization + Japan-HQ IT dispatch a just-profitable sub can't afford) — plus a **Taiwan-Thai(-Japanese-coordinating) local service team** so HQ needn't staff Thai IT. NEVER fight a Japanese ERP on generic function. Japanese decision-makers value 確定性 / 風險規避 / 合規性 (J-SOX): lead with RISK + TIMELINE, in a Japanese-language window; make the resident Rep Director the internal ally vs a parent-mandated Japanese-ERP rollout.
- **Inbound first move: do NOT demo.** Send a Japanese/English "merger: system + tax-compliance milestone roadmap" and enter as a compliance advisor; win a 2-hour "merger tax-compliance + project-cost diagnostic," not a system Demo. Greenfield with no IT staff = go-live risk → weight Key-User enablement + SOP build up front. Stage C2→C1.
- **Data note (reusable bug):** `refresh_financials_from_dbd.py` overflows `net_margin_pct` (decimal(8,4), max ±9999.99) on a near-zero-revenue greenfield year (e.g. rev ฿4,620 vs a ฿-1.9M loss → margin ≈ -42,000%), failing the whole load — cap/NULL the ratio when revenue≈0 before it will load greenfield financials.

## 22. Cash-generative but balance-sheet-INSOLVENT owner-run SME + no-BOM commodity industry (live 2026-07-31, Buathong Ice 2532 run)

Two priors that usually co-occur in provincial owner-operator businesses. Either can be applied alone.

- **A. Separate CASH from the P&L before you disqualify.** A long-established plant with heavy old PP&E can report losses for years while generating real cash: depreciation with no reinvestment is a non-cash charge. Add it back before judging affordability (Buathong: net loss -฿5.87M but approx +฿4.6M EBITDA, with ฿0 interest paid). NOVA ruling: **可以接, 但必須採取「極端防禦性」的商務條款** — the classic 「資產在口袋, 債務在公司」 owner-type firm, where the COMPANY is insolvent but the FAMILY is not. Defence lines: (1) **no financing at all** — never post-acceptance payment; SaaS prepaid monthly/quarterly, or 100 percent prepay (licence outright, consulting pre-settled by stage); (2) **consulting = pre-purchased man-days**, work stops the day payment stops; (3) **carry no hardware or network** — client binds their own card to the cloud provider; (4) **never release a licence key or start customisation before full prepayment**. Funding note: a loss-making company gets **ZERO** from a tax deduction (the Thai 200 percent CIT digital deduction is worthless with no taxable profit, and quoting it signals we did not read the accounts) — pitch **GRANTS** instead: สสว./OSMEP BDS co-payment (50-80 percent, <=฿200k) and depa d-Transform (<=฿1M or 60 percent).
- **B. No-BOM commodity manufacturing (ice, drinking water, gas, aggregate, basic milling): do NOT sell MES/APS. Sell 物流防弊 + 能耗分攤.** Where the product is one SKU with no bill of materials and no routing, there is no shop-floor complexity to instrument — profit leaks downstream, in **配送車輛與收現環節 (跑冒滴漏)**. Core mechanism = **「出庫量 vs 解繳現金」勾稽**: in an all-cash trade the standard hole is *"the driver sells 100 bags, reports 20 melted, and hands in cash for 80"* — **the shrinkage report is the cover story**. Control load-out quantity, returned/melt quantity, and cash received. Costing without a BOM = monthly total-output allocation: **unit cost = (electricity + water + depreciation + packaging) / tons actually shipped**. Module order: **1 銷售與配送 (出庫/車隊) -> 2 庫存與採購 -> 3 應收與現金現結 -> 4 總帳與簡易成本分攤**.
- **C. Turning an unexplained cost rise into 立案.** When external inputs FELL but unit costs ROSE and the customer's own accounts cannot say why, package the gap as a **利潤黑洞 (Profit Leakage)** in owner language, expressed per day ("your cash register is robbed of ฿X every morning"). Then set expectations honestly: **系統是止血鏡, 不是印鈔機**. Name the share of the break-even gap the system can realistically recover (the unexplained leak), and attribute the rest to route-profitability analysis and strategic repricing of low-margin customers. The declaration that keeps the deal: 「系統無法直接幫您多賣冰塊, 但能確保您賣出去的每一袋冰, 現金都安全地流回您的口袋。」 **Arithmetic discipline: do NOT add the cost increase to the net loss — the increase is a COMPONENT of the loss.** NOVA itself double-counted this (250萬 + 587萬 = 830萬); an owner's bookkeeper catches it instantly and it costs the credibility the rest of the pitch depends on.
- **D. Three pre-qualifying questions before scoping any anti-leakage system in an owner-run firm.** (1) **核決企圖** — is the owner building to pass on (永續經營) or to stop the bleeding and sell? This sets funding depth. (2) **資金真實來源** — who holds the large interest-free long-term debt: the family (capacity exists, owner decides alone) or a bank with interest suspended (the firm is in workout; lender consent may be needed and the facility can be pulled)? (3) **現場權力結構** — are the drivers, plant manager and bookkeeper relatives or hired? An anti-leakage system cuts off someone's skim, so this predicts internal resistance and tests whether the owner has the will to push it through.
- **E. Highest-yield, cheapest discovery move: ride along on one delivery vehicle for a day.** Watch how the driver transacts, records shrinkage, and settles at the depot. In cash-delivery industries this is where the leak becomes visible, and one hole caught converts the owner's 立案 decision on the spot.
- **Stage note:** owner-initiated contact plus clear pain still grades **C2 (立-隱性)** while budget, project team and timeline are all absent. "Seeking a remedy" is not yet 立案 and can retreat to 維持現狀.

## Usage map (which dossier section each entry feeds)

| KB entry | Feeds |
|---|---|
| §1 entry wedge | §13 pain→product; 60-sec Fit line; Key Sales Angles |
| §2 base rates + diagnosis | D1 verdict prior; Discovery Priorities (the 3-question probe); Competitive Landscape |
| §3 ROI benchmarks | pain-in-฿ fence (assumption ranges → citable DigiWin ranges) |
| §4 gates + red flags | Early-DQ Gate; Fit Assessment; budget-capacity fence; deal-structure recommendation |
| §5 trigger ranking | §16 urgency taxonomy weighting; 60-sec 急 line |
| §6 authority playbook | decision-map fence; AUTHORITY CHECK follow-through; stage cap logic |
| §7 multi-entity | §17 group-map; Template-D/quote scoping; contract-entity choice; ownership probes in Discovery |
| §8 C2 evidence bar | OSINT Recommended Stage rules; pre-visit qualification |
| §9 objection library | NEW objection-preempt block; Talking Points; low-margin deal structure |
| §10 competitive plays | Competitive Landscape section; displacement/defense verdicts |
| §11 Thai-local citability | pain-in-฿ fence (which figures may be pitched as "Thai"); Talking Points origin-challenge script; local-case proof pairing per industry |
| §12 project AR/retention | pain→product AR row; DSO red-flag interpretation (industry-structure vs distress); sales-angle wording for construction-adjacent traders; stage prior for long-DSO findings |
| §13 nominee/informal power | Directors table read; AUTHORITY CHECK; decision-map fence (nominal-vs-real power hypothesis); Discovery Priorities probes |
| §14 allies & resistance | Key People hypotheses (accountant/SI/middle-manager 防衛指數 from job ads); Talking Points framing rules (no surveillance narrative); objection-preempt block |
| §15 Kreng Jai + BOI | Discovery Priorities (2 mandatory micro-commitment tests + BOI window probes); Stage Recommendation discipline (fail → D); quote-structure note in deal-structure recommendation |
| §16 two-books + infra | Group-map/CFO probe; pre-B infrastructure checklist; compliance boundary note |
| §22 insolvent-but-cash-positive + no-BOM commodity | Early-DQ Gate (never disqualify on reported loss alone — run the depreciation add-back); budget-capacity fence (defensive terms, grants not tax deductions); pain→product (route/cash reconciliation + energy allocation, NEVER MES/APS); Key Sales Angles (profit-leakage framing + the honest declaration); Discovery Priorities (3 pre-qual questions + the ride-along) |

## §20 — Cost-frame language re-triggers the anti-ERP defense in light-tool-seeking SME owners (NOVA live 2026-08-11, Asia Poly Sacks deck-resonance ruling)
When an owner has explicitly said "no ERP, I want a light tool," classic cost-ledger framings — 全倉盤點, 人料機全算進去, financial cost computation — READ AS HEAVY-ERP ACTIONS in his mind and re-raise the wall, even when hedged. Translate downward: 財務算成本 → 現場看流失 (talk floor-level leakage in HIS units: resin waste, rework, wrong pieces — not ledger cost); an inventory-count question is itself a heavy-ERP tell — replace with a rework/waste question inside a number he already accepts. Value-spine ordering for this owner type: his stated management pain FIRST (fairness/accountability), waste-made-visible second, cost-as-natural-byproduct third ("手腳先動, 大腦不動, 成本自然產出"). Quantify FOR him in physical objects ("3 percent leak = X tonnes of resin a day = a Benz a year"), never demand his number. Generalizes to any 2nd-gen Thai SME owner asking for a point tool while the financials show a structural cost wound.

## 23. Sub-gate SME — revenue FAR below the iGP floor but fast-growing, cash-fragile (live 2026-08-18, Manston Foods run)

Case shape: ฿44M revenue (iGP gate = ฿100–300M), 3 straight years +20%+ growth, net margin 0.86% (below the 1.5% red line), one year of negative equity, current ratio <1, first-ever borrowing, inventory 42% of assets and growing faster than revenue, multi-channel (wholesale + e-commerce + new physical outlet), zero system evidence (Excel/manual likely), food-safety compliance push (GMP done, HACCP in progress).

NOVA ruling (verbatim gist, tag 【NOVA live 2026-08-18】):
- **Disposition: watch-list + low-cost digital "pain touch" only — never heavy consultative pursuit.** Heavy iGP pursuit on this balance sheet = "必虧無疑" (we lose money for certain) and they cannot pay a large first installment.
- **Lightweight entry (EDH-style 進銷存-first) is worth sales time ONLY if standardized / zero-custom / live within ~1 week.** The test is Time-to-Value; any customization mire kills the economics. The hook is perishable-inventory cash lock-up (inventory turns = survival at sub-1% margin).
- **Re-engagement triggers to set on the watch-list:** (1) the newest channel completes its first full quarter (multi-channel manual reconciliation hits crisis); (2) the compliance certification (HACCP) is actually obtained (B2B modern-trade orders arrive and Excel fails audits); (3) any capital/equity event fixing the liquidity crisis.
- **Compliance + multi-channel inventory sync IS a valid wedge at this size — but framed as OWNER RISK, never system features:** translate to "stock mistakes → expired product reaching customers → certification revoked + channel fines → fatal at 0.86% margin."
- **First touch = digital only** (LinkedIn/Email lightweight case piece, e.g. "inventory control → +1% net margin + compliance traceability"); a reply proves 企圖 exists before any visit is booked.
- **Payment guard for any deal that does form: 100% deposit or SaaS monthly/quarterly subscription only** — never milestone/installment terms against a current-ratio-<1 balance sheet (bad-debt risk explicitly flagged).
- Stage discipline: OSINT depth alone ≠ contact — such a company enters at D (intent unconfirmed; 立案三要項 all zero).

Reusable prior: for any prospect below ~half the iGP revenue floor, the decision tree is Go-lightweight (only if standardized + fast TTV + a cash-survival pain like perishable inventory) / else watch-list with 3 concrete dated triggers / never heavy pursuit; and collections risk is part of the qualification, not an afterthought.

## 24. NON-THAI (Taiwan-domiciled) prospect in 鼎新's home market — dual-track, NOT a referral (live 2026-08-19, Cobra King run, job f8107591)

**Situation class.** A Taiwan-domiciled manufacturer with strong fundamentals, no Thai legal entity, no
existing 鼎新 relationship, surfaced by the Thailand team. Applies to any 台商 prospect that lands in
Peter's lap but is legally and operationally in Taiwan.

**Ruling — 「台灣拉動、泰國落地」 dual-track, not a hand-off:**
- Thailand's standing role is **「海外雷達與合規顧問」** — collect first-hand build-signals locally (Thai BOI,
  泰國台商商會, industrial-estate offices) and provide local tax/compliance/system-build consulting on landing.
- **Thailand engages directly ONLY IF** a Thai entity is registered, land is bought, or a 建廠小組 is posted —
  then approach the build lead on the ground (usually the 特助 or the 2nd-gen).
- **Otherwise refer to Taiwan at once.** Decision brain + capex authority + family core stay at the parent;
  the Thailand team cannot move a Taiwanese parent's budget. Route to the owning TW branch/BU.
- **Attribution: standard S/D split** — Source (TW parent-relationship, contract, group-consolidation design)
  50–70%; Destination (local delivery, local compliance, customisation, support) 30–50%. Register as a
  **跨國協同報備** case in CRM; neither side commits price unilaterally.

**South-bound tripwire — 投審會 approval is TOO LATE.** Leading indicators, best first:
1. **Job posts** for 泰國建廠經理 / 雙語建廠特助 / 泰國廠財務主管 on 104 or LinkedIn — leads 投審會 by **3–6 months**.
2. **MOPS 公開資訊觀測站 資金貸與 / 重大資產取得 announcements** — legally mandatory for a **公開發行** company
   investing overseas, so the money shows before it moves. *Only available if the target is 公開發行 —
   check that status first; a private TW company gives no such warning.*
3. **Thai BOI quarterly approved-foreign-investment lists** — at landing.

**Stage discipline.** Excellent financials + real 企圖 still do NOT make it C2. With no vendor relationship,
no IT head, and **no budget / no timeline / no project team (立案三要項 unmet)** the grade is **D 級 (起-意向)**.
Do 痛點翻譯 and 企圖探尋 before any proposal.

**Generalisable wedge rulings from the same job (AM auto-parts / family-group shape):**
- **Labour-law penalties are NOT an ERP wedge.** To an owner a few tens of thousands NT$/THB is 「管理微恙」,
  an emotional complaint, not a business risk — and opening with 勞檢 gets the rep **stopped at 總務/HR and
  never into the decision circle**. Use only as an HR-module door-opener. (Generalises to any compliance-fine
  finding in an OSINT dossier: fines are colour, not the wedge.)
- **Related-party transaction volume IS a wedge, for a 公開發行 or IPO-track company.** Large, fast-growing
  intra-group payables are the 「關係人交易不公允」 red line — live tax-inspection risk now, fatal audit risk
  later. Sell the CFO a two-entity bidirectional reconciliation + auto-offset mechanism.
- **Convert inventory days into free cash flow in the CFO's own currency** ("87 days → 75 days releases NT$Xm")
  rather than pitching scheduling as a capability.
- **A long digitalisation desert is a RISK, not just an opportunity.** Decades with no IT record implies
  電腦化排斥 / 資訊孤島 and low absorptive capacity: **never open with MES or APS** — start at 進銷存與財務合規.
  Otherwise the project dies of 吸收能力不足.
