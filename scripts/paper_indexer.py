#!/usr/bin/env python3
"""paper_indexer.py -- Build and incrementally maintain the lsh-game-paper manifest.

Scans a directory of game-theory PDFs, extracts bibliographic metadata
(title / authors / year / venue / DOI / page count), assigns quality tiers,
and writes:
  <skill>/papers/manifest.json   -- machine-readable master list (incremental, hash-keyed)
  <skill>/papers/index.md        -- human-readable index with archive status

Incremental contract: an existing manifest is preserved; papers are keyed by
content hash so renamed files keep their ID, and newly added PDFs receive the
next free ID. Existing archive files (papers/PXXX.md) are never touched.

Usage:
  python paper_indexer.py [--pdf-dir DIR] [--skill-dir DIR]
"""
import argparse
import hashlib
import json
import os
import re
import sys

import pymupdf

DEFAULT_PDF_DIR = r"D:\System\zhuomian\lsh-game-paper"
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIER1_JOURNAL = [
    r"IEEE\s+TRANSACTIONS?\b", r"IEEE/ASME\s+TRANSACTIONS", r"IEEE\s+TRANSACTIONS",
    r"IEEE\s+CONTROL\s+SYSTEMS\s+LETTERS", r"IEEE/CAA\s+JOURNAL", r"IEEE\s+OPEN\s+JOURNAL",
    r"\bAutomatica\b", r"IEEE\s+Robotics\s+and\s+Automation\s+Letters",
]
TIER2_CONF = [
    r"American\s+Control\s+Conference|\(ACC\)", r"Conference\s+on\s+Decision\s+and\s+Control|\(CDC\)",
    r"European\s+Control\s+Conference|\(ECC\)", r"Robotics\s+and\s+Automation|\bICRA\b|\bIROS\b",
    r"AAAI", r"AIAA\b|SciTech|Guidance,\s*Navigation", r"ICUAS",
]
TIER2_JOURNAL = [
    r"Nonlinear\s+Dynamics", r"Neurocomputing", r"Ocean\s+Engineering",
    r"Chinese\s+Journal\s+of\s+Aeronautics", r"SCIENCE\s+CHINA|Science\s+China",
    r"International\s+Journal\s+of\s+Control|Guidance,\s*Navigation\s+and\s+Control",
    r"European\s+Journal\s+of\s+Control", r"IET\s+Control\s+Theory",
    r"Unmanned\s+Systems", r"Advanced\s+Intelligent\s+Systems", r"IEEE\s+Access",
    r"Journal\s+of\s+Intelligent\s+&?\s*Robotic", r"Aerospace\s+Science\s+and\s+Technology",
    r"Frontiers", r"Expert\s+Systems", r"Aerospace\s+Systems", r"Nonlinear\s+Dyn",
]
LOW_TIER = [
    r"Chinese\s+Control\s+Conference|\(CCC\)|Chinese\s+Automation|CCDC",
    r"IECON|ICCA|NAECON|\(CCTA\)|FASTA|\(SMC\)|Chinese\s+Guidance",
    r"Electronic\s+Research\s+Archive|Missiles\s+and\s+Space",
    r"International\s+Journal\s+of\s+Aerospace\s+Engineering|Advances\s+in\s+Astronautics",
    r"MDPI|mdpi\.org|Licensee\s+MDPI",
]
ARXIV = re.compile(r"arxiv\.org|arXiv:\s*\d{4}\.\d+", re.I)
THESIS = re.compile(r"学位论文|学校代码|学\s*号|申请.*博士|硕士学位论文")

DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"<>]+", re.I)
YEAR_RE = re.compile(r"(19|20)\d{2}")
ZOTERO_RE = re.compile(r"^(?P<authors>.+?)\s+-\s+(?P<year>(19|20)\d{2})?\s*-?\s*(?P<title>.+)\.pdf$")
IEEE_TR_RE = re.compile(r"IEEE\s+TRANSACTIONS?\s+ON\s+([A-Z/\s,&-]+)", re.I)


def file_md5(path, chunk=1 << 20):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()


def largest_font_lines(doc, max_pages=1):
    """Return text lines with the largest font size on the first page(s)."""
    best, out = 0.0, []
    for pno in range(min(max_pages, doc.page_count)):
        try:
            d = doc[pno].get_text("dict")
        except Exception:
            continue
        for block in d.get("blocks", []):
            for line in block.get("lines", []):
                text = "".join(s.get("text", "") for s in line.get("spans", [])).strip()
                if not text or len(text) < 4:
                    continue
                size = max((s.get("size", 0) for s in line.get("spans", [])), default=0)
                if size > best + 0.5:
                    best, out = size, [text]
                elif abs(size - best) <= 0.5 and text not in out:
                    out.append(text)
    return out, best


