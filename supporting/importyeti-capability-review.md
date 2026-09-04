# ImportYeti — what it gives us, and how to use it in /research-company

> Hands-on review 2026-08-11 by browsing the live site (not from documentation).
> Worked example uses a real prospect: **INNOVALUES PRECISION THAILAND**.
> Source tag for anything pulled from here: **【公開】ImportYeti / U.S. CBP bills of lading**.

## What the data actually is

**U.S. Customs and Border Protection bills of lading** — the manifest filed for every
**ocean** shipment entering the United States. 708,797,536 records, stated as updated daily,
each supplier page showing an explicit "ImportYeti synced <date>".

This matters for how far we can trust it: a bill of lading is a **legal shipping document**,
not marketing copy. Shipper, consignee, product description, HS code and container count are
declared to a customs authority. It is the same class of evidence as a DBD filing.

### Datasets and what costs money

| Dataset | Access |
|---|---|
| **U.S. Imports** | **Free** — this is the one that matters for us |
| U.S. Exports | Paid (★) |
| MX Imports / MX Exports | Paid (★) |
| U.S. Customs Clearance | Paid (★) |

Pricing is not published — the Pricing link routes to a "choose your product" survey
(Yeti Supply Chain / Yeti Logistics). **No public API was found**; access is web-only.
Account login exists but the free search worked without one.

## Field inventory — a supplier page

Verified on `importyeti.com/supplier/innovalues-precision-thailand`:

**Identity**
- Company name, country flag, Supplier/Company tag
- Full shipping address as declared to customs
- **"Also exports under N names and M addresses"** — alias resolution. This is how we catch
  a company shipping under a trading arm or a second entity.
- Website (when matched)

**Volume metrics**
- Last Shipment Spotted · Total Sea Shipments · Avg TEU per Shipment · Avg TEU per Month
- **Est. Shipping Spend**, with an explicit **coverage %** (76% for Innovalues, 9% for another
  company I checked) — the coverage number is the honesty flag; treat low coverage as unusable
- Monthly time series **Jan 2015 → present**, CSV export, with optional Covid-lockdown and
  Trump-tariff event overlays, and a YoY delta

**Customer list — the valuable part**
Per US buyer: name, city/state, shipment-count, a per-buyer activity sparkline, a product-category
mix bar, **the verbatim product description from the bill of lading**, and **HS codes**.
Also CSV export, and "see all bills of lading with this company".

**Cost structure**
Local currency + FX rating, and an estimated labour cost benchmark
(Thailand $409–425/month, comparable against China etc.)

## Worked example — INNOVALUES PRECISION THAILAND

83 Moo 2, Hi-Tech Industrial Estate, Bang Pa-In, Ayutthaya.
**267 sea shipments · avg 1.43 TEU/shipment · 6.45 TEU/month · est. spend $574,551 (76% coverage)
· last shipment 2026-08-05 · last month 3 shipments, −29.41% YoY.**

| US customer | Shipments | Declared products | HS codes |
|---|---|---|---|
| Bei Kimco Magnetics (San Diego) | 55 | Baseball Helmet, Asy Transfer, Shaft, USB Multi Port Adapter | 8483.10, 9033.00, 8544.42, 6506.10 |
| MGS USA (El Paso) | 52 | Insert Cup Machined, Aluminum Crimp Cup | 7326.90, 9033.00, 7010.90 |
| Hilite International | 48 | Pin Locking, Automotive Engine Metal Locking Pin, Calibration Cap Central Valve | 8708.99, 8517.70, 8543.90, 3926.90 |
| Acutex (Whitehall) | 47 | Central Valve CTA, Calibration Cap, Armature | 8483.90, 3926.90, 8481.90, 8708.10 |
| Plastibell Mexico North (Albany) | 18 | Aluminum Crimp Cup, Pallet | 7326.90, 9033.00, 3903.30 |
| Ola Logistics (El Paso) | 8 | Aluminum Crimp Cup | 7326.90 |
| Kavlico (San Diego) | 4 | Front Housing | 8708.99 |

