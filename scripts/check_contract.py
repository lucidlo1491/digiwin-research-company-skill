#!/usr/bin/env python3
"""check_contract.py — /digiwin-research-company v4 output-contract checker (stdlib only).

Enforces the ingest-boundary + quality contract on a gold-standard dossier
BEFORE it may be promoted into docs/ (nightly auto-commit is live).
Red-team-derived rules, 2026-07-09; boundary behaviors verified against the
live parser database/ingest_md_to_db.py.

Usage: python3 check_contract.py <dossier.md> [--deep]
Exit 0 = all PASS. One "PASS|FAIL <check>" line per check.
"""
import re, sys

def main():
    args = [a for a in sys.argv[1:] if a != "--deep"]
    deep = "--deep" in sys.argv[1:]
    if not args:
        print("usage: check_contract.py <dossier.md> [--deep]"); return 2
    src = open(args[0], encoding="utf-8").read()
    fails = 0
    def check(name, ok, detail=""):
        nonlocal fails
        print(("PASS " if ok else "FAIL ") + name + (f"  — {detail}" if (detail and not ok) else ""))
        if not ok: fails += 1

    # ---- banners -------------------------------------------------------------
    check("tier-banner", bool(re.search(r"(?m)^>\s*Research tier:\s*(QUICK|DEEP)", src)))
    check("internal-banner", bool(re.search(r"(?m)^>\s*INTERNAL WORKING DOSSIER", src)))

    # ---- required headings (ingest anchors + v4 sections) ---------------------
    req = [
        (r"(?im)^#{1,4}\s+.*60-SECOND PRE-CALL READ", "60-second-read"),
        (r"(?im)^#{1,4}\s+directors", "directors-heading"),
        (r"(?im)^#{1,4}\s+key people", "key-people-heading"),
        (r"(?im)^#{1,4}\s+ownership", "ownership-heading"),
        (r"(?im)^#{1,4}\s+(technology\s*&\s*systems|technology and systems)", "technology-heading"),
        (r"(?im)^#{1,4}\s+(sources|all sources)", "sources-heading"),
    ]
    for pat, name in req:
        check(name, bool(re.search(pat, src)))

    # ---- forbidden headings (ENTITY_HDR semantics: (?im), \s+) ----------------
    forb = re.findall(r"(?im)^#{2,4}\s+((?:entity\s*\d+|primary target|secondary target|sibling)\b.*)$", src)
    check("no-forbidden-headings", not forb, "; ".join(forb[:3]))

    # ---- Key People: prose only (no pipe tables, no bullets) ------------------
    m = re.search(r"(?im)^(#{1,4})\s+key people.*$", src)
    kp_ok, kp_detail = True, ""
    if m:
        lvl = len(m.group(1))
        rest = src[m.end():]
        nxt = re.search(rf"(?m)^#{{1,{lvl}}}\s+", rest)
        body = rest[:nxt.start()] if nxt else rest
        if re.search(r"(?m)^\s*\|", body):
            kp_ok, kp_detail = False, "pipe table inside Key People (ingests as registry directors)"
        elif re.search(r"(?m)^\s*[-*]\s+\S", body):
            kp_ok, kp_detail = False, "bullet list inside Key People (ingests as directors when Directors missing)"
    check("key-people-prose-only", kp_ok, kp_detail)

    # ---- AUTHORITY CHECK line --------------------------------------------------
    check("authority-check", bool(re.search(r"AUTHORITY CHECK:", src)))

    # ---- no 【推論】 inside pipe-table rows of INGESTED sections ----------------
    # (the two non-ingested inference tables — Urgency Signals, Group Structure — carry tags BY DESIGN)
    exempt_spans = []
    for pat in (r"(?im)^(#{1,4})\s+urgency signals.*$", r"(?im)^(#{1,4})\s+group structure.*$"):
        m2 = re.search(pat, src)
        if m2:
            lvl = len(m2.group(1))
            rest = src[m2.end():]
            nxt = re.search(rf"(?m)^#{{1,{lvl}}}\s+", rest)
            exempt_spans.append((m2.start(), m2.end() + (nxt.start() if nxt else len(rest))))
    def exempted(pos):
        return any(a <= pos <= b for a, b in exempt_spans)
    bad_rows, pos = [], 0
    for ln in src.splitlines(keepends=True):
        if ln.lstrip().startswith("|") and "【推論】" in ln and not exempted(pos):
            bad_rows.append(ln.strip()[:70])
        pos += len(ln)
    check("no-inference-in-ingested-tables", not bad_rows, bad_rows[0] if bad_rows else "")

    # ---- signing authority labelled line (when a Directors table exists) ------
    if re.search(r"(?im)^#{1,4}\s+directors", src) and "PENDING" not in src.split("Directors")[1][:200]:
        check("signing-authority-line", bool(re.search(r"(?i)signing authority\s*[:：]", src)))

    # ---- group map ⇒ explicit exports line -------------------------------------
    if re.search(r"(?im)^#{1,4}\s+group structure", src):
        has_exports = bool(re.search(r"(?im)^\s*\|?\s*exports?\s*[:：|]", src) or
                           re.search(r"(?im)^exports:\s*not found\s*$", src) or
                           re.search(r"(?im)export market", src))
        check("explicit-exports-line", has_exports,
              "Group map present but no explicit Exports line — parser scavenges 'Export' from entity names")

    # ---- urgency table: Date-first + tagged rows -------------------------------
    if deep or re.search(r"(?im)^#{1,4}\s+urgency signals", src):
        m = re.search(r"(?im)^(#{1,4})\s+urgency signals.*$", src)
        ok, detail = bool(m), "section missing"
        if m:
            lvl = len(m.group(1))
            rest = src[m.end():]
            nxt = re.search(rf"(?m)^#{{1,{lvl}}}\s+", rest)
            body = rest[:nxt.start()] if nxt else rest
            rows = [ln for ln in body.splitlines()
                    if ln.lstrip().startswith("|") and "---" not in ln
                    and not re.match(r"(?i)^\s*\|\s*date\s*\|", ln)]
            if not rows and "no timing trigger found" not in body.lower():
                ok, detail = False, "no rows and no explicit no-trigger line"
            for ln in rows:
                first_cell = ln.split("|")[1].strip() if ln.count("|") >= 2 else ""
                if not re.search(r"(19|20)\d{2}", first_cell):
                    ok, detail = False, f"row not Date-first: {ln.strip()[:60]}"
                    break
                if not re.search(r"【(DBD|公開|推論|電話|DB)】", ln):
                    ok, detail = False, f"row untagged: {ln.strip()[:60]}"
                    break
        check("urgency-table", ok, detail)

    # ---- tech section: no-signal must be blockquote, not a row -----------------
    m = re.search(r"(?im)^(#{1,4})\s+technology\s*&?\s*(and\s+)?systems.*$", src)
    if m:
        lvl = len(m.group(1))
        rest = src[m.end():]
        nxt = re.search(rf"(?m)^#{{1,{lvl}}}\s+", rest)
        body = rest[:nxt.start()] if nxt else rest
        bad = [ln for ln in body.splitlines()
               if ln.lstrip().startswith("|") and re.search(r"(?i)no signal|not found|none found", ln)
               and not re.search(r"(?i)\|\s*unknown", ln)]
        check("tech-no-signal-not-a-row", not bad, bad[0].strip()[:60] if bad else "")

    # ---- null token exact (backported from /research-partner, 2026-07-17) -------
    # A trailing period defeats the parser NULL token: "Exports: not found." was
    # ingested as a real export region (COMMIT burn). Flag it in table rows and
    # labelled lines.
    bad_null = []
    for ln in src.splitlines():
        is_row = ln.lstrip().startswith("|")
        is_labelled = bool(re.match(r"^\s*[-*]?\s*\**\s*[A-Za-z฀-๿一-鿿][\w /()฀-๿一-鿿]*\s*\**\s*[:：]", ln))
        if (is_row or is_labelled) and re.search(r"(?i)not found\.", ln):
            bad_null.append(ln.strip()[:60])
    check("null-token-exact", not bad_null,
          f"trailing period defeats the parser NULL token: {bad_null[0]}" if bad_null else "")

    # ---- INTERNAL fences --------------------------------------------------------
    fences = len(re.findall(r"(?m)^>\s*INTERNAL ONLY — never into customer-facing artifacts", src))
    if deep:
        check("internal-fences-6", fences == 6, f"found {fences}, need 6 (60s read/incumbent/decision map/pain-฿/budget/warm base)")
    else:
        check("internal-fence-present", fences >= 1, f"found {fences}, need ≥1 (60-second read)")

    # ---- NOVA judgment ledger (deep; added 2026-11-03, the QLT burn) ------------
    # Every judgment call nova-live-consultation.md names must be ASKED of live
    # NOVA (job id) or carry an allowed N/A with a reason. On QLT three of them
    # (lead ownership for a 100%-foreign target, proof-point choice, pain-฿
    # assumptions + visit-question wording) were decided by Claude alone and the
    # dossier still passed every gate.
    gen = re.search(r"(?m)^>.*Generated:\s*(\d{4}-\d{2}-\d{2})", src)
    ledger_required = deep and (not gen or gen.group(1) >= "2026-11-02")
    if deep and not ledger_required:
        print("NOTE  nova-judgment-ledger not required (dossier generated before 2026-11-02)")
    if ledger_required:
        LEDGER_ITEMS = ["product-fit", "wedge-stage", "competitive", "objections",
                        "authority-family", "lead-ownership", "proof-points",
                        "pain-amounts", "visit-questions", "residual"]
        NA_OK = {"competitive", "lead-ownership", "residual"}
        m = re.search(r"(?im)^(#{2,4})\s+NOVA Judgment Ledger.*$", src)
        ok, detail = bool(m), "section '## NOVA Judgment Ledger' missing"
        if m:
            lvl = len(m.group(1)); rest = src[m.end():]
            nxt = re.search(rf"(?m)^#{{1,{lvl}}}\s+", rest)
            body = rest[:nxt.start()] if nxt else rest
            rows = {}
            for ln in body.splitlines():
                cells = [c.strip() for c in ln.strip().strip("|").split("|")] if ln.lstrip().startswith("|") else []
                if len(cells) >= 3 and cells[0].lower() in LEDGER_ITEMS:
                    rows[cells[0].lower()] = cells
            foreign = bool(re.search(r"(?i)(100\s*%[^\n|]{0,40}(foreign|malaysia|china|chinese|japan|taiwan|singapore|korea|hong kong))|((foreign|malaysia|china|japan|taiwan|singapore|korea)[^\n|]{0,40}100\s*%)", src))
            problems = []
            for item in LEDGER_ITEMS:
                c = rows.get(item)
                if not c:
                    problems.append(f"{item}: no row"); continue
                status, job = c[1], c[2]
                if status.upper().startswith("ASKED"):
                    if not re.search(r"\b[0-9a-f]{8}\b", job):
                        problems.append(f"{item}: ASKED without an 8-hex NOVA job id")
                elif status.upper().startswith("N/A"):
                    if item not in NA_OK:
                        problems.append(f"{item}: N/A not allowed — must be asked")
                    elif item == "lead-ownership" and foreign:
                        problems.append("lead-ownership: target is ≥100% foreign-held — must be asked")
                    elif len(re.sub(r"(?i)^n/a\W*", "", status)) < 10:
                        problems.append(f"{item}: N/A needs a reason (≥10 chars)")
                else:
                    problems.append(f"{item}: status must start ASKED or N/A")
            if problems:
                ok, detail = False, "; ".join(problems[:4])
        check("nova-judgment-ledger", ok, detail)

    # ---- industry layer (deep; added 2026-11-03, the QLT burn) ------------------
    # A deep dossier must cite the sub-industry brief it used (reused or newly
    # swept) from docs/industry-briefs/. On QLT a matching 6-week-old brief
    # existed and was never opened.
    if ledger_required:
        has_brief = bool(re.search(r"docs/industry-briefs/[a-z0-9-]+\.md", src))
        check("industry-brief-cited", has_brief,
              "no docs/industry-briefs/<slug>.md cited — reuse a brief <6 months old or run the NotebookLM sweep (industry-sweep.md)")

    # ---- Site & Map Check (both tiers; added 2026-11-03) -------------------------
    # tools/maps/places.py check output: a Google place ID or the explicit
    # "NOT FOUND on Google Maps" line. Dossiers generated before 2026-11-02 exempt.
    gen2 = re.search(r"(?m)^>.*Generated:\s*(\d{4}-\d{2}-\d{2})", src)
    if not gen2 or gen2.group(1) >= "2026-11-02":
        m = re.search(r"(?im)^##\s+Site & Map Check.*$", src)
        ok, detail = bool(m), "section '## Site & Map Check' missing — run tools/maps/places.py check (SKILL Step 2.3)"
        if m:
            rest = src[m.end():]
            nxt = re.search(r"(?m)^##\s+", rest)
            body = rest[:nxt.start()] if nxt else rest
            if not (re.search(r"place ID `[A-Za-z0-9_-]{20,}`", body) or "NOT FOUND on Google Maps" in body):
                ok, detail = False, "no Google place ID and no 'NOT FOUND on Google Maps' line"
        check("site-map-check", ok, detail)

    # ---- deep-only: module banners are legitimate but noted --------------------
    if deep:
        failed = re.findall(r"MODULE FAILED \(D\d\)", src)
        if failed:
            print(f"NOTE  {len(failed)} module-failure banner(s) present — PARTIAL ship: {', '.join(failed)}")

    print(("ALL PASS" if fails == 0 else f"{fails} FAIL"))
    return 0 if fails == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
