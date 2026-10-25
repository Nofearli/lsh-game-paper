# IEEE Transactions Paper Templates -- lsh-game-paper skill

All templates below are skeletons to be instantiated with REAL content from the
knowledge base (`references/`, `papers/`). Never leave a slot unfilled in a
delivered draft; never invent citations -- pull them from `papers/PXXX.md`
archives (BibTeX blocks) only.

---

## 1. Introduction template (references/templates/introduction.md)

Structure proven across TAC/TAES/TCYB/Automatica game papers in the library:

```
[Para 1 -- Context & application]  <1-3 sentences>
    Autonomous systems operating in adversarial environments ... motivate
    <problem class: pursuit-evasion / reach-avoid / target defense /
    perimeter defense> games as the natural framework.

[Para 2 -- Related work A: analytic/geometric line]  <grouped by problem class>
    Existing studies on <problem class> have proceeded along two main lines.
    For <line A>, <Author> [PXXX] derived <result>; <Author> [PXXX] extended
    it to <setting>.  (1 sentence per cited work: contribution + setting)

[Para 3 -- Related work B: computational/learning line]
    When <analytic assumption> does not hold, <HJI [PXXX] / RL [PXXX]>
    approaches ... [PXXX], [PXXX].

[Para 4 -- Gap]  <1-3 sentences, the ONLY place the gap is stated>
    However, these works either assume <A>, or restrict to <B>, or require
    <C>; none of them addresses <precise gap of this paper>.

[Para 5 -- This paper]  <"In this paper, we ...">
    In this paper, we study <exact problem>. The main contributions are
    summarized as follows.  (i) ...  (ii) ...  (iii) ...

[Para 6 (optional) -- Organization]
    The remainder of this paper is organized as follows. Section II ...
```

Rules extracted from the library (details in `references/introduction_patterns.md`):
- Every related-work sentence = contribution + setting + citation. Never a bare
  list of citations.
- The gap sentence must be supported by the related-work sentences that
  precede it.
- Contributions are numbered and each maps to exactly one main theorem or one
  algorithm/experiment in the paper.

---

## 2. Problem Formulation template (references/templates/problem_formulation.md)

```
A. Scenario description in words (players, regions, sensing, obstacles).
B. Notation: vectors bold upright ($\mathbf{x}$), scalars italic ($x$, $t$).
C. Dynamics:   $\dot{\mathbf{x}}_i = f_i(\mathbf{x}_i, \mathbf{u}_i)$,
   $\mathbf{x}_i \in \mathbb{R}^{n}$, $\mathbf{u}_i \in \mathcal{U}_i$,
   $\|\mathbf{u}_i\|_2 \le 1$ (unit-speed players unless stated otherwise).
D. Definitions (Definition 1: capture, Definition 2: outcome/win region).
E. Assumptions (A1 speed ratio, A2 information structure, A3 region shape) --
   every assumption numbered and used later by number.
F. Strategies: $\phi_i: \mathcal{X} \to \mathcal{U}_i$ (feedback) vs
   open-loop $\mathbf{u}_i(t)$; state which class is admissible.
G. Problem statement: "Problem 1: find $\phi_P^*$ / characterize
   $\mathcal{W}$ such that ...".
```

Symbol-contract reminders (see `references/latex_notation.md` for the full table):
- Declare the symbol map once: pursuers $\mathcal{P}$, evaders $\mathcal{E}$,
  defenders $\mathcal{D}$, attackers $\mathcal{A}$, target/flag $\mathcal{T}$.
- Do not reuse a symbol across sections with different meanings; if the
  literature uses conflicting symbols, adopt ONE convention and state it.

---

## 3. Theorem/Lemma/Proof template (references/templates/theorem_lemma_proof.md)

```latex
\begin{lemma}\label{lem:dominance}
Let $...$ (all hypotheses explicit; each maps to an assumption A1--A3).
Then $...$ (conclusion in precise set/equality form).
\end{lemma}
\begin{proof}
Step 1 (construct candidate boundary): consider ...
Step 2 (show boundary characterization): from (12), we obtain ...
Step 3 (rule out the complement): suppose, to the contrary, ...
Step 4 (conclude): hence ...
\end{proof}

\begin{theorem}\label{thm:main}
[Main claim; cite Lemma \ref{lem:dominance} inside the proof.]
\end{theorem}
\begin{proof}
...
\end{proof}

\begin{remark}
[Physical interpretation; scope; what fails if A1 is dropped.]
\end{remark}
```

Rules: every assumption used must be numbered and cited in the statement;
necessary vs sufficient conditions never mixed; a numeric simulation may
illustrate but NEVER replace a proof.

---

## 4. Algorithm float (templates/algorithm.tex)

```latex
\begin{algorithm}[t]
\caption{<Name of the proposed strategy/algorithm>}
\label{alg:proposed}
\begin{algorithmic}[1]
\Require initial states $\mathbf{x}_i(0)$, parameters $r_c, r_s, v_i$
\Ensure feedback strategy $\phi_i$ / capture assignment $\pi$
\State initialize $\pi \leftarrow \pi_0$; $k \leftarrow 0$
\While{termination condition not met}
    \State measure $\mathbf{x}(t_k)$ \Comment{information available to player $i$}
    \State compute candidate boundary point via (14) \Comment{Lemma 2}
    \State update control $\mathbf{u}_i(t_k) = \phi_i(\mathbf{x}(t_k))$
    \State $k \leftarrow k+1$
\EndWhile
\State \Return $\pi$
\end{algorithmic}
\end{algorithm}
```
Every step that uses a theoretical result carries a `\Comment` naming the
equation/lemma. Complexity statement goes in the text right after the float.

---

## 5. Simulation section template (references/templates/simulation_section.md)

```
A. Simulation setup: environment, dynamics parameters table (value+unit),
   toolchain (Python/MATLAB), integrator + step size, number of Monte-Carlo
   runs, random seeds.
B. Scenario descriptions: Fig. N verifies Theorem M -- one sentence linking.
C. Baseline definitions and fairness of comparison.
D. Results: report metric = value +/- std over runs; state significance.
E. Discussion: connect the observed numbers back to the theory (which
   constant/boundary in which theorem explains the curve).
```
Figure style rules live in `references/visualization_guidelines.md` and the
ready-made rcParams in `scripts/simulation_plotting.py`.

---

## 6. Conclusion template (references/templates/conclusion.md)

```
This article studied <problem in one sentence>. <Main analytic results:
which regions/strategies were characterized, under which assumptions.>
<Algorithmic contribution in one sentence.> <Simulation/experimental
validation summary with the headline number.> <Scope limitation.>
<Future work: 2-3 concrete extensions tied to limitations, NOT new topics.>
```
Forbidden: copying the abstract; claiming results not proven/shown above.

---

## 7. IEEE three-line tables (templates/ieee_tables.tex)

```latex
% Method comparison table
\begin{table}[!t]
\centering
\caption{Comparison With Existing Strategies}
\label{tab:comparison}
\begin{tabular}{lccc}
\toprule
Method & Win region & Online cost & Info required \\
\midrule
Apollonius-based [PXXX] & $\mathcal{C}_{PE}$ & $O(1)$ & positions \\
HJI-based [PXXX] & numerical & $O(N_x N_u)$ & full state \\
Proposed & $\mathcal{B}$ (closed form) & $O(n)$ & local \\
\bottomrule
\end{tabular}
\end{table}
```
Use booktabs (\toprule/\midrule/\bottomrule), no vertical rules; units in the
column header; numbers with consistent significant digits.
