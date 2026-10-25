# LaTeX Notation Contract — lsh-game-paper

Default writing style of the user (mandatory unless the user says otherwise)
plus the cross-paper symbol mapping. The mapping table is filled/updated from
paper archives (Section 5 of each PXXX.md); it prevents the classic failure of
reusing a symbol that two source papers define differently.

## 1. User's fixed conventions

| Item | Rule | Example |
|---|---|---|
| Vectors | bold upright | `\mathbf{x}`, `\mathbf{u}_P` |
| Scalars | math italic | `x`, `t`, `v_P`, `r_c` |
| 2-norm | subscript required | `\|\mathbf{x}\|_2` |
| First appearance | define every symbol at first use | "where $\mathbf{x}_P\in\mathbb{R}^2$ is the position of P" |
| Uniqueness | one symbol = one meaning across the whole paper | never reuse $\mathcal{B}$ |
| Inline vs display | prefer inline short formulas; split long ones only per IEEE two-column layout | |
| Sets | calligraphic | `\mathcal{W}`, `\mathcal{R}_P` |
| Players | calligraphic sets, subscript letters | $\mathcal{P}, \mathcal{E}, \mathcal{D}, \mathcal{A}$ |

Automated check: `python scripts/notation_checker.py paper.tex`.

## 2. Standard lsh-game-paper symbol set (use unless a source paper's result is
quoted verbatim — then keep the source symbols and say so)

| Symbol | Meaning |
|---|---|
| $P, E, D, A$ | pursuer, evader, defender, attacker (players) |
| $\mathbf{x}_i, \mathbf{u}_i$ | state, control of player $i$ |
| $v_i, \phi_i$ | speed, feedback strategy of player $i$ |
| $\mathcal{U}_i$ | admissible control set (often $\{\mathbf{u}: \|\mathbf{u}\|_2\le 1\}$) |
| $t, t_f$ | time, terminal time |
| $r_c$ | capture radius (point capture: $r_c=0$) |
| $r_s$ | sensing radius (limited-sensing games) |
| $\alpha$ | speed ratio $v_E/v_P$ (some papers use $v_P/v_E$ — always define) |
| $\mathcal{T}$ | target region / flag region |
| $\mathcal{C}_{PE}$ | Apollonius circle of $P$ vs $E$ |
| $\mathcal{B}$ | barrier (boundary of the winning region) |
| $\mathcal{W}_P, \mathcal{W}_E$ | winning regions |
| $\mathcal{R}_P, \mathcal{R}_E$ | dominance / reachable regions |
| $V(\mathbf{x},t)$ | value function |
| $J$ | payoff/cost functional |
| $\lambda$ | costate (PMP) |
| $H$ | Hamiltonian |
| $\mathcal{L}, \mathcal{D}$ | Isaacs PDE operators (main/denominator) |

## 3. Cross-paper symbol mapping table

Synthesized from the archives (game_theory_foundations.md symbol-conflicts survey +
problem_formulation.md mapping table). **Within one derived document, use the canonical
symbol and give the original in parentheses at first mention** (e.g., $\mathcal{B}$
(denoted $B$ in [P035])). When quoting a paper's result verbatim, keep its symbols and say so.

### 3.1 Conflicts that MUST be resolved before writing (four speed-ratio orientations coexist)

| Concept | Conflicting usages (PXXX: symbol) | Canonical choice |
|---|---|---|
| speed ratio | $\alpha=v_T/V_A<1$ [P022]; $\alpha=v_A/v_D<1$ [P011]; $\alpha=v_E/v_P$ (also printed $a$) [P002/P031/P094]; $\alpha_{ij}=v_{P_i}/v_{E_j}>1$ [P100/P103/P058]; $\beta_i$ [P044]; $\nu_i=v_{D_i}/v_A>1$ [P050/P017]; $\nu=v_E/v_P$ [P023/P071]; $\lambda=V_P/V_T$ [P013] | define **once, explicitly, with orientation**: e.g. $\alpha = v_E/v_P \le 1$ (evader-over-pursuer); never reuse $\alpha$ for the inverse without saying "inverse ratio" |
| capture radius | $l$ [P041/P094/P102]; $r$ [P031/P080/P098]; $r_i$ [P103/P106]; $r_c$ [P113]; $r_F,r_D$ [P034]; $\rho$ [P050/P091] | $r_c$ |
| barrier | barrier set [P073]; $B(\mathbf{x})=\max\{B_1,B_2\}$ function [P035]; CBF $B_j$ [P046]; $\mathcal{B}$ curve [P099/P102] | $\mathcal{B}$ = barrier set; $b(\mathbf{x})$ = barrier function value |
| Hamiltonian vs geometry | $H$ Hamiltonian [P022/P061]; $\mathbf{H}_j$ half-space [P001]; $h(x)$ target function [P048] | $H$ = Hamiltonian only; target sets via $\mathcal{T}=\{h\le 0\}$ stated once |
| $\delta$ | non-anticipative map [P041]; time shift [P101]; capture distance [P002]; startup time $\Delta$ [P007] | $\delta$ = time shift only (this library's most common); rename others |
| $\rho$ | capture radius [P050/P091]; sensing radius [P062/P067]; intruder sensor range [P071]; thrust bound [P108] | avoid $\rho$ for radii (use $r_c, r_s$); keep for thrust bounds |
| $E$ | evasion space [P073/P058]; energy function [P113]; evader; expected payoff [P051] | $E$ = evader only; spaces via $\mathcal{E}$ |
| $T$ | target set [P050/P041]; terminal time; capture time [P019]; target player [P022] | $\mathcal{T}$ = target set; $t_f$ = terminal time; $T_c$ = critical time |
| $J$ | payoff [P044]; branch values [P019]; pursuer/evader-side payoffs [P102]; offensive/defensive [P091] | $J$ = payoff functional; subscripts indexed per player |
| $V$ | value function [P022]; max speeds [P066] | $V$ = value function; speeds as $v_i$ |
| $I$ | interception point [P022/P096]; identity matrix [P027]; information set [P062/P064] | $\mathbf{I}^\star$ = interception point; $I_i(t)$ = information set; $\mathbf{Id}$ = identity |
| $\Gamma$ | singular/dispersal surface [P019]; winning-region boundary arcs [P102]; sightline heading [P007] | $\Gamma$ = singular/dispersal surface only |
| $\phi$ | heading angle [P011/P026/P091]; potential functions [P102/P058/P031] | $\phi$ = heading; level-set functions as $h(\mathbf{x})$ |
| $S$ | safe/reachable set [P066]; Voronoi cell [P113]; terminal set [P044] | $\mathcal{S}$ = safe-reachable set; cells as $\mathcal{V}_i$ |
| $\omega$ | line-of-sight angle [P091]; blend weight [P003]; angular rate [P007/P114] | $\omega$ = angular rate; LOS angle as $\theta_{LOS}$ |

### 3.2 Recommended canonical set (already used by the majority of the library)

$P, E, D, A$ players; $\mathbf{x}_i, \mathbf{u}_i$ state/control; $v_i$ speed;
$\mathcal{U}_i$ control set; $r_c$ capture radius; $r_s$ sensing radius;
$\alpha = v_E/v_P$ speed ratio (orientation stated once); $\mathcal{T}$ target region;
$\mathcal{C}_{PE}$ Apollonius circle; $\mathcal{B}$ barrier set; $\mathcal{W}_P,\mathcal{W}_E$
winning regions; $\mathcal{R}_P,\mathcal{R}_E$ dominance regions; $V(\mathbf{x},t)$ value;
$J$ payoff; $\lambda$ costate; $H$ Hamiltonian.
