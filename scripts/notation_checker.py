#!/usr/bin/env python3
"""notation_checker.py -- Symbol & notation consistency checker for lsh-game-paper drafts.

Enforces the user's writing contract (references/latex_notation.md):
  1. vectors are bold upright:  \mathbf{x}   (not \bm, not \boldsymbol)
  2. scalars are math italic:   x, t, v_P
  3. 2-norm is written \| \cdot \|_2  (subscript required)
  4. every player/state symbol used in math should appear in a definition
     (heuristic: symbol must occur in some \dot{...}/= definition line or
     notation paragraph before heavy use)

Usage:
  python notation_checker.py paper.tex [more.tex ...]
Exit 0 = clean, 1 = issues found.

The checker is heuristic by design: it flags candidates for human review
rather than pretending to parse mathematics.
"""
import os
import re
import sys

BOLD_VARIANTS = re.compile(r"\\(bm|boldsymbol|symbf)\b")
NORM_NO2 = re.compile(r"\\\|\s*[A-Za-z\\].*?\\\|(?!\s*_)(?![\w])")
# \dot{\mathbf{x}}-style definition lines: \dot{SYM} = ...
DOT_DEF = re.compile(r"\\dot\{\\mathbf\{([A-Za-z])\}\}")
VECDOT_PLAIN = re.compile(r"\\dot\{([A-Za-z])\}(?![a-z])")
SUBSCRIPTED_VEC = re.compile(r"\\mathbf\{([A-Za-z])\}_\{?([A-Za-z0-9])\}?")

def strip_comments(text):
    return re.sub(r"(?<!\\)%.*", "", text)

def check_file(path):
    text = strip_comments(open(path, encoding="utf-8").read())
    issues = []

    # 1. mixed bold-vector macros
    for m in BOLD_VARIANTS.finditer(text):
        issues.append((m.start(), f"bold-vector macro \\{m.group(1)} used -- contract requires \\mathbf"))

    # 2. norms without explicit 2-subscript (single-token norms only; multi-term
    #    norms like \|\mathbf{x}-\mathbf{y}\| flagged separately below)
    for m in re.finditer(r"\\\|\s*\\?[A-Za-z]+\s*\\\|(?!\s*_\{?2)", text):
        tok = m.group(0)
        if "\\|" in tok and "_2" not in tok and "_{2}" not in tok:
            issues.append((m.start(), f"norm without _2 subscript: {tok}"))

    # 3. plain-italic time derivative of a vector-like state: \dot{x} used while
    #    \dot{\mathbf{x}} also appears elsewhere -> inconsistent style
    has_bold_dot = bool(DOT_DEF.search(text))
    if has_bold_dot:
        for m in VECDOT_PLAIN.finditer(text):
            issues.append((m.start(),
                           f"\\dot{{{m.group(1)}}} inconsistent with bold convention \\dot{{\\mathbf{{{m.group(1)}}}}}"))

    # 4. symbols used before any definition-like occurrence (crude order check)
    body = text
    first_math = body.find("$")
    if first_math != -1:
        math_part = body[first_math:]
        defined = set(DOT_DEF.findall(math_part))
        # also treat \mathbf{x}_P style occurrences as self-evidencing
        for m in SUBSCRIPTED_VEC.finditer(math_part):
            defined.add(m.group(1))
        # frequent single-letter bold symbols should be defined somewhere
        freq = {}
        for m in re.finditer(r"\\mathbf\{([A-Za-z])\}", math_part):
            freq[m.group(1)] = freq.get(m.group(1), 0) + 1
        for sym, n in sorted(freq.items()):
            if n >= 5 and sym not in defined:
                issues.append((first_math,
                               f"\\mathbf{{{sym}}} used {n}x without any \\dot{{\\mathbf{{{sym}}}}}= definition line -- define it in Problem Formulation"))

    # 5. player-letter collision heuristic: both P/E used as players and as
    #    probability/energy elsewhere is the classic clash -- just report counts
    for sym, meaning in (("P", "Pursuer"), ("E", "Evader")):
        n = len(re.findall(r"\b" + sym + r"\b", math_part))
        if n > 60:
            issues.append((first_math,
                           f"'{sym}' occurs {n}x in math -- ensure it is exclusively the {meaning} symbol and never re-used"))

    return issues


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total = 0
    for path in sys.argv[1:]:
        issues = check_file(path)
        print(f"== {os.path.basename(path)}: {len(issues)} issue(s)")
        for pos, msg in issues:
            line = open(path, encoding="utf-8").read()[:pos].count("\n") + 1
            print(f"  L{line}: {msg}")
        total += len(issues)
    sys.exit(0 if total == 0 else 1)


if __name__ == "__main__":
    main()