### The inference chain Peter is after

This is where it turns into a sales angle. **The customer list tells you what standards the
prospect must already be living under** — and those standards are exactly what an ERP/MES sells against.

- **Hilite International, Acutex, Kavlico** are automotive Tier-1 / sensor makers. HS 8708.99
  (motor-vehicle parts) and 8481.90 (valve parts) confirm the parts class.
  → Automotive Tier-1 supply means **IATF 16949**, and with it **PPAP, APQP, per-lot traceability,
    8D corrective action, and customer-driven audits**. None of that is optional.
- **Declining volume** (−29.41% YoY, 3 shipments last month) is a business fact worth raising
  carefully — it changes what "efficiency" means to them this year.
- **Two El Paso consignees** (MGS USA, Ola Logistics) plus **Plastibell Mexico** point at a
  **US-Mexico border/maquila flow** — cross-border logistics, USMCA origin documentation.

**The DigiWin conversation those facts license** (all falsifiable, all to be confirmed with the client):
per-lot / per-serial traceability from raw material to shipment; PPAP-grade document control and
revision history; supplier-quality and incoming-inspection records; audit-ready retention; and
customer-specific labelling and packing rules. That is an **eMES + quality-module** conversation,
grounded in who their customers actually are rather than in a generic pitch.

## Traps — read before quoting any of this to a client

1. **The consignee is not always the end customer.** "Ola Logistics" is a freight forwarder.
   Any name ending in Logistics / Forwarding / Cargo is a shipping agent, and treating it as a
   customer in front of the client will be visibly wrong.
2. **Ocean freight only.** Bills of lading cover sea shipments. Air freight is not here — so a
   high-value/low-volume exporter can look far smaller than it is.
3. **US-bound only, on the free tier.** It shows nothing about Thai domestic sales, intra-Asia
   trade, EU/Japan exports, or anything the company imports. A company can be a major exporter
   and appear here as nothing.
4. **Selling through an intermediary hides the maker.** If the prospect sells via a trading
   company, the trading company appears as shipper and the prospect is invisible.
   ASIA POLY SACKS returned no Thai match — that is *not* evidence they don't export.
5. **Est. Shipping Spend is modelled, not declared** — always read the coverage %; ignore it
   when coverage is low (I saw 9% on one company).
6. **Name matching is fuzzy.** Always confirm the address against the DBD record before
   attaching shipment data to a company in our database. Use "Also exports under N names" to
   catch alias entities before concluding anything about volume.

## Recommended integration into /research-company

Add a step after the deep website crawl, writing into the dossier under a new
**Exports & US Customers** heading:

1. Search the company name; **verify by address against the DBD record**, not by name alone.
2. If matched: capture total shipments, TEU/month, last-shipment date, YoY trend, and the
   customer table (buyer, city, shipments, products, HS codes).
3. **Classify each buyer** — end customer vs. forwarder vs. related party — and drop forwarders.
4. Derive the **standards regime** from the buyer set (automotive → IATF 16949; food → FDA/FSMA;
   medical → FDA/ISO 13485; toys → CPSIA) and record it as a **hypothesis to confirm**, never as fact.
5. If no match: record `ImportYeti: no US-bound sea shipments found` **plus the reason it may be
   absent** (air freight / trading intermediary / non-US markets). Today 88 dossiers say
   "no data found" with no such qualifier, which reads as "doesn't export" and shouldn't.

Mechanically this is the DBD pattern — a rendered-page scrape driven by Playwright, since there
is no API. The per-company CSV exports (time series and customer list) are the cleanest capture path.

---

# Vendor bake-off — non-US BOL data (2026-08-11)

