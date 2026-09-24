#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""reference_sweep.py — find every DigiWin reference customer in a prospect's industry BEFORE any deck or dossier
claims "we have no reference for X".

    python3 tools/reference_sweep.py <company-id> --terms "不織布,熔噴,紡粘,nonwoven,spunbond"

WHY (Peter, 2026-09-24): the research searched only the OSINT DB and the Monk slide corpus, concluded
"genuine white space: no nonwoven anywhere", and the deck said "we have not done a nonwoven plant". DigiWin TW's
own case library (mirrored locally since July) held three nonwoven manufacturers — three of them —
and the Monk had one of them on a logo wall. Two negative sources do not prove absence. This sweep searches ALL of them.

Sources (each reports FOUND / none / ERROR — an ERROR source means the verdict can never be NONE):
  1 tw-case   DigiWin TW published cases       docs/digiwin-tw-mirror/_internal/case/*/article.source.zh.md
  2 tw-blog   DigiWin TW blog                  docs/digiwin-tw-mirror/blog/*/article.source.zh.md
  3 tw-dsc    DigiWin TW solution mini-sites   docs/digiwin-tw-mirror/dsc/**/*.html
  4 monk      Sweeping Monk slide cards        ~/.sweeping_monk/cards/*.md
  5 rag       Drive corpus RAG (semantic)      ~/digiwin_rag/rag.py query  (hits count only if they contain a term)

Output: docs/research-fragments/<company-id>/reference-sweep.md — the reference table, then two machine lines
`SWEEP-VERDICT: FOUND <n> | NONE | INCOMPLETE` and `SOURCES: ...`. check_inputs.py (first-visit deck) FAILS
without this file. A case page proves the PAST (feedback_case_currency_not_case_page): the table carries each
page's date; present tense on a slide needs a currency check, and naming a customer needs Peter's OK.
"""
import argparse
import datetime
import glob
import os
import pathlib
import re
import subprocess

REPO = pathlib.Path(__file__).resolve().parents[1]
MIRROR = REPO / "docs" / "digiwin-tw-mirror"
CARDS = pathlib.Path.home() / ".sweeping_monk" / "cards"
RAG = pathlib.Path.home() / "digiwin_rag" / "rag.py"
RAG_PY = "/opt/homebrew/Caskroom/miniconda/base/bin/python3"   # the interpreter that has sqlite_vec


def _body(text):
    """Drop the site chrome that pollutes every mirrored page: menu bullets, image links, prev/next footer, and the
    "更多案例" sidebar (other cases' titles — counting those made names 'appear' in unrelated cases)."""
    text = text.split("更多案例")[0]
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(("- ", "![", "上一頁", "下一頁", "返回")) or not s:
            continue
        out.append(s)
    return "\n".join(out)


def _ctx(text, term, width=70):
    i = text.lower().find(term.lower())
    return re.sub(r"\s+", " ", text[max(0, i - width): i + len(term) + width]) if i >= 0 else ""


def _meta(text):
    title = next((m.group(1).strip() for m in re.finditer(r"^#{1,2} (.+)$", text, re.M)), "")
    date = re.search(r"發布時間[：:]\s*(\d{4}-\d{2}-\d{2})", text)
    company = next((l.strip() for l in text.splitlines()
                    if l.strip() and not l.lstrip().startswith(("#", "-", "!", "文：", "發布", "[", "　"))
                    and 2 <= len(l.strip()) <= 16), "")
    return title, company, date.group(1) if date else ""


def sweep_markdown(pattern, terms, kind):
    hits, n = [], 0
    for f in sorted(glob.glob(str(pattern))):
        n += 1
        raw = open(f, encoding="utf-8", errors="ignore").read()
        body = _body(raw)
        found = [t for t in terms if t.lower() in body.lower()]
        if found:
            title, company, date = _meta(raw)
            hits.append({"source": kind, "id": pathlib.Path(f).parent.name, "company": company, "date": date,
                         "title": title, "terms": found, "context": _ctx(body, found[0]),
                         "path": os.path.relpath(f, REPO)})
    return hits, n


def sweep_dsc(terms):
    hits, n = [], 0
    for f in sorted(glob.glob(str(MIRROR / "dsc" / "**" / "*.html"), recursive=True)):
        n += 1
        raw = open(f, encoding="utf-8", errors="ignore").read()
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S)))
        found = [t for t in terms if t.lower() in text.lower()]
        if found:
            title = re.search(r"<title>(.*?)</title>", raw, re.S)
            hits.append({"source": "tw-dsc", "id": pathlib.Path(f).stem, "company": "", "date": "",
                         "title": (title.group(1).strip() if title else "")[:80], "terms": found,
                         "context": _ctx(text, found[0]), "path": os.path.relpath(f, REPO)})
    return hits, n


def sweep_cards(terms):
    hits, n = [], 0
    for f in sorted(CARDS.glob("*.md")):
        n += 1
        text = f.read_text(encoding="utf-8", errors="ignore")
        found = [t for t in terms if t.lower() in text.lower()]
        if found:
            hits.append({"source": "monk", "id": f.stem[:60], "company": "", "date": "", "title": f.stem[:60],
                         "terms": found, "context": _ctx(text, found[0]), "path": str(f)})
    return hits, n


def sweep_rag(terms):
    """Semantic recall over the Drive corpus. Known weakness (2026-09-24): page chrome in mirrored articles outranks
    content on generic queries, so a hit only counts when its text actually contains a term."""
    q = " ".join(terms[:6])
    try:
        r = subprocess.run([RAG_PY, str(RAG), "query", q, "-k", "12"], capture_output=True, text=True,
                           timeout=300, cwd=str(RAG.parent))
    except Exception as e:
        return None, f"ERROR: {e}"
    if r.returncode != 0:
        return None, "ERROR: " + (r.stderr.strip().splitlines() or ["rag failed"])[-1][:120]
    hits = []
    for block in re.split(r"\n(?=— )", r.stdout):
        m = re.match(r"— (.+?)\s+\(score ([-\d.]+)\)", block.strip())
        if not m:
            continue
        found = [t for t in terms if t.lower() in block.lower()]
        if found:
            hits.append({"source": "rag", "id": m.group(1)[:60], "company": "", "date": "", "title": m.group(1)[:60],
                         "terms": found, "context": _ctx(block, found[0]), "path": m.group(1)})
    return hits, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("company_id")
    ap.add_argument("--terms", required=True, help="comma-separated industry terms, zh + en (+ th)")
    ap.add_argument("--no-rag", action="store_true", help="skip the RAG (the verdict then reads INCOMPLETE)")
    a = ap.parse_args()
    terms = [t.strip() for t in a.terms.split(",") if t.strip()]

    rows, sources = [], []
    for pat, kind in ((MIRROR / "_internal" / "case" / "*" / "article.source.zh.md", "tw-case"),
                      (MIRROR / "blog" / "*" / "article.source.zh.md", "tw-blog")):
        h, n = sweep_markdown(pat, terms, kind)
        rows += h; sources.append(f"{kind}={len(h)}/{n}" if n else f"{kind}=ERROR(no files)")
    h, n = sweep_dsc(terms); rows += h; sources.append(f"tw-dsc={len(h)}/{n}" if n else "tw-dsc=ERROR(no files)")
    h, n = sweep_cards(terms); rows += h; sources.append(f"monk={len(h)}/{n}" if n else "monk=ERROR(no cards)")
    if a.no_rag:
        sources.append("rag=SKIPPED")
    else:
        h, status = sweep_rag(terms)
        if h is None:
            sources.append(f"rag={status}")
        else:
            rows += h; sources.append(f"rag={len(h)}/12")

    # NAME PASS: the Monk records company NAMES (logo walls, reference lists) without their industry, so an industry
    # term never finds them (one sat on a customer logo wall). Search every case company found above by name.
    names = sorted({r["company"] for r in rows if r["source"] == "tw-case" and len(r["company"]) >= 3})
    by_name = 0
    for f in sorted(CARDS.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="ignore")
        for nm in names:
            if nm in text:
                rows.append({"source": "monk-name", "id": f.stem[:60], "company": nm, "date": "", "title": f.stem[:60],
                             "terms": [nm], "context": _ctx(text, nm), "path": str(f)}); by_name += 1
    sources.append(f"monk-name={by_name} (names: {', '.join(names) or '-'})")

    incomplete = any("ERROR" in s or "SKIPPED" in s for s in sources)
    cases = [r for r in rows if r["source"] == "tw-case"]
    verdict = (f"FOUND {len(rows)}" if rows else ("INCOMPLETE" if incomplete else "NONE"))

    out = REPO / "docs" / "research-fragments" / a.company_id / "reference-sweep.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    L = [f"# Reference sweep — {a.company_id} · {datetime.date.today().isoformat()}", "",
         f"Terms: {', '.join(terms)}", "",
         "> A case page proves the PAST, not today's system: quote it with its year; present tense needs a currency",
         "> check (current job posts / NOVA / TW AM). Naming a customer on a slide needs Peter's OK.", ""]
    if cases:
        L += ["## Published DigiWin TW cases", "", "| Case | Company | Date | Title | Terms | Context |", "|---|---|---|---|---|---|"]
        L += [f"| {r['id']} | {r['company']} | {r['date']} | {r['title'][:50]} | {', '.join(r['terms'])} | {r['context'][:120]} |" for r in cases]
        L.append("")
    other = [r for r in rows if r["source"] != "tw-case"]
    if other:
        L += ["## Other mentions (blog, solution pages, Monk cards, RAG)", "", "| Source | Item | Terms | Context |", "|---|---|---|---|"]
        L += [f"| {r['source']} | {r['title'][:50]} | {', '.join(r['terms'])} | {r['context'][:120]} |" for r in other]
        L.append("")
    L += [f"SWEEP-VERDICT: {verdict}", f"SOURCES: {' · '.join(sources)}", ""]
    out.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L[-3:])); print(f"wrote {os.path.relpath(out, REPO)}  ({len(cases)} published cases)")


if __name__ == "__main__":
    main()
