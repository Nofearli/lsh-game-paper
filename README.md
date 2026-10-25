# lsh-game-paper — a research & paper-writing skill for game-theory (IEEE Transactions)

A knowledge base **and** a working research assistant for differential games, pursuit–evasion,
reach–avoid, target/active defense, perimeter defense, capture-the-flag, lifeline and
reconnaissance games — built from **102 papers read and archived paper-by-paper** (page-level
traceability), with an IEEE Transactions writing system on top.

Every claim the skill makes about a paper is traceable to a per-paper archive with the original
page and equation number. It will tell you "the library does not cover this" instead of guessing.

## What's inside

- **Entry point:** `SKILL.md` (capabilities, triggers, 7 modes A–G, quality red lines, incremental-update flow).
- **Paper archives:** `papers/` — 102 deep-analysis archives (bibliographic info + BibTeX / background /
  problem & gap / contributions / **key mathematical results with page & equation citations** /
  experiments with as-printed parameter tables / limitations / citation value), plus `manifest.json`,
  a cross-index, and compressed digests. ~90 errata & proof gaps found in the source papers are
  recorded with page evidence.
- **Cross-paper knowledge:** `references/` (18 files) — theory compendium (Apollonius, Cartesian ovals,
  barriers, HJI/viscosity, PMP, equilibrium concepts…), 6 barrier recipes with a proven-vs-asserted
  scorecard, 14 proof patterns, 14 problem-class modeling profiles, symbol-conflict table, strategy &
  algorithm patterns, experiment-design mapping, hardware-experiment compendium, figure standards,
  Introduction patterns, related-work taxonomy, IEEE style, novelty-analysis workflow, reviewer
  checklist, and the full BibTeX compilation.
- **Working code:** `scripts/` — incremental PDF indexer, anti-fabrication citation checker,
  notation-consistency checker, IEEE-style plotting helpers. `assets/` holds generated example figures.
- **Templates:** `templates/` — Introduction / problem formulation / theorem-proof / algorithm (.tex) /
  simulation / conclusion / three-line tables.
- **Acceptance record:** `BUILD_REPORT.md` (what was processed, verification results, known limitations).

## The 7 modes

| Mode | When to use | Output |
|---|---|---|
| A · Literature research | related work, "what should I cite" | verified recommendation list + BibTeX + citation slots |
| B · Problem modeling | formulate a new game | modeling profile + inheritable-assumption analysis |
| C · Theory & proof check | theorems, barriers, conjectures | proof chain + assumption-inheritance audit |
| D · Paper writing | Abstract/Intro/Results/Conclusion | section drafts with per-paragraph purpose |
| E · Simulation design | validate a theorem | experiment matrix + IEEE-style figures |
| F · Review check | pre-submission review | Critical/Major/Minor report |
| G · Full-paper co-writing | from scratch | blueprint → chapters → final consistency check |

**Quality red lines (enforced in every mode):** never fabricate papers/DOIs/pages; distinguish
*proven* vs *asserted*; separate source facts, cross-paper synthesis, and advice; simulations never
count as proofs.

## Install

The repo **is** the skill folder — cloning it into a skills directory is the whole install.

```bash
# ZCode (cross-tool location)
git clone https://github.com/Nofearli/lsh-game-paper.git ~/.agents/skills/lsh-game-paper

# Windows PowerShell
git clone https://github.com/Nofearli/lsh-game-paper.git "$env:USERPROFILE\.agents\skills\lsh-game-paper"
```

**Or use the bundled script** (from a checkout):

```bash
bash ./install.sh              # macOS / Linux  -> ~/.agents/skills/lsh-game-paper
powershell -ExecutionPolicy Bypass -File .\install.ps1   # Windows
```

**Update later:** `cd ~/.agents/skills/lsh-game-paper && git pull`

## Quick check

```bash
python scripts/citation_checker.py --check-library   # library audit (bibliographic integrity)
python scripts/paper_indexer.py --help               # incremental indexing of new PDFs
```

## Adding new papers

Drop the PDF into your literature folder, run `python scripts/paper_indexer.py --pdf-dir <folder>`
(stable IDs, content-hash dedup), then write the new archive from `papers/_TEMPLATE.md` — existing
knowledge is never overwritten.

## Provenance & scope

Archives summarize and quote from published papers with full citation and page/equation traceability
for research use; no PDF full texts are included in this repository. The `manifest.json` venue field
is an automatic first guess — the authoritative bibliographic record is each archive's Section 1
(corrections are logged there).

## License

MIT — see [LICENSE](LICENSE).