Test: search **INNOVALUES PRECISION THAILAND** on each vendor's free/unauthenticated tier and
compare against our verified ImportYeti ground truth (267 US shipments; Hilite, Acutex, Kavlico,
Bei Kimco, MGS USA, Plastibell). **No accounts were created** — that bounds this test to what each
site shows the public.

| Vendor | Result |
|---|---|
| **Panjiva** (S&P Global) | **Works unauthenticated.** Real shipment rows, "limited preview" banner |
| Volza | **Could not evaluate** — stuck on an active Cloudflare challenge widget |
| TradeAtlas | **Could not evaluate** — search 404s; gated behind signup |

## Panjiva's country list — the definitive answer to "where else?"

The dataset picker enumerates every country S&P actually sells shipment-level data for
(🔓 = free preview, 🔒 = paid):

- **North America:** 🔓 United States · 🔒 Mexico
- **Europe:** 🔒 **Ukraine — and nothing else**
- **Central America:** 🔒 Costa Rica, Panama
- **South America:** 🔒 Bolivia, Brazil, Chile, Colombia, Ecuador, Paraguay, Peru, Uruguay, Venezuela
- **Asia:** 🔒 China, India, Indonesia, Pakistan, Sri Lanka, Philippines, Turkey, Vietnam

**This confirms the structural limit: no EU, no Japan, no Korea, no Taiwan, no Thailand.**
If a vendor claims EU or Japanese company-level BOL data, treat the whole offering as suspect.
One correction to my earlier note: **China IS sold** here, despite not being officially public.

## What Panjiva's free preview shows that ImportYeti does not

| Field | ImportYeti | Panjiva (free preview) |
|---|---|---|
| Declared cargo **value (USD)** | ✗ | **✓ $748k over the Feb 28 – May 31 window** |
| Weight / quantity / container count | ✗ | ✓ 85,000 kg · 432 CTN · per shipment |
| **Container marks** | ✗ | **✓ — these name the buyer even when consignee is hidden** |
| Shipper phone number | ✗ | ✓ +66 66818519017 |
| Port of lading/unlading, bill type (House/Master) | ✗ | ✓ |
| Total fields | ~10 | **120** (21 shown in preview) |
| Consignee (buyer) name | **✓ full list** | **✗ redacted in preview** |
| Named buyer aggregation over years | ✓ | paid |

Note the two "spend" numbers measure different things: ImportYeti's **Est. Shipping Spend**
($574k) is modelled *freight cost*; Panjiva's **Value** ($748k/quarter) is *declared cargo value*.
Do not compare them.

**They are complementary, not substitutes.** ImportYeti names the customers for free; Panjiva
quantifies the trade and, via container marks, exposes customers ImportYeti missed.

## New intelligence this produced on a live deal

Container marks on Innovalues shipments name:
- **HUSCO AUTOMOTIVE HOLDINGS LLC** — appears repeatedly, **NOT in ImportYeti's customer list**
- BEI NORTH AMERICA LLC · ACUTEX INC — corroborating the known buyers

HUSCO is an automotive hydraulics/electro-hydraulic Tier-1. Its presence **strengthens the
IATF 16949 inference** already recorded, and adds a named account we did not previously know about.
Also visible: shipment origin splits **Thailand 18 / China 2** — Innovalues ships to the US from a
Chinese site as well, which is a supply-chain fact worth confirming with them.

## Recommendation

1. **Keep ImportYeti as the default free step** — it is the only one that names buyers without paying.
2. **Add a Panjiva free-preview pass for live deals** — for the declared value and, above all, the
   container marks. That is where HUSCO came from.
3. **Only pay if the target sells into Latin America, India, Vietnam, Indonesia, China or Turkey.**
   For an EU- or Japan-facing prospect no subscription helps; fall back to certification scope,
   customer logos, job postings and BOI records.
4. Before buying anything, make the vendor reproduce the Innovalues US picture on a trial. A vendor
   returning less than free ImportYeti is selling a thinner database with a wider claim.
