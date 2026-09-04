#!/usr/bin/env python3
"""Depth gate for /digiwin-research-company deep runs (batch-mode.md AC1-AC4).

Usage: batch_depth_gate.py <company-id> [--fragments-dir DIR]

Checks that a deep run actually ran at full depth BEFORE the dossier is promoted:
  AC1  four fragment files d1-*.md .. d4-*.md exist
  AC2  each ends with STATUS: OK|PARTIAL|FAILED and logs >=8 searches/fetches
  AC3  fragment mtimes are sequential (d1 <= d2 <= d3 <= d4)
  AC4  a nova-live-*.md file exists with a job id and >=800 chars of capture,
       AND postdates the newest arm fragment (the consult must see the research)

Exit 0 = PASS, exit 1 = FAIL (each failure printed with the missing artifact).
"""
import glob
import os
import re
import sys

STATUS_RE = re.compile(r"STATUS:\s*(OK|PARTIAL|FAILED)")
SEARCH_LINE_RE = re.compile(r"(WebFetch|WebSearch|fetch|search)", re.IGNORECASE)
# Compact logs list many sources on one line ("sources consulted: a.com, b.tw, ...") —
# count distinct domain mentions as an alternative depth signal to line count.
DOMAIN_RE = re.compile(r"\b[a-z0-9][a-z0-9.-]*\.(?:com|net|org|tw|cn|th|nu|ai|co|io|gov)\b")
# Website deep-crawls (d4) legitimately concentrate on ONE domain — count distinct
# URL/path tokens (full URLs or /slug/ paths) as a third depth signal.
URLPATH_RE = re.compile(r"https?://\S+|(?<=[\s(`])/[a-zA-Z0-9_][a-zA-Z0-9_/.-]{2,}")
JOB_ID_RE = re.compile(r"job\s+[0-9a-f]{8}", re.IGNORECASE)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    company_id = sys.argv[1]
    frag_dir = f"docs/research-fragments/{company_id}"
    if "--fragments-dir" in sys.argv:
        frag_dir = sys.argv[sys.argv.index("--fragments-dir") + 1]

    failures = []

    if not os.path.isdir(frag_dir):
        print(f"FAIL AC1: fragment directory missing: {frag_dir}")
        return 1

    # AC1 + AC2 — d5 (community & sentiment) required for runs from 2026-07-18;
    # a fragment dir whose newest d1-d4 file predates that is grandfathered.
    newest_core = max(
        (os.path.getmtime(p) for p in glob.glob(os.path.join(frag_dir, "d[1-4]-*.md"))),
        default=0,
    )
    D5_REQUIRED_FROM = 1784678400  # 2026-07-22 00:00 UTC (grace window after 2026-07-18 rollout)
    n_max = 6 if newest_core >= D5_REQUIRED_FROM else 5
    frag_paths = {}
    for n in range(1, n_max):
        matches = sorted(glob.glob(os.path.join(frag_dir, f"d{n}-*.md")))
        if not matches:
            failures.append(f"AC1: fragment d{n}-*.md missing in {frag_dir}")
            continue
        # "Latest variant" means most RECENT, not lexically last. A retry named
        # d4-...-v2.md sorts BEFORE d4-....md (hyphen precedes dot), so lexical
        # sort silently picked a superseded fragment and then failed AC3 against
        # it. Select by mtime, which is what the intent always was.
        path = max(matches, key=os.path.getmtime)
        frag_paths[n] = path
        text = open(path, encoding="utf-8").read()
        if not STATUS_RE.search(text):
            failures.append(f"AC2: {os.path.basename(path)} has no STATUS: OK|PARTIAL|FAILED line")
        n_lines = sum(1 for line in text.splitlines() if SEARCH_LINE_RE.search(line))
        n_domains = len(set(DOMAIN_RE.findall(text.lower())))
        n_paths = len(set(URLPATH_RE.findall(text)))
        n_searches = max(n_lines, n_domains, n_paths)
        if n_searches < 8:
            failures.append(
                f"AC2: {os.path.basename(path)} search/fetch log too thin "
                f"({n_lines} log lines / {n_domains} domains / {n_paths} url-paths, need >=8 of any)"
            )

    # AC3 — sequential production order across whatever fragments exist
    ks = sorted(frag_paths)
    for a, b in zip(ks, ks[1:]):
        if os.path.getmtime(frag_paths[a]) > os.path.getmtime(frag_paths[b]):
            failures.append(f"AC3: d{a} is newer than d{b} — fragments not produced sequentially")

    # AC4 — NOVA live capture
    # Pick the most RECENT capture, not the lexically last — the same bug that
    # bit fragment selection. "nova-live-<date>-post-arms.md" sorts BEFORE
    # "nova-live-<date>-sunrobot-wms.md", so lexical order graded a stale
    # pre-arms consult and failed AC4 against a fresh one that was present.
    nova = sorted(glob.glob(os.path.join(frag_dir, "nova-live-*.md")),
                  key=os.path.getmtime)
    if not nova:
        failures.append(f"AC4: nova-live-*.md missing in {frag_dir}")
    else:
        # AC4b — the consult must POSTDATE the research. The protocol is
        # D1..D5 -> NOVA live -> synthesis: a consult taken before the arms ran
        # never saw their findings. On 2026-08-30 a T.N. Advance capture from
        # 11:10 passed this gate against arms that ran at 21:03-21:38, and a
        # stale ruling was promoted with the dossier.
        newest_arm = max((os.path.getmtime(f) for f in frag_paths.values()), default=0)
        if newest_arm and os.path.getmtime(nova[-1]) < newest_arm:
            failures.append(
                f"AC4: {os.path.basename(nova[-1])} PREDATES the newest arm fragment "
                f"— consult NOVA after D1-D5, not before")
        text = open(nova[-1], encoding="utf-8").read()
        if not JOB_ID_RE.search(text):
            failures.append(f"AC4: {os.path.basename(nova[-1])} has no capture job id")
        if len(text) < 800:
            failures.append(f"AC4: {os.path.basename(nova[-1])} capture too short ({len(text)} chars)")

    if failures:
        for f in failures:
            print(f"FAIL {f}")
        print(f"DEPTH GATE: FAIL ({len(failures)} failures) — do NOT promote {company_id}")
        return 1
    print(f"DEPTH GATE: ALL PASS — {company_id} ran at full depth (4 fragments + NOVA)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