def parse_meta(path):
    name = os.path.basename(path)
    meta = {"file": name, "title": None, "authors": None, "year": None,
            "venue": None, "venue_raw": "", "doi": None, "type": "article",
            "tier": None, "pages": None, "notes": []}

    m = ZOTERO_RE.match(name)
    if m and not m.group("title").lower().endswith(("pdf",)):
        meta["authors"] = m.group("authors").strip()
        meta["year"] = m.group("year")
        meta["title"] = m.group("title").strip()

    try:
        doc = pymupdf.open(path)
    except Exception as e:
        meta["notes"].append(f"OPEN_FAIL: {e}")
        return meta
    meta["pages"] = doc.page_count
    head = "\n".join(doc[p].get_text("text") for p in range(min(2, doc.page_count)))

    if doc.metadata.get("title") and len(doc.metadata["title"]) > 12 and not name.startswith(doc.metadata["title"][:8]):
        meta["title"] = meta["title"] or doc.metadata["title"].strip()

    if not meta["title"]:
        lines, _ = largest_font_lines(doc)
        cand = " ".join(lines[:2]).strip()
        if len(cand) >= 10:
            meta["title"] = re.sub(r"\s+", " ", cand)
    doc.close()

    if not meta["year"]:
        years = YEAR_RE.findall(head)
        if years:
            meta["year"] = years[-1]
    dm = DOI_RE.search(head)
    if dm:
        meta["doi"] = dm.group(0).rstrip(".,;)")

    def matched(patterns):
        for p in patterns:
            mm = re.search(p, head, re.I)
            if mm:
                return mm.group(0)
        return None

    if THESIS.search(head):
        meta["type"], meta["tier"], meta["venue"] = "thesis", "T3", "PhD/MSc Thesis"
        return meta
    tr = IEEE_TR_RE.search(head)
    if tr:
        meta["type"], meta["tier"], meta["venue"] = "article", "T1", "IEEE Trans on " + tr.group(1).strip()
        return meta
    if matched(TIER1_JOURNAL):
        meta["type"], meta["tier"], meta["venue"] = "article", "T1", matched(TIER1_JOURNAL)
        return meta
    if ARXIV.search(head):
        meta["type"], meta["tier"], meta["venue"] = "preprint", "T2", "arXiv"
        return meta
    if matched(TIER2_CONF):
        meta["type"], meta["tier"], meta["venue"] = "conference", "T2", matched(TIER2_CONF)
        return meta
    if matched(TIER2_JOURNAL):
        meta["type"], meta["tier"], meta["venue"] = "article", "T2", matched(TIER2_JOURNAL)
        return meta
    low = matched(LOW_TIER)
    if low:
        meta["type"], meta["tier"], meta["venue"] = "article", "T3", low
        return meta
    meta["tier"] = "T3"
    meta["notes"].append("VENUE_UNRESOLVED")
    return meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-dir", default=DEFAULT_PDF_DIR)
    ap.add_argument("--skill-dir", default=SKILL_DIR)
    args = ap.parse_args()

    papers_dir = os.path.join(args.skill_dir, "papers")
    os.makedirs(papers_dir, exist_ok=True)
    manifest_path = os.path.join(papers_dir, "manifest.json")

    old = {"papers": []}
    if os.path.exists(manifest_path):
        with open(manifest_path, encoding="utf-8") as f:
            old = json.load(f)
    by_hash = {p["hash"]: p for p in old.get("papers", []) if p.get("hash")}
    by_name = {p["file"]: p for p in old.get("papers", []) if p.get("file")}
    used_ids = {p["id"] for p in old.get("papers", []) if p.get("id")}
    next_num = max((int(i[1:]) for i in used_ids), default=0) + 1

    pdfs = sorted(f for f in os.listdir(args.pdf_dir) if f.lower().endswith(".pdf"))
    papers, new_ids = [], 0
    for fname in pdfs:
        fpath = os.path.join(args.pdf_dir, fname)
        h = file_md5(fpath)
        # filename match first so that identical-content files keep their own IDs
        if fname in by_name:
            p = dict(by_name[fname])
        elif h in by_hash:
            p = dict(by_hash[h])
            p["file"] = fname  # renamed file keeps its ID
        else:
            p = parse_meta(fpath)
            p["id"] = "P%03d" % next_num
            next_num += 1
            new_ids += 1
        p["hash"] = h
        p["archive"] = os.path.exists(os.path.join(papers_dir, p["id"] + ".md"))
        papers.append(p)

    papers.sort(key=lambda p: p["id"])
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({"pdf_dir": args.pdf_dir, "count": len(papers), "papers": papers},
                  f, ensure_ascii=False, indent=1)

    # human-readable index
    rows = []
    for p in papers:
        title = (p.get("title") or "?")[:80]
        ven = (p.get("venue") or "?")[:32]
        yr = p.get("year") or "?"
        mark = "x" if p["archive"] else " "
        rows.append(f"| {p['id']} | {mark} | {p['tier']} | {p['type'][:4]} | {yr} | {ven} | {title} | `{p['file']}` |")
    with open(os.path.join(papers_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("# lsh-game-paper Literature Index\n\n")
        f.write(f"Source: `{args.pdf_dir}` -- {len(papers)} PDFs, {new_ids} newly indexed.\n\n")
        f.write("Archive column: `x` = papers/PXXX.md exists.\n\n")
        f.write("| ID | Arch | Tier | Type | Year | Venue | Title | PDF file |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        f.write("\n".join(rows) + "\n")

    done = sum(1 for p in papers if p["archive"])
    print(f"indexed={len(papers)} new={new_ids} archives_done={done}")
    unresolved = [p["id"] + " " + p["file"] for p in papers if "VENUE_UNRESOLVED" in p.get("notes", [])]
    if unresolved:
        print("venue unresolved:", *unresolved, sep="\n  ")


if __name__ == "__main__":
    sys.exit(main())
