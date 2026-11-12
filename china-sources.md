# Chinese-side sources — finding and proving a PRC (or Taiwan) parent

> Added 2026-10-27 from the Jinjiale (Thailand) run. Read this whenever the Thai entity has Chinese
> directors, Chinese nationality on DBD, or a Chinese name in the input. Parent identification is
> MAIN-LOOP work and runs BEFORE agent D1 (see SKILL.md Step 3D).

## Why this file exists
WebSearch is US-based. On Jinjiale it returned nothing for the parent across D1 and D2 (30+ queries),
and AIERFU's five arms all came back PARTIAL for the same reason. Baidu, opened in Peter's Chrome
through the Chrome extension, found the parent on the second query. Background agents have no
browser, so they cannot do this — the orchestrator must, and must hand the result to the arms.

## What works, what doesn't (verified 2026-10-27)
| Source | Status from Thailand | Use |
|---|---|---|
| **Baidu search** `baidu.com/s?wd=…` (Chrome extension) | ✅ works, no CAPTCHA | the main finder. Results carry Baike, Sina, Weibo, WeChat, Zhaopin, university careers pages AND registry-mirror snippets |
| **Baidu Baike** `baike.baidu.com/item/<全称>` | ✅ readable in Chrome (403 to WebFetch) | compiled company profile citing qichacha/aiqicha: legal rep, owner %, staff, sales, penalties, history. Grade 【公開】 secondary |
| **qichacha / tianyancha snippets inside Baidu results** | ✅ visible | 统一社会信用代码 (USCC), reg/paid-in capital, 关联企业 count, IP counts — enough to RESOLVE the third-party ID rule |
| aiqicha.baidu.com | ❌ geo-blocked ("中国大陆以外的地区暂不支持访问") | do not try to bypass |
| tianyancha.com company page | ❌ redirects to login | do not log in |
| 国家企业信用信息公示系统 (gsxt) | ❌ CAPTCHA | never solve CAPTCHAs |
| Parent website | often dead/odd (416) | use the Wayback CDX API: `web.archive.org/cdx/search/cdx?url=<domain>/*&output=txt&fl=timestamp,original,statuscode&filter=statuscode:200&collapse=urlkey` |
| Chinese job boards (Zhaopin, BOSS直聘, 58) | ⚠ reachable via Baidu snippets | parent's job ads may name 金蝶/用友/SAP; regional ads give a base rate only |
| University careers pages (就业信息网) | ✅ via Baidu snippets (page body may be unreadable) | parents post overseas-plant recruitment with **investment amount, start date, planned output** — Jinjiale's said "泰国公司投资人民币3亿, 2025年3月投产, 年产值4亿" |

When a registry proof is needed (equity chain, 对外投资 list): ask a DigiWin China colleague on a
mainland network or NOVA, or buy the Thai บอจ.5 shareholder list. Never bypass a geo-block or login.

## The search that finds the parent (in this order)
1. **Directors' names in Chinese, PAIRED, plus the product word.** Transliterate each Thai director
   name to likely characters (ฟาง จุน → 方军; ฟาง เจ๋อหาว → 方泽浩/方哲豪; เซี่ยว อวี้สง → 肖玉雄),
   then search two names together with the product: `方泽浩 方军 铸造`. A single common name (方军)
   drowns in noise; a pair + product does not.
2. **The English name as pinyin of a Chinese brand.** "Jinjiale" = 金家乐 (not the guessed 金佳乐).
   Try the Thai transliteration of the EN name too (จินเจียหลี่). Guessing characters for a brand
   alone failed four times — confirm the brand via step 1 first.
3. **Product + 泰国 + city/district** in Chinese (`泰国 春武里 烧烤 炉排 铸铁`) — finds trade press and
   association notes ("有在泰国设立生产工厂的意向").
4. Once the parent's full name is known: `<全称> 软件著作权`, `<全称> 招聘 ERP OR 金蝶 OR 用友`,
   `<全称> 泰国`, `<全称> 官网`.
Extraction tip (Chrome extension): read results with
`[...document.querySelectorAll('#content_left .result, #content_left .c-container')].map(x=>x.innerText)`;
do NOT return hrefs with query strings (the extension blocks them) — read the `mu` attribute for the real URL.

## Proving the link (contract rules 8 and 9 apply)
A parent claim needs ≥2 independent signals; Jinjiale had five: (1) brand pinyin = EN name,
(2) director = parent's legal rep/owner, (3) same product family as the DBD objective,
(4) **same contact e-mail domain on US bills of lading** for the Thai and the PRC supplier, the Thai
one at the exact DBD address (ImportYeti), (5) the parent's own recruitment notice for its Thai
company. Even five signals prove CONTROL BY A PERSON, not equity: write "common controller, equity
chain unproven" until a shareholder register says otherwise.

## Hand-off to the arms
Write what the main loop found to `docs/research-fragments/<id>/00-context.md` (shared context) and
`orch-*.md` capture files BEFORE dispatching each arm, and append updates as the run learns more.
Every arm's prompt says "read 00-context.md first". On Jinjiale, D1 ran before the parent was known
and came back thin; every later arm built on the parent.

## Mandate flag (both tiers)
A 100% non-Thai-held plant (PRC or Taiwanese parent) is OFF Peter's Thai-local mandate
([[feedback_peter_targets_thai_local_not_taiwanese]] in memory). Research it when Peter asks, but the
60-second read opens with an off-mandate flag, and NOVA live is asked who owns the lead (AIERFU
2026-10-27: TH Chinese-desk / direct team owns it; Peter is lead provider; check ACP for a
colleague's booking first).
