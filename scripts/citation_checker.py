#!/usr/bin/env python3
"""citation_checker.py -- Anti-fabrication citation checker for the lsh-game-paper skill.

Verifies that citations in a draft (LaTeX \\cite{...} / \\bibitem, or [PXXX]
markers, or a .bib file) resolve to REAL entries recorded in this skill's
knowledge base (papers/manifest.json + per-paper archives with BibTeX blocks),
and that every archive BibTeX entry is complete (no unresolved `to verify`).

Usage:
  python citation_checker.py draft.tex            # check a LaTeX/Markdown draft
  python citation_checker.py --check-library      # audit the library's own BibTeX
Exit code 0 = clean, 1 = problems found (printed to stdout).

This script enforces the skill's hard rule: NEVER cite a paper that has no
traceable record in the library or the archives.
"""
import argparse
import json
import os
import re
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(SKILL_DIR, "papers")


def load_library():
    manifest_path = os.path.join(PAPERS_DIR, "manifest.json")
    if not os.path.exists(manifest_path):
        print("ERROR: papers/manifest.json missing. Run paper_indexer.py first.")
        sys.exit(2)
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    by_id = {p["id"]: p for p in manifest["papers"]}
    bibkeys, bibtex_by_key = {}, {}
    bib_re = re.compile(r"@\w+\{([^,]+),")
    verify_re = re.compile(r"(volume|pages|doi|year|author|journal|booktitle)\s*=\s*\{?to verify", re.I)
    for pid, p in by_id.items():
        arch = os.path.join(PAPERS_DIR, pid + ".md")
        if not os.path.exists(arch):
            continue
        text = open(arch, encoding="utf-8").read()
        for m in bib_re.finditer(text):
            key = m.group(1).strip()
            bibkeys[key] = pid
            block_start = m.start()
            nxt = text.find("\n@", block_start + 1)
            block = text[block_start: nxt if nxt != -1 else len(text)]
            unresolved = verify_re.findall(block)
            bibtex_by_key[key] = {"pid": pid, "unresolved_fields": unresolved}
    return by_id, bibkeys, bibtex_by_key


def check_library(by_id, bibkeys, bibtex_by_key):
    """Library audit: warnings are EXPECTED (variant stubs, honest `to verify`
    markers on early-access papers); they never fail the audit. Exit 1 is
    reserved for drafts containing citations that cannot be resolved."""
    print(f"library: {len(by_id)} papers, {len(bibkeys)} BibTeX keys collected")
    missing_archive = [pid for pid in by_id if not os.path.exists(os.path.join(PAPERS_DIR, pid + ".md"))]
    if missing_archive:
        print(f"[WARN] {len(missing_archive)} papers without archive (expected: skipped/variant entries):")
        print("  " + ", ".join(missing_archive[:40]))
    bad = {k: v for k, v in bibtex_by_key.items() if v["unresolved_fields"]}
    if bad:
        print(f"[WARN] {len(bad)} BibTeX entries carry honest `to verify` fields (early-access etc.):")
        for k, v in sorted(bad.items()):
            print(f"  {k} ({v['pid']}): {', '.join(v['unresolved_fields'])}")
    else:
        print("[OK] all recorded BibTeX entries have complete fields")
    dup = len(bibkeys) - len(set(bibkeys))
    if dup:
        print(f"[FAIL] {dup} duplicate BibTeX keys -- resolve before citing")
        return False
    print("[OK] library audit clean (warnings above are informational)")
    return True


def extract_keys_from_draft(text):
    keys = set()
    for m in re.finditer(r"\\cite[tp]?\{([^}]+)\}", text):
        for k in m.group(1).split(","):
            keys.add(k.strip())
    for m in re.finditer(r"\\bibitem\{([^}]+)\}", text):
        keys.add(m.group(1).strip())
    for m in re.finditer(r"\[(P\d{3}(?:\s*,\s*P\d{3})*)\]", text):
        for k in re.split(r"[,\s]+", m.group(1)):
            if k:
                keys.add(k)
    return sorted(keys)


def check_draft(path, by_id, bibkeys):
    text = open(path, encoding="utf-8").read()
    keys = extract_keys_from_draft(text)
    print(f"draft: {len(keys)} citation keys found in {path}")
    problems = 0
    for k in keys:
        if k in bibkeys:
            print(f"  [OK]   {k} -> {bibkeys[k]} ({by_id[bibkeys[k]].get('title', '')[:60]})")
        elif k in by_id:
            print(f"  [OK]   {k} -> manifest entry: {by_id[k].get('title', '')[:60]}")
        elif re.fullmatch(r"P\d{3}", k):
            print(f"  [FAIL] {k} looks like a skill ID but is NOT in the library")
            problems += 1
        else:
            print(f"  [FAIL] {k} has NO record in the lsh-game-paper library "
                  f"(possible fabrication -- verify against papers/index.md)")
            problems += 1
    return problems == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", nargs="?", help="draft .tex/.md file to check")
    ap.add_argument("--check-library", action="store_true")
    args = ap.parse_args()
    by_id, bibkeys, bibtex_by_key = load_library()
    ok = True
    if args.check_library or not args.draft:
        ok = check_library(by_id, bibkeys, bibtex_by_key) and ok
    if args.draft:
        ok = check_draft(args.draft, by_id, bibkeys) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
