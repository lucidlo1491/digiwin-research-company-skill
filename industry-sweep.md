# Industry Sweep — NotebookLM Deep Research as the Phase-0 breadth arm

Added 2026-08-25 (Peter: "wire it in"). This is the **industry layer only** — the entity layer
(DBD, ImportYeti, directors, financials, NOVA fit ruling) stays with `/digiwin-research-company`;
NotebookLM cannot reach those sources.

## When to run
- A sub-industry we have NOT briefed before (no prior deck/industry brief to reuse), OR
- a moving regulation (PPWR, CBAM, ISO 14067 …) where the landscape shifted since the last brief.
Skip when a recent brief exists — reuse and spot-refresh instead (don't pay 15–30 min for a re-read).

## How to run
1. Build the prompt from the template below (fill `{{sub_industry}}`, `{{client_context_neutral}}` —
   NEVER the client's name or numbers; the sweep is outbound text to Google).
2. `notebooklm-mcp`: `research_start` with the prompt (creates/uses a notebook), then poll
   `research_status`; on completion `research_import` → the briefing lands as a notebook source.
3. Save the briefing to `docs/<deck>/industry-sweep-<date>.md`,每 claim keeps its citation and is
   tagged 【NotebookLM sweep <date>】.
4. Fold into the Phase-0 industry brief. Rules: hedged 產業普遍現象 only; no client-specific claims;
   strategy reasoning inside internal fences; conflicts with DBD/NOVA evidence → the gated source wins.

## The prompt template (NOVA-calibrated 2026-08-25 — 商機助手 live ruling, D-stage首訪準備)

NOVA's priority ORDER (differs from intuition — regulation is NOT #1; a regulation only counts
when it carries a penalty/audit clock, otherwise it's noise). Each dimension exists to be
translated into 老闆-language pain (NOVA's 痛點翻譯 column, kept inline):

```
Research the {{sub_industry}} industry in Thailand for a manufacturing-operations briefing.
Audience: an ERP/MES consultancy preparing a first meeting with a mid-size Thai manufacturer
({{client_context_neutral}}, e.g. "an export-oriented flexible-packaging converter").
Cover, in priority order, with sources and dates for every claim:

1. ORDER-PATTERN SHIFT — brand-customer lead-time compression, small-batch/high-mix trends,
   rush-order (插單) frequency in this vertical in Thailand. [痛點翻譯: 交期延誤與罰款風險 —
   排程混亂、停工待料、掉單/大客戶罰款]
2. COST-STRUCTURE PRESSURE — raw-material price volatility for THIS industry's inputs (name
   them, e.g. PE/PP resin, solvents), energy, published margin trends for Thai players.
   [痛點翻譯: 毛利流失與報價失準 — 算不出單一訂單實際成本, 報價跟不上漲幅, 接越多虧越多]
3. BUYER-SIDE REQUIREMENTS with a real clock — what EU/US/JP customers now AUDIT Thai suppliers
   on (batch traceability, recall speed, ESG data), incl. regulations ONLY where an enforcement
   date + penalty/disqualification exists ({{known_regs}}). [痛點翻譯: 抽單風險 — 24小時拉不出
   批次追溯報告 = 失去供應商資格]
4. FIELD BOTTLENECKS specific to this industry's process steps — where practitioners publicly
   describe waste, changeover loss, scrap/offcut (餘料/回料) control, machines that don't talk
   (trade press, case studies, job postings, seminars). [痛點翻譯: 資金佔用/呆滯料 — 重複採購,
   換線效率, 呆滯吃現金流]
5. GOVERNMENT INCENTIVE WINDOWS — BOI digital/Industry-4.0 programs with dates and what they
   cover. [痛點翻譯: 錯過補助窗 = 多花30-50%建置成本]
6. PEER DIGITALIZATION MOVES — Thai/regional peers in this vertical that announced ERP/MES/IoT
   projects in the last 24 months, framed as WHAT DELIVERY/QUALITY PROBLEM they solved and which
   customers they won — never their IT budget totals.

EXCLUDE (NOVA blacklist): market-size/CAGR forecasts ("市場再大, 我收不到錢有什麼用"); policy
pronouncements WITHOUT penalties or dates (綠色生產倡導 etc.); competitor IT spend totals;
generic Industry-4.0 essays; vendor marketing; any specific named company's internal affairs.
```

## What NOT to ask for (NOVA's 無效資訊排除清單, verbatim-grounded)
- 宏觀產值/CAGR — boss can't collect money from a market forecast
- 無罰則無時程的政策宣示 — no 非做不可, ignored
- 對手 IT 預算總額 — useless; only "what delivery problem they solved, which customer they took"
- Anything the entity layer answers better (financials, directors, systems of a specific company)

## Bonus: NOVA's 5 golden first-visit questions for Thai flexible packaging (reference set)
Boss: ① audit-traceability days (粒子→配方→油墨→成品, affects 續約?) ② per-order actual-margin
lag (報價過低接單越虧?). Manager: ③ changeover/cylinder losses per day (找版/等版/洗機工時)
④ 餘料/回料 control (系統有帳現場找不到 → 重開料 → 呆滯). Operator: ⑤ how many Excel/paper
hops per order, hours/day of re-keying. — use these as the question spine when the deck's
sub-industry is flexible packaging; for other verticals, regenerate via NOVA with this shape.

## Output contract
`docs/<deck>/industry-sweep-<date>.md` header carries: sweep date · notebook id · prompt used ·
"【NotebookLM sweep】 = secondary source; DBD/NOVA/transcript evidence overrides on conflict".
The deck's Gate-0 industry-brief answers may cite sweep claims only WITH their original citation.
