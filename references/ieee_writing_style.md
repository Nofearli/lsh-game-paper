# IEEE Transactions Writing Style — Language and Structure Norms for Game Papers

Distilled (**[归纳]**) from the bibliographic records (Section 1), contribution records
(Section 4), and limitation/errata records (Section 7) of the T1 archives in `papers/PXXX.md`
— 19 archives read in full (P013, P019, P021, P022, P037, P040, P046, P050, P053, P054, P059,
P077, P090, P091, P099, P100, P103, P105, P106) plus the complete digest set (which supplies
the P011/P027/P028/P067/P095 errata records and the remaining cells of the taxonomy). General IEEE Trans conventions are included only where the archives evidence them.
Skeletons are NOT duplicated here — use `templates/templates_overview.md` for the seven
section templates; this file supplies the norms that govern any instantiation of them.

**Anti-plagiarism rule (binding):** paraphrase everything; never lift sentences from source
papers or from the archives. Facts claimed about a specific paper must be checked against its
`PXXX.md` archive before use (red line 1 of `SKILL.md`); mark synthesis as [归纳] and new
advice as [建议].

---

## 1. Section-structure variants observed in the library

### 1.1 IEEE Transactions variant (TAC / TAES / TCYB / TRO / TCST / TSMC / TII)
Canonical order, roman-numeral sections:
I. Introduction (contributions listed at its end) → II. Problem Formulation / Preliminaries →
III–IV. Main Results → V. Extensions / Algorithm / Simulations → VI. Conclusion.
Archive evidence and variations:
- P022 (TAC): theory-only paper — no simulation section; verification is the HJI check, the C1
  argument, and a root-existence proof. A pure-theory TAC paper without numerics is viable
  when every claim carries an analytic proof.
- P037 (TAC): III = main theorems, IV = implementation/enumeration, V = one computational
  example (a timing table), VI = conclusion; trajectory-level robustness deferred to the
  extended arXiv version — acceptable, but the archive flags the transparency cost.
- P050 (TAC): II problem statement, III main results (value + verification), IV strategies and
  partition, V single 3-D example, VI conclusion.
- P054 (TAC): four-subproblem decomposition (P1–P4) structures the entire paper; simulations
  have lettered subsections (A: 1-on-1 validation, B: allocation benchmark vs. baselines,
  C: full 8-vs-10 game, D: dynamic variant).
- P106 (TAC): three winning modes (onsite / goal-visible / nongoal-visible) each get a theorem
  and a dedicated simulation case; the case-to-claim mapping is made explicit in the text.

### 1.2 Automatica variant
Arabic-numbered sections (1. Introduction, 2. Problem statement, …), section-prefixed result
numbers (Theorem 3.2), inline Remarks, no organization paragraph (P021, P103). Length regimes:
Brief papers ≤ ~10 printed pages (P031: 10 pp.; P113: 9 pp.); regular papers 12–14 pages
(P021: 13 pp.; P103: 11 pp. + appendix). A printed generative-AI-use statement is now part of
the front matter (recorded for P021).

### 1.3 Internal ordering: game of kind vs. game of degree
Two legitimate orderings, both attested:
- **Kind first** (the geometric school default): barrier/winning regions, then optimal target
  points and strategies inside each region — P099, P100, P103, P091, P105, P058.
- **Degree first** (when the kind answer is *needed* to state the degree problem): P022 solves
  the Game of Degree (Theorems 1–2) inside the escape region and derives the barrier
  (Theorem 3) afterwards, explicitly declaring "the Game of Kind assumed solved" in Theorem 2's
  statement.
**[归纳] Rule:** whichever order, the dependency must be explicit in the theorem statement
("with x ∈ R_e", "in the defender winning region W_D"), never implicit.

### 1.4 Placement of contributions
Numbered contributions at the end of Section I are near-universal: recorded verbatim conventions
include "Our contributions are threefold" (P017, ACC but representative), seven items (P103),
six (P053), five (P054, P106), four (P050). Each item names its deliverable (theorem, algorithm,
complexity result, or experiment) — see `introduction_patterns.md` Section 1.4.

