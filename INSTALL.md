# Install — lsh-game-paper skill

The repo is a self-contained skill folder. Cloning it into a skills directory is the whole install.

## ZCode

```bash
git clone https://github.com/Nofearli/lsh-game-paper.git ~/.agents/skills/lsh-game-paper
```

Restart ZCode (or start a new session); the skill triggers on differential-game / pursuit-evasion /
paper-writing requests, or can be invoked explicitly.

## From a checkout (bundled scripts)

```bash
bash ./install.sh                                        # macOS / Linux
powershell -ExecutionPolicy Bypass -File .\install.ps1   # Windows
```

Default target is `~/.agents/skills/lsh-game-paper`; pass a custom skills root as the first argument,
or `--force` to overwrite an existing installation.

## Verify

```bash
python scripts/citation_checker.py --check-library   # expect: library audit, 0 fabricated keys
python scripts/simulation_plotting.py                # regenerate demo figures into assets/
```

## Point the indexer at your own PDF folder

`papers/manifest.json` records the original build's PDF folder. To index your own:

```bash
python scripts/paper_indexer.py --pdf-dir /path/to/your/pdfs
```

New PDFs get fresh stable IDs (content-hash dedup); existing archives are never overwritten.