---

## 2. Abstract and Conclusion formulas [建议 — consistent with library records]

The archives record contributions and conclusions rather than abstract prose, so these formulas
are recommended patterns consistent with the recorded content, not quotations.

**Abstract (150–250 words, single paragraph, no citations):**
1. One sentence naming the problem class and setting (players, information structure, geometry).
2. One to two sentences stating the method ("We construct analytical barriers…", "We prove the
   value function is the viscosity solution…").
3. One to two sentences with the headline guarantees, quantified against the adversary and
   carrying the paper's identity numbers ("at most two pursuers are necessary" — P100/P105;
   "a nondecreasing guaranteed capture count" — P106; "0.41 s for 16 barriers" — P091).
4. One sentence of validation ("Monte-Carlo studies and hardware experiments on a six-MAV
   platform…" — P059-style), or explicitly none for theory papers.
Calibration rule from the archives: every quantitative adjective in the abstract must survive
Section 7 scrutiny — P046's "model-free" and P077's "analytical solution" both draw archive
errata because the body supports only weaker claims.

**Conclusion (0.5–1 column, no new results):**
1. One-paragraph recap of what was proved, in the past-or-present declarative, matching the
   contribution list one-to-one.
2. Honest limitations — the strongest T1 papers volunteer them here (P054: "we are unable to
   provide the complete proof yet"; P019: focal surfaces "left as future work").
3. Three to five future-work items, each concrete enough to name a model class (P021: more
   target regions, slower defenders, non-convex targets; P059: onboard/distributed LLM,
   richer dynamics).

---

## 3. Theorem, assumption, and remark machinery

### 3.1 Numbering conventions
- **IEEE Trans — global sequential numbering** across the whole paper: Definition 1–4, Lemma
  1–6, Proposition 1–2, Theorem 1–6, Corollary 1–3, Remark 1–9, Assumption 1–2 (attested in
  P050, P053, P054, P046, P106, P022). Equations numbered (1), (2), … in order of appearance;
  proofs cite equations by number, never by "above".
- **Automatica — section-prefixed numbering**: Definition 2.1, Lemma 3.1, Theorem 3.2, Remark
  3.2, Assumption 2.1–2.2 (attested in P103, P021).
- **Assumptions** are lettered or numbered, stated once, and *restated inside theorem
  statements* that depend on them (P022 restates "DT ≤ AT and x ∈ R_e" in Theorem 2; P031 uses
  A1–A5 referenced throughout; P054's Assumption 1 is the load-bearing speed condition).
- **Remarks** carry interpretation, degenerate cases, and comparison to prior work — the
  library's remarks routinely do triple duty (P050's Remarks 1–7; P054's Remarks 2–5, including
  the complexity remark).

### 3.2 Statement hygiene (the pattern the errata punish when violated)
- Every theorem statement is self-contained: game objects by their equation numbers, all
  assumptions inline, the conclusion quantified ("for all x in …", "for any admissible
  evader strategy").
- Constants of the statement are defined *before* the theorem or in its preamble, never inside
  the proof (P091's "polynomial constants" s*_j, s_k that are actually implicit roots draw an
  archive flag for exactly this).
- Proofs end with a tombstone or an explicit closing sentence; a proof woven into surrounding
  text without a marker is anomalous (flagged for P021, Theorem 8).
- Deferred proofs must be pointed to explicitly ("proof in the extended version [35]", P037) —
  silent deferral is an archive-flagged defect (P037's Theorem 3 and Corollary 1).

### 3.3 The verification idiom
The library's highest-value sentence pattern, attested in P019, P022, P031, P050, P053, P054:
construct a candidate value geometrically, then prove it is *the* (unique viscosity or classical
C1) solution of the HJI equation, including behavior on singular surfaces. The full-claim form
requires: continuity, differentiability/subdifferential characterization, HJI satisfaction, and
boundary-condition match (P050's Theorem 2 performs all four steps). Partial forms must be
named honestly: "satisfies the HJI equation on the smooth region" (P103's stated scope) is
acceptable; omitting the caveat is not (P037's asserted-but-deferred HJI claim is flagged).

---

## 4. Notation style (summary; full system in `latex_notation.md`)

- Vectors bold upright ($\mathbf{x}$), scalars italic ($x$, $t$, $\alpha$), norms
  $\|\cdot\|_2$, sets calligraphic ($\mathcal{W}$, $\mathcal{T}$, $\Omega$). Every symbol
  defined at first use (checked by `scripts/notation_checker.py`).
- **Player names** — pick one family per paper and keep it: P_i/E_j (P054, P100, P103) or
  D_i/A_j/T (P022, P091, P050). Cross-paper variation is fine; intra-paper mixing is an errata
  class (P091's subscript mismatches).
- **Speed ratio** — α dominates (P022, P099, P100, P103); variants ν_i (P048/P050), ξ_i
  (P021), λ_i (P013). If λ is the ratio, costates must move to another symbol and vice versa.
- **Capture radius** — r_i, ρ_i, ε_i, ℓ all attested; within one paper choose one and do not
  collide with perturbation/slack parameters (P053's ϵ̄ = ϵ + δ is a documented, deliberate
  exception).
- **Regions** — Ω_goal/Ω_play/Ω_tar for target and play regions; T (or 𝒯) for the target
  line/set; W_P, W_D (or 𝒲) for winning regions; R_e, R_c (P022) for escape/capture; B or 𝓑
  for the barrier; V for the value; H for the Hamiltonian.
- A "Notation" paragraph or table early in Section II is common in long multiplayer papers
  (P037, P103) and pays for itself — the archives flag P037's state-ordering inconsistency
  (pursuers-first in Sec. II, evaders-first in Sec. III) as a direct cost of skipping it.

---

## 5. Tense, voice, and person

Scope this section before applying it. The bullets below are `[归纳·档案]`: they were induced
from the 102 deep-read archives, whose T1 records are weighted toward theory-forward work
(TAC-style geometric and viscosity-solution prose). Application venues behave differently, and
the difference is measurable rather than a matter of taste.

- **Present tense** for the paper's own actions and mathematical truth: "we construct", "we
  prove", "the value is the viscosity solution", "capture is guaranteed", "the barrier consists
  of three arcs". `[归纳·档案]`
- **Present tense also for literature**: "Chen et al. formulate …", "Yan et al. construct …" —
  the archives' records of T1 prose consistently use the historic present for cited work; past
  tense is reserved for dated events ("was introduced at Allerton 2014", P022's background).
  `[归纳·档案]` — but see the counter-evidence below before using this in an application paper.
- **Mixed voice**: active "we" for choices and proofs; passive for mathematical facts and
  procedures ("is computed at every sampling step", "is obtained by"). First-person singular
  does not occur; imperatives do not occur. `[归纳·档案]`
- "In this paper, we …" opens the contribution paragraph; "This paper" may open sentences
  elsewhere ("This paper is the journal-length, rigorous treatment…" is the archive's
  paraphrase of P022's self-positioning move). `[归纳·档案]`

### 5.1 Counter-evidence from application venues `[实测·7篇]`

`lsh-ieee-trans-style` re-measured the body prose of 7 papers in TCST / TIE / T-Mech / TAES /
TII / TSMC:S (39,589 words, 1,265 prose sentences; 2 of them are reach-avoid papers already
archived here). Three findings contradict the bullets above for this venue group:

| Claim above | Measured in the 7-paper application corpus |
|---|---|
| active "we" for choices and proofs | `we` 4 and `our` 4 occurrences total (0.10 per 1k words); `We + verb` sentence leads: 2 of 1,265. Agency is carried instead by `one can` (84), `can be` (179), passive be+past participle (629) |
| present tense for cited work | other work appears as past passive: `was/were proposed` 10 times, `In [n], …` 108 times, past participle + `in [n]` 15 times |
| "In this paper, we …" opens contributions | the frame is `The main contributions of this paper are summarized as follows:` + `1) 2) 3)` (`as follows` 44, `1)` 63, `first,/second,/third,` 23), with the bullets themselves in the passive |

Also measured, and not derivable from either rule set: a bracketed reference **never** acts as
the clause subject in this corpus (0 occurrences) — `[12] proposes …` is the ML-venue habit, not
the IEEE control-venue one; `the proposed X` never co-refers with a citation (0 occurrences), so
it marks the paper's own object only; and connectors `to this end`, `in particular`,
`it is worth noting` occur **0** times, while `then` / `therefore` / `however` carry the turns.

**[归纳] Rule:** pick by venue, not by habit. Theory-forward TAC-lineage prose follows §5.
Application-venue prose (TCST, TIE, T-Mech, TAES, TII, TSMC:S) follows §5.1, and should be
checked mechanically with `lsh-ieee-trans-style/scripts/style_checker.py` before submission.
When the two disagree, the archive-derived bullets describe what the archived papers did, not
what a reviewer at an application venue will expect.

---

## 6. Hedging vs. claiming norms

1. **Quantify the adversary inside the claim.** Guarantees are stated as "for any admissible
   evader strategy", "regardless of the opponent's control", "against any strategy of E_j"
   (P023's containment law; P106's Definition 1; P097's capture certificate). A guarantee
   without the adversarial quantifier is not a game-theoretic claim.
2. **Hedge novelty exactly once**: "to the best of the authors' knowledge" (P059, P040) or
   "as far as the authors are aware" (P053). Repeating it dilutes; omitting it turns a
   plausible gap into an unprovable impossibility claim.
3. **Scope claims to the setting**: name the assumptions in the claim sentence itself when they
   are load-bearing (P050's verification holds where LICQ holds — the paper says so; P019's
   value is assembled locally near singular boundaries — the paper says so).
4. **Prove or simulate every negative claim**: P019's demonstration that the naive max-value
   fails (a constructed set Υ₂ plus numerics) is the model; "X is not possible" without a
   construction is not attested anywhere in the library's T1 records (the competitive thread
   P005–P009 proves impossibility by explicit adversarial input constructions).
5. **Match evidence strength to claim strength**: "asserted but not demonstrated" is the exact
   defect the archives record for P022's implementability remark and P091's real-time
   superiority (no numerical baseline was run). Either add the experiment or weaken to
   "by construction".
6. **Author-claims vs. verified**: when summarizing prior work, distinguish what the cited
   paper claims from what has been checked — this skill's archives do it with [authors'
   claim]/[verified] tags; a paper does the same by attributing characterizations ("[12] uses
   pairwise outcomes" vs. "we verified") and never quoting rendered limitations of other papers
   as facts.

---

## 7. Safe phrases vs. clichés

**Safe (evidence-bearing, attested patterns):** "admits a closed-form solution"; "is the
viscosity solution of the HJI equation"; "guarantees capture in finite time"; "at most k
pursuers are necessary"; "without solving any PDE"; "with a nondecreasing guaranteed capture
count"; "computed in 0.412 s for 16 barriers"; "the proof is deferred to the extended version".
**Clichés / red flags (all attested as errata or archive-flagged weaknesses):** "the simulation
results verify the effectiveness of the proposed method" (used where no baseline exists —
flagged for P013, P103, P106, P077, P091); "significantly outperforms existing methods"
(unquantified); "comprehensive experiments" for a single scenario (P050 tested one initial
condition); "real-time capable" without timing; "model-free" with a known input matrix (P046);
"optimal" for geometrically constructed strategies without an equilibrium verification (P100,
P091 flagged); "guaranteed" attached to a heuristic (P059's approximation ratio is explicitly
"inferred", not proved).

---

## 8. Errata checklist — what the archives' Section 7 records show reviewers catch

Use as a pre-submission pass; each item is a real defect recorded in a library archive.

**A. Symbol and typography slips**
- Swapped or inconsistent parameters: P099 (h/l horizontal-vs-vertical swap; an appendix
  case-header sign flipped relative to its own figure); P011 (t_A vs. t̄_A for one quantity);
  P095 (target-sensing-region subscript r_0+ρ_I vs. r_0+ρ_T); P067 (Ω_play/Ω_tar swapped in a
  prose sentence); P028 (evader speed v_I vs. v_E; "pursers" for "pursuers").
- Wrong symbol in a display: P013 ((y−y_O)² printed where (z−z_O)² belongs); P021 (E ⊂ N for
  [n]; η printed as k; g* for W*); P053 (‖u*_e‖ = u_pm for v_em; a sign typo in the
  superiority threshold (22) that contradicts the paper's own classification); P091 (ρ₃ for
  ρ₆ in a parameter table).
- Residual template text: P013 ("AUTHOR ET AL.: SHORT ARTICLE TITLE", "VOL. XX" left in the
  early-access build); "UVA" for "UAV".
- Punctuation/wording: P059 ("Z+ … nonpositive integers"; a garbled complexity sentence;
  "assigned with at to one"); P021 ("generation" for "generalization"); P091 (duplicated
  sentence; "relative ordinate (x-coordinate)").
**B. Structural and cross-reference defects**
- State-ordering inconsistency across sections (P037); leftover shorter-case state vector in a
  general formulation (P037); table rows missing entries (P037, Table I); undefined matrices in
  theorem hypotheses (P090's Ω, S_Ξ); a coalition-count formula that is impossible as typeset
  (P105); citations numbered inconsistently for the same work (P077: relay pursuit as [16] in
  one section, [1] in another); a key lemma argued by pointing at a figure rather than a proof
  (P103, Lemma 3.3).
**C. Claim–evidence mismatches (the class reviewers weight most)**
- Abstract broader than body: P046 ("model-free" while the input matrix is used throughout);
  P077 ("analytical solution" holds strictly only for one pursuer).
- Hidden load-bearing assumptions behind "general" claims: P050 ("no restrictive assumptions"
  while defender speed superiority ν_i > 1 drives every proof).
- Optimality claimed without equilibrium verification: P100 (barrier not certified against the
  HJI barrier; nonanticipative information asymmetry), P091 (no Isaacs verification; the most
  novel scenario never simulated).
- Steps asserted, not derived: P054 (Lemma 1–2 proofs omitted); P019 (Υ₂ nonemptiness asserted
  from numerics); P022 (which quartic root defines the aim point left implicit; squaring may
  introduce extraneous roots); P053 (a barrier invariance step that holds only instantaneously);
  P106 (finitely-many-point checks presented as conditions); P059 (approximation ratio
  "inferred").
**D. Reproducibility gaps**
- Unreported parameters/platforms: speeds, radii, solvers, integrators UNREPORTED in P103,
  P106, P050, P021, P077, P019. The T1 norm the archives reward (P037's timing table; P054's
  full parameter tables; P059's hardware table) is: every scenario reproducible from printed
  numbers.

---

## 9. Pre-submission language checklist [建议]

1. Every claim sentence carries its adversarial quantifier and its assumptions.
2. Novelty hedged once; gap statement supported by the preceding related-work sentences.
3. Contributions one-to-one with theorems/algorithms/experiments; verbs name deliverables.
4. One player-naming family, one ratio symbol, one radius symbol; all defined at first use.
5. Theorem statements self-contained; deferred proofs pointed to explicitly.
6. Verification idiom complete or honestly scoped (smooth-region-only claims labeled as such).
7. No cliché evidence phrases; every quantitative adjective traceable to a table or theorem.
8. Abstract claims survive the Section 8C test (no claim broader than the body).
9. All scenarios reproducible from printed parameter tables; platforms and solvers named.
10. Symbols, citations, and cross-references machine-checked (`citation_checker.py`,
    `notation_checker.py`) and the full pass of `references/reviewer_checklist.md` completed.
