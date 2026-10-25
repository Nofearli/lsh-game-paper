# Game Theory Foundations — Master Theory Compendium

Cross-paper synthesis of the mathematical tools used in the lsh-game-paper library (100 per-paper archives, `papers/PXXX.md`). Every claim carries its archive ID and, where the archive records it, the original page/equation. `[proven]`/`[asserted]` flags propagate the archives' own proof-gap notes (archive Section 7). Symbols are paper-local; see "Symbol conflicts observed" at the end.

---

## 1. Apollonius circle / sphere and Apollonius partitions

**Definition.** For pursuer $P$, evader $E$ with speeds $v_P > v_E$ and ratio $\alpha = v_E/v_P \in (0,1)$, the Apollonius circle (AC) is $\mathcal{A} = \{x : \|x - x_P\| = \alpha\|x - x_E\|\}$, i.e. the equal-time locus. With $r = \|x_E - x_P\|$:
$$x_C = \frac{x_E - \alpha^2 x_P}{1-\alpha^2}, \qquad R = \frac{\alpha\, r}{1-\alpha^2}.$$
Equivalent parameterizations appear as $x_A = \alpha x_E - \beta x_P$, $R_A = \gamma r$ with $\beta = \nu^2(1-\nu^2)^{-1}$, $\gamma = \nu(1-\nu^2)^{-1}$, $\alpha = (1-\nu^2)^{-1}$ for $\nu = v_E/v_P$ [P023, eq. (1), p. 3], and as $c_i = \frac{V_i^2}{V_i^2 - V_e^2}e + \frac{V_e^2}{V_e^2 - V_i^2}p_i$, $r_i = \frac{V_iV_e}{|V_i^2 - V_e^2|}\|e - p_i\|$ [P066, eq. (2), p. 2].

**Canonical construction.** Square the equal-time identity $\|x - x_P\|/v_P = \|x - x_E\|/v_E$ and complete the square; the interior of the AC is the evader-dominant region. In 3D the same algebra gives the Apollonius sphere: $\|\Gamma - P\|/\|\Gamma - T\| = \lambda$, squared to an explicit center/radius [P002, eq. (3), p. 5; P013, Def. 2, eqs. (2)–(5), p. 3; P033, eq. (8); P075, Sec. III "Apollonius sphere in 3D", eq. (13)]. With the pursuer constrained to a different dimension (3D pursuer vs. planar evader), the intersection of the two players' isochrones is again a circle in the evader's plane with closed-form center and radius depending on the pursuer's altitude $z_P$ [P052, eqs. (4)–(6), pp. 1300–1301, Remark 1].

**Key derived facts.**
- *Position-independent tangent cone*: the angle $\theta$ between the line center→focus and any tangent from the slower player satisfies $\sin\theta = \lambda$ — depends only on the speed ratio [P013, Lemma 1, eq. (6), p. 4, proven by right-triangle algebra $\|O-T\| = r/\lambda$].
- *Apollonius partition*: each pursuer's AC induces a dominant region; the evader's region is $\bigcap_i$ (interiors of the $P_i$-ACs) [P104, Def. 2, Sec. 3; P097, eqs. (6)–(9), pp. 3–4, with neighbor indicator $\delta_i$ marking pursuers whose ACs support the evader's region].
- *One AC is enough (containment)*: a Lyapunov pursuit law $\mathbf{v}_P = \hat{\mathbf{z}}_P$, $\mathbf{z}_P = (R_C - R_A)\hat{\mathbf{r}} + \nu\,\mathbf{y}$ confines the time-varying AC inside the initial AC inflated by $\delta$ and guarantees capture in $t \le t_0 + 2(1+\nu^{-1})R_C\ln(R_C/\delta)$ [P023, Thm 1, p. 3; Cor. 1; Lemma 1: $\|{\bf r}(t)\| < \|{\bf r}(t_0)\|$ strictly].
- *Area gradients of AC intersections*: $\nabla A_e$ for the intersection of $N$ Apollonius discs derived without a closed-form area, via a coordinate-free Leibniz/Reynolds transport argument on level sets [P066, Prop. 1.3 and Thm 1.4, pp. 4–6].
- *Robust ovals*: with measurement noise on speed ratio and capture radius, the safe region is built from Cartesian-oval boundaries with closed-form sensitivity [P028, Thm 1, Thm 2 (OIS), eqs. (11)–(14), (33)].

**Scope/assumptions.** Simple motion (single integrators), constant max speeds, strict speed superiority, point capture unless a radius is folded in (Sec. 2 below). At $\alpha = 1$ the AC degenerates to the perpendicular bisector (line/plane) [P002, Fig. 2, p. 4; P104, Def. 1].

**Pitfalls.** (i) The equal-speed limit is singular: formulas blow up as $\alpha \to 1$; P023 carries a "minor preprint typo" note on the $\alpha,\beta,\gamma$ identification (eq. (1), p. 3). (ii) AC-based partitions are exact only for point capture; adding radii requires the offset machinery of Sec. 2. (iii) The AC is a *dominance* tool, not an optimality certificate: [P023] explicitly positions it as dissolving dispersal pathologies rather than proving Nash play.

---

## 2. Offset / generalized Apollonius regions (non-zero capture radius)

**Definition.** For capture radius $\rho \ge 0$, the simultaneous-arrival condition becomes a *weighted difference of distances* equal to a constant:
$$\frac{1}{\alpha}\|x - x_A\| = \|x - x_D\| - \rho$$
(time for attacker to reach $x$ = time for defender to get within $\rho$ of $x$) [P091, p. 4, "interception-tie point $S'_j$"]. Equivalently $d(x) = R_D - aR_I - r \ge 0$ defines the invader's dominance region, whose boundary is a Cartesian oval (fourth order in coordinates) [P031, eq. (2.5), p. 3]. In squared program form: $f_i(x,\theta) = \|x - x_A\|^2 - \big(\frac{\|x - x_{D_i}\| - \rho_i}{\nu_i}\big)^2 \le 0$ [P050, eq. (11), p. 6359], and in function-based form $f_{ij}(x) = \|x - x_{P_i}\| - \alpha_{ij}\|x - x_{E_j}\| - r_i$ [P104, Def. 3, attributed to Yan et al. 2022 (P103); P103, ES machinery, Sec. 3].

**Canonical construction.** Apply the law of cosines in the triangle (pursuer, evader, boundary point) and solve the resulting quadratic; the admissible root is the *inner* oval. Exemplar: P094's capture strategy on the oval — law of sines $\sin\varsigma/\sin\varepsilon = r_1/r_2$ (eq. (9)) + time balance $r_1 = a r_2 + l$ (eq. (10), itself the oval definition) → $\varepsilon = \arcsin\!\big(\tfrac{r_2}{ar_2 + l}\sin\varsigma\big)$ (eq. (11)) → quadratic $(1-a^2)r_2^2 - 2(al + \delta\cos\varsigma)r_2 + \delta^2 - l^2 = 0$ (eq. (13)) whose "+" root is an outer oval violating (10), so the "−" root is taken [P094, Lemma 3.2, eqs. (8)–(14), p. 4]. Same quadratic-with-two-roots structure in P091's Theorem 3: $(1-\mu^2)\eta_j^2 - 2(\mu\rho_i + \varsigma\cos\theta)\eta_j + \varsigma^2 - \rho^2 = 0$ (eq. (17)), the two roots being the near arc $O^1_i$ and far arc $O^2_i$; the zero-discriminant condition gives the half-angle $\theta_{ji}$ and the defensive advantage angle $\gamma_i = 2\theta_{ji}$ [P091, Thm 3, eqs. (15)–(17), pp. 6–7].

**Papers using it.** P050 (dominant region (10)–(11), Slater/KKT analysis, Sec. 4 below); P091 (all barrier Theorems 1–7); P094/P102/P112 (lifeline games, Sec. "Barrier surfaces"); P098 (generalized barrier via metric projection onto the target, eq. (19), reducing to "(11) in [7]" for circular targets); P103 (capture-radius-generalized Apollonius surface as zero level set, ES certificate $\bar{E}(s,j) = \{f_{ij} \ge 0,\ i \in s\}$); P060 (Cartesian oval centered at the attacker, polar-form quadratic whose positive root is $f_{r_A}$, p. 4); P092 (Decision Line from Apollonius circles of a faster target).

**Pitfalls.** (i) Strict convexity/coercivity of $f_i$ needs $c_{i,1} = 1 - 1/\nu_i^2 > 0$, i.e. every defender strictly faster — the hidden standing assumption of P050 [P050, Prop. 1, eq. (14), and archive Sec. 7 observation 1]. (ii) At $\alpha = 1$ the oval degenerates to a hyperbola branch (difference of distances constant) [P091, Thm 6, p. 9; P094, Fig. 2b]. (iii) "Polynomial constant with six variables" phrasing in P091 is loose — $s_j^*$ is an implicit quartic root [P091, Remark 14, eq. (21)].

---

## 3. Cartesian ovals and isochrones

**Definition.** *Cartesian oval*: locus $|PS| + m|QS| = a$; first type ($m < -1$, $a \in [0,|PQ|)$) is bounded, strictly convex, simple closed, with $P$ outer and $Q$ inner foci; $a = 0$ gives the Apollonius circle; second type ($a \in (m|PQ|,0)$) is bounded but not convex [P041, p. 3]. *Isochron* of time $\tau$: the set player $i$ can reach at $\tau$ under optimal direction strategies; a predicted horizon, distinct from real time [P053, Def. 1, p. 2].

**Canonical construction.** Without obstacles, time-optimal paths are straight lines and isochrones are concentric circles centered at the agent [P069, Thm 1, p. 4, via wavefront propagation; P053, Lemma 2]. With polygonal obstacles, paths break at obstacle vertices and every isochrone piece is a circular arc about a *known* center (continuous-Dijkstra wavefront) [P069, Thm 2, p. 4]. For a damped double integrator $\dot v = -\mu v + u$, the optimal isochrone is the circle with moving center $c_p(\tau) = (x_p - \tfrac{v_{px}}{\mu}(e^{-\mu\tau}-1), \ldots)$ and radius $R_p(\tau) = \tfrac{u_{pm}}{\mu}(\tau + \tfrac{e^{-\mu\tau}-1}{\mu})$ [P053, Lemma 2, eqs. (8)–(13); P061, eq. (15), reached via the Maximum Principle: max acceleration with constant heading, eqs. (7)–(14)]. Self-overlapping isochrones generate the *multiple reachable region* (MRR) with boundary curves $\mathcal{B}_I, \mathcal{B}_{II}$, cusp time $t_u$ and barrier time $t_{is}$ [P061, Lemma 2, eqs. (25)–(32); circumscribing/inscribing times: at least one, at most three — Thm 1 + Algorithm 1].

**Papers.** P041 (dominance via ovals; the l-oval boundary $D_l$); P052 (isochrone intersection = dimension-heterogeneous AC); P053 (16-case taxonomy of the damped-pursuer vs single-integrator game by ET/IT tangency events of isochrone circles, Table I, p. 7); P061 (MRR and three-type attacker dominance region); P069 (obstacle isochrones); P094/P102 (oval reachability).

**Pitfalls.** The sufficiency direction "point satisfying the travel-time inequality ⇒ reachable before capture" is usually argued only for the pursuer running straight at the point; the general case needs the triangle inequality and is occasionally left implicit [P102, Lemma 3 proof-gap note, p. 7; P094, formal gap in eq. (6) where the capture-avoidance path constraint is only in prose].

---

## 4. Dominance regions and Voronoi-based partitions

**Definitions.** *Voronoi cell* (equal-speed, point-capture dominance): $R^p_i = \{x \in \Omega : \|x - x_{P_i}\| \le \min_{i'\ne i}\|x - x_{P_{i'}}\|,\ \|x - x_{P_i}\| \le \|x - x_{E_j}\|\ \forall j\}$ [P104, Def. 1; P113, Voronoi partition $V(\Omega) = \{S_e, V_1, \ldots, V_N\}$, Sec. 3]. *Dominance region under speed ratio*: the Apollonius/oval superlevel sets of Secs. 1–2 [P041, Def. 2, p. 4: $D_l(x_1,x_2) = \{x : \|x-x_1\| - \alpha\|x-x_2\| > l\}$, and with obstacles $D(x_1,x_2) = \{x \in X : d_L(x,x_1) - \alpha d_L(x,x_2) > 0\}$ in the shortest-path metric $d_L$].

**Canonical results.**
- *Dominance = reachability*: the evader's initial dominance region equals its guaranteed reachable region — no obstacles [P041, Thm 4, p. 4, "easy to prove by the convexity of Cartesian ovals of the first type", cited to Yan–Shi–Zhong]; with obstacles and $l=0$, proven constructively via exact arrival times $t_p(x) = t_0 + \frac{1}{\alpha}d_L(x_{p0},x)$, $t_e(x) = t_0 + d_L(x_{e0},x)$ and the path-invariance Lemma 6 [P041, Thm 5, pp. 4–5].
- *Voronoi area descent*: each pursuer moves to decrease the evader's cell area $A$; the input heads exactly to the midpoint of its line of control $B_i$ [P113, Thm 2]; capture in finite time via the energy $E = kA + \|x_e - x_p\|^2$ decreasing at rate $c(\beta)$ [P113, Thm 3].
- *Attack-region method*: for $\alpha = 1$ the attack region is computed from Voronoi diagrams, for $\alpha < 1$ from Apollonius circles; the barrier follows "by utilizing the semipermeability of barrier" [P099, p. 1038 — semipermeability asserted, not verified].
- *Weighted-Voronoi coverage of footprints*: 3D Apollonius-sphere → tangent cone → central-projection ellipse chain, projected ellipses covered via weighted Voronoi partitions [P013, Thm 1, eqs. (13)–(16); eqs. (25)–(33)].

**Papers.** P013, P041, P052, P066, P069, P070, P097, P099, P104, P113.

**Pitfalls.** Voronoi dominance is exact only at equal speeds and point capture [P104, Def. 1]; the classical "aim at the exit point" strategy is a valid *non-anticipative* strategy only under conditions made precise in P041 (Thm 7) and can fail outright with obstacles (P041, Example 13 counterexample, p. 8 — no PELIDR non-anticipative strategy exists for a corner-obstacle instance, because two evader controls coincide on an interval while the forced pursuer replies differ, violating non-anticipativity (3)).

---

## 5. Reachable sets and reach–avoid sets (HJ formulation)

**Definition.** For dynamics $\dot x = f(x, u, d)$, target $\mathcal{L}$ and obstacle set $\mathcal{K}$, the reach–avoid set $\mathcal{V}(x,t) = \{\theta(0) :$ exists $u(\cdot)$ s.t. for all $d(\cdot)$, $\exists \tau \in [t,0]$: $\theta(\tau) \in \mathcal{L}$ and $\theta([t,\tau]) \not\subseteq \mathcal{K}\}$, computed as the viscosity solution of a constrained HJI PDE with terminal data $+1$ on $\mathcal{L}$, $-1$ on $\mathcal{K}$ [P039, eqs. (3)–(5), p. 1454; P040, Sec. IV].

**Canonical construction (library standard, from the Berkeley/Stanford line).** (i) Elliott–Kalton nonanticipating-strategy formulation of the finite-horizon reach–avoid game; (ii) equivalent constrained terminal-cost minimax via the *time-dilation augmentation* trick; (iii) upper value = constrained viscosity solution of the HJI equation, $J^{\bar{}}_T(x^0) = \phi(x^0,-T)$, "by slight modifications of the proof techniques" of Evans–Souganidis [P040, results (12)–(15), Isaacs condition (16)]. Two-phase objectives are handled by *sequential composition*: $\tilde{R}_A = \mathcal{G}_F \cap R_A$ stitches flag-capture and flag-return sets [P039, eq. (5), p. 1454 — the founding device, later reappearing in closed form as the "transition phase" of P038 and the ellipses of P018].

**Alternatives used in the library.** Open-loop reachable region à la P041 Def. 3 (quantifier form $\exists u_e, \forall u_p, \ldots$; its complement is an anticipative/open-loop-Stackelberg object, eq. (6), p. 5 — the gap Theorem 7 closes); time-to-go metrics $\varphi_T = \|x_T - x_e\|/v_e$, $\varphi_s$ (intercept time of a straight-running evader) yielding safe/failing/risky partitions [P077, Props. 1–2, eqs. (4)–(9), p. 699–700]; isochrone-based reachable regions (Sec. 3).

**Pitfalls.** Numerical HJI gives the *winning set*, not the feedback's optimality certificate; P044 uses HJI purely for verification of geometric candidates (Thm 1, p. 1054). The constrained HJI is an obstacle-type (reflected) boundary condition — the constraint enters as a projection above $-\phi_K$ [P040, step (ii) of the proof sketch].

---

## 6. Games of kind and degree; winning regions

**Definitions.** *Game of kind*: which of two target sets is hit first (binary outcome). *Game of degree*: a continuous payoff once the kind is decided (capture separation, terminal distance). The library's standing taxonomy is 1v1 / Nv1 / 1vM / NvM with ~90 classified references [P044, pp. 1050–1053].

**Canonical structure.** Outcome preference ordering rules out nonterminating play: P022's Definition 1 (Type P: $m_t \succ_P n_t \succ_P \Upsilon$, nontermination worst for the Attacker) justifies "no discriminatory/stroboscopic strategies" [P022, Def. 1, p. 555]. The game of kind is frequently *solved by the game of degree*: $J = \min_i y_{A_i}(T_i) \le 0 \iff$ attack team wins [P019, eq. (5), p. 561]. Winning regions are zero-sublevel sets of the value: $\mathcal{W}_A = \{\theta : V(\theta) \le 0\} = \Theta^{=0}$, $\mathcal{W}_D = \Theta^{>0}$ [P050, eqs. (13), (32), justified via Mitchell–Bayen–Tomlin Thm 2]; or defined directly with path constraints (PWR/EWR quantifier definitions) [P094, eqs. (15)–(16), p. 4–5].

**Papers.** P011 (two-threshold classification bypass/penetration), P012 (three circle-relation subgames), P019, P022, P035, P049, P050, P052, P056 (three-case territory split), P058, P091, P094, P102, P112.

---

## 7. Barrier surfaces (construction and semipermeability)

**Definition.** A barrier $\mathcal{B}$ is the codimension-one set $\{V = 0\}$ (or a directly constructed surface) separating winning regions, with the *semipermeability* property: each side holds a strategy preventing the opponent from crossing.

**Canonical constructions in the library** (full treatments in `barrier_reachability.md`):
- *Apollonius-tangency*: the barrier is the locus where the relevant AC is exactly tangent to the defender's bisector; algebraically a hyperbola branch with center at the AD midpoint and axes along AD [P022, Thm 3, eqs. (82)–(83), pp. 564–567, discriminant $-\alpha^2(1-\alpha^2) < 0$; game-of-kind region $\mathcal{R}_e = \{H(x;\alpha) < 0\}$, eq. (81)].
- *Bisector-plane mirror (3D, equal speeds)*: barrier = union of mirror points, circular arcs in vertical planes, and a spherical patch over the pursuers' projection triangle [P073, Lemma 1, Thms 1–3, eqs. (7)–(16), pp. 3–5].
- *Value-zero barrier*: $\{V^g = 0\}$ for the geometric value of the target-defense game, proven the correct HJI object [P031, §4.5, p. 7, Thm 2.1].
- *Tangency barrier with capture radius*: parametric curve from the FOC $dJ_P/dx^* = 0$ (eq. (48)) plus the on-barrier identity $J_P(x^*) = l$ (eq. (49)) [P102, Lemma 7, eqs. (44)–(52), pp. 11–13]; four-piece version with lifetime [P102, Thm 1, eqs. (58)–(59)].
- *Barrier as max of pairwise barriers*: $B(\mathbf{x}) = \max\{B_1, B_2\}$, $B_i = R_E^2 - R_i^2$ [P035, eq. (21), p. 4258]; general-coalition inductive construction where "every barrier segment depends on at most two pursuers" [P100, Thms 1–4, pp. 113–116].
- *Bond of sub-game barriers*: the three-player barrier is the "bond" of $\mathscr{B}_1$ and $\mathscr{B}_2$, the evader's barrier trajectory switching at the intersection of the two sub-game curves [P112, Thm 2, eqs. (18)–(20), p. 6].

**Semipermeability status.** Proven via HJI/viscosity in P022, P031, P050, P019, P080, P082, P096 (Sec. 9 below). Asserted: P099 ("utilizing the semipermeability of barrier", p. 1038), P098 (Remark 2), P101 (barrier machinery), P094 ("both sides have strategies ensuring the opponent does not win", p. 5 — asserted), P112 (RPE construction asserted). P073 constructs the barrier but *no strategies at all* ("under $P_i$ and $E$'s optimal strategies" is invoked, not constructed) [P073, archive Sec. 7, observation 2].

---

## 8. Dispersal and singular surfaces

**Definitions.** *Dispersal surface*: two optimal choices meet; the player owning the choice picks the side. *Switch envelope / equivocal surface*: one side's optimal trajectories leave tangentially. *Focal surface*: envelope where characteristics fold. *BUP (barrier useable part)*: the portion of the terminal manifold where the Hamiltonian condition admits usable barrier trajectories.

**Canonical results.**
- *$m$-branch viscosity lemma*: near a kink where $u = \min_{i \le m} u_i$ with distinct gradients, the viscosity condition holds iff $F(x_0, \sum_i \lambda_i \nabla u_i(x_0)) \ge 0$ for all convex weights $\lambda$ — proven by showing no test function attains a local minimum of $u - \varphi$ (distinctness forces $\|\nabla u_i - \nabla u_j\|^2 \le 0$, contradiction) and applying KKT at the minimum of the lifted problem [P019, Lemma 1, eq. (2), p. 560, generalizing Melikyan's $m=2$]. Mixed max–min branches pass automatically (Lemma 2, eq. (3)).
- *Dispersal certification needs more than exit-transversality*: "it is not enough that optimal trajectories leave the surface; the viscosity condition is also necessary — and indeed fails on $\Upsilon_2$" [P019, Remark 3 + Sec. V-A]: the naive $\bar V = \max\{J_1, J_2\}$ is *not* the value; the numerical set $\Upsilon_2 = \{X : \max_\lambda f(\lambda, X) > 0\}$ is nonempty (Fig. 3), and Lemma 8, eq. (29), shows the defender can strictly increase both branch values there.
- *Switch-envelope ODE*: along the envelope, $\dot X = F^*(p)$, $\dot p = a(X,p)(p - q(X))$ with $a$ fixed by $(p-q)^\top F^*(p) = 0$, giving eq. (36); bifurcation theorems produce two envelopes (Thm 2), envelope + dispersal (Thm 3), or a single envelope (Thm 4), all local, all requiring $C^2$ branches and strict inequalities [P019, eqs. (35)–(36), pp. 568–572].
- *Classical examples*: 2P1EDG dispersal surface where the two AC intersections are equidistant from E; teams guessing opposite branches pay an "infinitesimally small price"; the perpetual dilemma is improbable [P044, p. 1056, p. 1059]. Phase-II CTF dispersal $\{y_A = y_D\}$ [P034, Sec. V; P038, eq. (34), $\mathcal{D} = \{y_A = y_D\}$]. MPME dispersal surfaces $y_{s_\iota} = y_{s_{\iota'}}$ between assignments, outside which the value is $C^1$ [P037, Sec. III, citing [35]]. Five-surface taxonomy for the DDR–OA cone game: EDS, ESCS, PES, PDS, PSCS [P076, pp. 294–302]. Obstacle-induced type-(p,u,p) lines and hyperbolic dispersal surfaces [P069, Remark 1]. Indeterminate terminal component $\min\{d_1,d_2\} = l$ blocking the classic single-BUP RPE construction in the three-player lifeline game [P112, p. 4].

**Pitfalls.** Focal surfaces closing the singular construction are open in P019 ("cannot be constructed by solving an ODE system", pp. 569–572); dispersal tie-breaking is typically handled by a geometric dual argument, not a variational one [P022, Cor. 1, $\kappa = \arg\min_i \Delta_i$, p. 561]; P102's dispersal OTP pair gets no tie-breaking rule (Thm 2, $\mathcal{R}_2$).

---

## 9. HJI equation and viscosity verification

**Definition (verification form).** If there exists a $C^1$ function $V(t,x)$ satisfying $-\partial V/\partial t = \min_u \max_v\{\nabla V \cdot f(t,x,u,v) + g\}$ with $V(t_f,x) = q(x)$, then the saddle-point feedbacks are optimal in state feedback [P044, Thm 1, eq. (3), p. 1054, cited to Hespanha]. For nonsmooth candidates, $V$ is a viscosity solution iff $F(\xi) \le 0$ for all $\xi \in \partial^+ V$ and $F(\xi) \ge 0$ for all $\xi \in \partial^- V$ [P050, eqs. (7)–(8), Def. 1, Crandall–Evans–Lions].

**Canonical verification workflows (library exemplars).**
1. *Envelope argument* (geometric value → HJI): compute $dV/dx^*$ along the implicitly defined aimpoint, show it equals the stationarity residual of the design equation, hence zero; then $\partial V/\partial x \cdot f = 0$ term-by-term. P022: $dV/dx^*$ (eqs. (64)–(65), (78)–(79)) vanishes because $x^*$ solves the quartic (15); HJI check collapses to $-\alpha/2 - \alpha/2 + \alpha = 0$ (eq. (67)). P044: in the simultaneous-capture region the $\partial V/\partial \phi^*$ term vanishes via the identity $\partial t_{f_i}/\partial\phi^* = F_i t_{f_i}$, and $\partial V/\partial x\cdot f = -1$ via eq. (39), giving $1 + \partial V/\partial x \cdot f = 0$ (eq. (40)).
2. *Implicit-function + determinant collapse*: treat the tangency point $p^*$ as implicitly defined by stationarity + boundary equation, differentiate, and use a determinant identity $K^{*\top}H_{\varphi^*}K^* + \varphi_{y^*}(k^*k_{y^*} + k_{x^*}) = \Delta/d_{y^*}$ (eq. (3.20)) to collapse the value gradient to $[\varphi_{y^*}/d_{y^*}; 0]$ in a local frame [P031, Steps II–III, eqs. (3.13)–(3.21)].
3. *Parametric program + Danskin + Clarke*: candidate value = optimal value of a convex program in $x$ parameterized by the state; strong duality (Slater) → KKT; generalized Danskin gives the Clarke subdifferential $\partial V(\theta) = \mathrm{conv}\{\nabla_\theta L(x^\star,\bar\lambda,\theta)\}$; $C^1$ iff LICQ; viscosity verification by showing $F(\xi) = 0$ for *every* convex combination of active-multiplier gradients [P050, Lemma 1 (eqs. (24)–(26)), Thm 1 (eqs. (27)–(28)), Thm 2, 7 steps, pp. 6361–6362].
4. *$m$-branch convex-hull check* on the singular set: $\tilde H(\sum_i \lambda_i \partial_i^*) \ge 0$ for all weights, via geometric identities + convexity of $\tilde H$ in the gradient [P019, Lemma 7, eqs. (23)–(26), pp. 563–564]; uniqueness by Crandall–Lions comparison [P019, Thm 1, step (iv)].
5. *SOSC/parametric sensitivity*: at local minimizers of the stacked capture-point program satisfying the second-order sufficient condition, the value $V$ is $C^1$ and satisfies the Isaacs equation classically [P048, Thm 2, p. 235, Fiacco-type].
6. *Direct substitution*: closed-form values verified by plugging equilibrium fields into the Hamiltonian: P096 (eqs. (37)–(47), Thm 1), P080 (eq. (17)), P082 (eqs. (17), (44)), P023-adjacent Lyapunov route (no HJI), P055 (Lemmas 1–2: terminal value $C^1$ in the ratio; Theorems 1–3 via HJI).

**Assumptions/scope.** All classical verifications are on the *regular region* only — dispersal surfaces excluded [P044, archive Sec. 7: "no viscosity/weak-solution treatment... classical C¹ verification on the regular region only"]; viscosity extensions cover kinks via Secs. 8/10. P050 proves viscosity globally (including the measure-zero nonsmooth set) and classical exactly where LICQ holds (LICQ fails only on a measure-zero set by Rademacher [P050, Remark 6]).

**Pitfalls.** Squaring the design equation introduces extraneous roots with no stated sign filter [P022, archive Sec. 7 observation 1; P044's root-selection rules (49): $x_T \le 0 \to y_1$, $x_T > 0 \to y_2$ are the exception, stated explicitly]; "piecewise classical + continuous ⇒ viscosity" is asserted rather than verified at switching surfaces [P031, §4.4 gap]; HJI satisfaction on the smooth region alone never proves a value [P019, Remark 6].

---

## 10. Isaacs condition (minimax = maximin Hamiltonian)

**Definition.** $H$ separable in the opposing controls so that $\min_u \max_v H = \max_v \min_u H$; equivalently $F^+ = F^-$.

**Where it holds and is used.** P022: the Hamiltonian decouples per agent, so Isaacs' condition holds and controls are read off costates (eq. (8), p. 556). P050: $H$ separable in $u_A$ and each $u_{D_i}$, hence $F = F^+ = F^-$ with minimizers $u_A^\star = -\xi_1/\|\xi_1\|$, $u_{D_i}^\star = \xi_{i+1}/\|\xi_{i+1}\|$ (eqs. (37)–(38), p. 6363). P040: Isaacs condition (16) guarantees value existence. P086: Value satisfies Isaacs' condition (eq. (6)) and the Nash-saddle property (eq. (7)). P019: minimax Hamiltonian $\tilde H(q) = \|q_D\| - \alpha_1\|q_{A_1}\| - \alpha_2\|q_{A_2}\|$ and equilibrium field $F^*(q)$ (eqs. (14)–(15), p. 562). P103: the HJI-equals-convex-program equivalence ("KKT–Isaacs"). P021: Danskin-based state-gradient machinery certifying equilibrium via the Isaacs condition (eqs. (30), (31), (36), (37)). P048: classical Isaacs-equation verification via SOSC (Thm 2). **Caution**: when the game is played over *feedback* classes the min/max order matters; P044's archive notes the printed Main Equation order in the ATDDG section must be read with the costate sign pattern rather than the prose (Sec. 7).

---

## 11. Pontryagin Maximum Principle: Hamiltonian, costates, transversality, RPEs, BUP

**Canonical two-sided PMP template (AFRL/AFIT school).** For simple motion with Mayer cost:
1. Write the Hamiltonian $H = \sum_k \lambda_k \dot x_k$; separability gives Isaacs' condition.
2. Stationarity: headings align/anti-align with costate vectors, e.g. $\cos\chi^* = -\lambda_{x_A}/\|\lambda_A\|$, $\cos\psi^* = \lambda_{x_D}/\|\lambda_D\|$, $\cos\phi^* = \lambda_T/\|\lambda_T\|$ [P022, eqs. (19)–(21); P044, eqs. (9)–(11)].
3. Costate dynamics $\dot\lambda = -\partial H/\partial x = 0$ (state-independent $H$) ⇒ constant costates ⇒ *straight-line optimal play* [P022, step 3; P044, p. 1055 — with printed typo $\dot\lambda_{y_{P1}}$ repeated for $y_{P2}$, verified on the page image; P052, Lemma 1: control is an LP over a ball, so bang-parallel].
4. Two-point boundary value problem: augment the Mayer function with multipliers $\nu_1, \nu_2$ for the terminal manifold, transversality $\lambda(t_f) = \partial\Phi_a/\partial x$ (or $-\partial$; sign conventions differ between P022 (23) and P044 (52)–(57)), eliminate the multipliers, fix $t_f$ by $H(t_f) \equiv 0$ (Main Equation 1) [P022, eqs. (22)–(32); P044, eqs. (52)–(60)].
5. Reduce to a one-variable design equation and square to a quartic: P022 (55)→(56)→(15); P044 (49). Root selection: P022 leaves it implicit (≥ 2 real roots exist by IVT on the pre-squared form, p. 564); P044 gives explicit rules.
6. RPEs/BUP (Isaacs' retrograde path equations from the BUP): used where the barrier is integrated from the terminal manifold — P112 (Thm 1, eq. (6), (17): parametric barrier via Isaacs' main equation + RPE integration from the whole BUP; the three-player terminal component $\min\{d_1,d_2\} = l$ is "indeterminate" and blocks the classic construction, p. 4).

**Variants.** Bang-bang force allocation for speed-varying plants: PMP gives full acceleration then coast, and the 6-D game decomposes into force allocation + a 1-D search of the terminal value over the average speed ratio $\bar\alpha$ [P055, §IV-A, pp. 1857–1858]. Asymmetric control sets (cube vs. ball thrust): componentwise sign vs. normalized alignment; adjoint antisymmetry (eq. (18)) halves the state+adjoint system [P108, Thm 1, eqs. (19)–(22), (29)]. Damped dynamics: costates are exponentials, not constants [P061, eqs. (8)–(11)].

**Pitfalls.** P094's printed Hamiltonian swaps $\sin/\cos$ relative to its own dynamics (p. 3) — never used downstream; P044's costate typo above; transversality sign conventions differ across the AFRL papers without reconciliation.

---

## 12. Equilibrium concepts: Nash, saddle-point, minimax

**Definitions.** Zero-sum saddle: $J(x_0; u_A^*, u_D^*) = \min_{u_A}\max_{u_D} J = \max_{u_D}\min_{u_A} J$ over the chosen strategy class (P035 eqs. (8), (10); P086 eqs. (6)–(7)). Nonzero-sum Nash: $J_i(x_0; u_i^*, u_{-i}^*) \le J_i(x_0; u_i, u_{-i}^*)\ \forall i$ [P085, eq. (3), p. 691], with *interactive NE* adding non-degeneracy (eqs. (4)–(5)). Mixed-strategy saddle for finite zero-sum games invoked for the matrix-game reduction [P078, eqs. (6)–(7), citing existence results]. Yao's minimax principle imported for randomized competitive analysis against an oblivious adversary [P009, Def. 1, p. 2]. Ordinal potential games: NE existence for $N_e = 1, N_p \ge 2$ via the finite improvement property [P097, Thm 2, eqs. (22)–(28), App. B]. Level-$k$ behavioral equilibrium via recursive best response with Bayesian inference of rationality levels [P029, eqs. (5)–(12)]. Inverse game theory: arbitrary visibility-feasible feedback laws realized as exact NE of reverse-engineered quadratic costs [P090, Thms 1–2].

**Team-of-teams.** Multipopulation LQ games with intra/inter-population best responses and Nash definitions (Defs. 1–6, pp. 3–5) [P010]. Two-level mean-field value factorization: group mean-field collapse $Q_{\mathrm{GRP}}(x) = \sum_k \lambda_k Q^k_{\mathrm{LOC}} + 2Q_{\mathrm{GMF}}$ (eq. (11), p. 3) [P110].

**Pitfalls.** Under state feedback the game "may not necessarily admit a value" (Cardaliaguet) — P103 deliberately adopts feedback and forgoes non-anticipativity (p. 3, Sec. 2.2); P062/P064 keep non-anticipative sets under partial information; the choice of information structure changes which equilibrium concept is even well-posed (Sec. 13).

---

## 13. Strategy classes: feedback vs open-loop vs non-anticipative

**Library positions.** (i) *Perfect state feedback*: strategies $\gamma(t, x)$; used by nearly all geometric papers [P041, P050, P091, P103 — P103 explicitly rejects Elliott–Kalton structures as "too strong (they instantiate Stackelberg play)", p. 3]. (ii) *Non-anticipative (Elliott–Kalton)*: $\delta : \mathcal{U}^e \to \mathcal{U}^p$ with $u_e = u'_e$ a.e. on $[t_0,t'] \Rightarrow \delta[u_e] = \delta[u'_e]$ a.e. on $[t_0,t']$ [P041, Def. 1, eq. (3), p. 4]; generated by locally Lipschitz laws $u_p(t) = \gamma(x_p, x_e, u_e(t))$ (eqs. (4)–(5)) — note these require the evader's *current* control [P041, p. 4]; formalized with Evans–Souganidis machinery in P040 (Sec. IV). (iii) *Open-loop with feedback refresh*: "piecewise open-loop" saddle strategies re-solved along play [P099, p. 1037]. (iv) *Partial information*: deployment/capture two-phase decomposition with open-loop pre-detection and closed-loop post-detection strategies [P062, Thm 1, eqs. (6)–(7)]; sensing-limited winning regions and the "fuzzy region" [P067, Def. 2, p. 5]; conservative radius-free ratio-only barriers [P064]. (v) *Robust/estimated*: virtual evader with chance-constrained inflated decision set fed by a Kalman filter [P027, Sec. 3.2]; RESR safe regions with $3\sigma$ guarantees [P028, Thm 1].

**Value existence.** Friedman-type hypotheses checked in P019 (Remark 1: bounded continuous $F$, separable controls, continuous terminal payoff, forced termination); constrained reach–avoid value via viscosity in P040; P103 accepts possible nonexistence under feedback.

---

## 14. Switching and phase structure

Multi-phase games are solved by backward induction over phases with value-matching:
- *CTF*: two phases (flag capture → return) with HJI sequential composition $\tilde R_A = \mathcal{G}_F \cap R_A$ [P039, eq. (5)]; the closed-form analogue is the transition phase where the Defender "concedes a lost Phase I" and optimizes the Phase II entry state, the transition optimum continuing straight into the Phase II aimpoint (hyperbola condition (57)) [P038, Sec. IV].
- *Reconnaissance*: approach/retreat decomposition with the retreat point = projection of the Apollonius center; Phase-I value verified against HJI (eqs. (57)–(59)) — a step "absent in [20]" [P049, Thms 1–2, pp. 3–5].
- *Ellipses*: two-leg objectives have iso-cost ellipses with foci at start and safe point; thief wins iff the target intersects the open ellipse with major axis $v_T \times$ (guarder arrival time) [P018, Thms 1–2; cooperative case via Danskin, Thms 3–4].
- *Detection-time phases*: partial → perfect information at random $t_s$; the post-detection Apollonius Nash value is substituted as the MARL terminal reward [P017, Lemma 1, Thm 1 (eq. (16)), Prop. 1].
- *Time-limited games*: piecewise polar barriers classified by $(\Delta t, m)$ into two stages and three circle-relation subgames [P012]; range-limited detection with two-threshold classification and barrier $\mathscr{B}^{\text{inner}}$ (eq. (17)) [P011, Thms 1–4]; lifetime-limited lifeline barrier, four pieces [P102, Thm 1].
- *Piecewise value continuity*: the $C^1$ gluing argument — at the switch $V_s = V_g$ and the gradients (66) with (60)–(61) coincide, so $V$ is $C^1$ with no singular surfaces [P022, p. 564].

---

## 15. Differential inequalities and set invariance (Nagumo-type)

**Where used.** (i) *Two-clock transport*: in the safe region $\varphi_s > \varphi_T$ both time-to-intercept and time-to-target decrease at unit rate under straight optimal play, so the inequality is preserved — "a one-line transport/invariance argument (no Nagumo formalism needed because both functions decrease at the same known rate)" [P077, Corollary, p. 701]. Conversely, P077's Prop. 6 forward-invariance of the shell $\{\|r_i\| \ge \hat\ell\}$ is argued by a limiting-rate + informal Hausdorff sentence, and the archive flags the missing Nagumo/Brežis condition or strict comparison inequality as the proof gap (p. 702). (ii) *Dominance-region confinement*: the moving l-oval never approaches the lifeline under the aim-at-closest-point law, $\dot y_H \ge 0$ with equality iff the evader runs at the tangency point — obtained by differentiating the potential $F(x_H) = 0$ and Cauchy–Schwarz [P102, Lemma 5, eqs. (36)–(40), pp. 9–10]; the moving dominance region is contained in the initial one via a supporting-hyperplane/QP/KKT argument closed with Rockafellar Thm 18.8 [P041, Thm 7(b), pp. 6–7]. (iii) *Oval invariance in implementation*: under the oval-based interception strategy the attacker is confined to the Cartesian oval $\mathcal{R}_i$ (Lemma 3), extended to two defenders by set intersection (Thm 1) [P060, p. 4]. (iv) *CBF forward invariance*: reciprocal-form CBF $B_j = b_j^2$ with safeguarding control $u_j^s = -c_j B^\top\nabla B_j$ proves forward invariance of $\mathrm{Int}(C_j)$ whenever the nominal strategy is merely bounded — no QP needed [P046, Lemma 1, eqs. (6)–(9)].

---

## 16. Control barrier functions (CBF)

- *Safety layer + game solver composition*: CBF filter (6)–(9) with a feasibility condition relaxing Cohen–Belta; the nonquadratic $\tanh^{-1}$-integral game cost (13) yields saddle strategies (14)–(16) bounded by construction ($|u_j^{n*}| < \lambda_j$), which is exactly what Lemma 1's invariance proof consumes; Theorem 1 gives the sufficient condition (29) for closed-loop stability with the safety layer [P046, pp. 5440–5443].
- *CBF-QP filters on top of geometric games*: CBF-QCQP filter (eqs. (46)–(49)) as the safety layer of the Voronoi-coverage pursuit [P013]; standard CBF-QP stack for collision-free ASV reach–avoid, layered under the guidance-point reduction of underactuated kinematics [P096, Secs. II–III].

---

## 17. Matching-based coalition and task-allocation methods

- *Value-annotated subgames + bipartite matching*: MPME decomposed into 1P1E/2P1E/3P1E subgames with exact values; assignment = weighted bipartite matching with online rematching; at most 3 pursuers needed in 3D [P033, Remark 4, Thms 1–3]; heterogeneous 3D version with ES certificates and the "at most three pursuers" degeneration collapsing coalition space to $O(N_p^3)$ [P103, Secs. 3–4]. Barrier-measure-driven assignment [P075]. Convex-domain barriers + 0-1 ILP assignment; "every multiplayer barrier segment depends on at most two pursuers" [P100, Thms 1–4, Lemma 3, Algorithm 1].
- *Assignment inside the value*: $V(\mathbf{x}) = \max_\iota y_{s_\iota}(\mathbf{x})$ over feasible assignments $\mathcal{A}_\iota$ — hybrid continuous guidance + discrete assignment without solving any PDE [P037, Sec. III]. Matching-based CTF: reduction to 2D-1A/1D-1A subgames, $C^1$ value satisfying HJI (Thm 1 + Cor. 1), and maximum bipartite matching with conflict graph (MBMC) solved by sequential matching [P089, Secs. III–IV, eqs. (4)–(8)].
- *Team-vs-team exactness via combinatorics*: local-game decomposition into $N_D^2$ LGRs; intruder guarantee $Q_{LG} = \max_G \sum_{k \in G}\max\{q^k, 0\}$ computed in $O(N_D^4)$ as maximum-weight independent set on a circular-arc graph; defender policy closes the bound into a saddle point [P015, eqs. (6)–(7) vs (10), pp. 3–6].
- *Alternatives*: hedonic-game coalitions with single-peaked-at-one preferences (Nash-stable partition exists; convergence in $\le |A|(|A|+1)/2$ iterations) [P045, Thms 1–2, Def. 4, p. 1537]; minimum-makespan distributed allocation via isochron capture conditions + conflict graphs [P054, Thm 1]; k-WTA dynamical networks with load reassignment [P084, eqs. (7)–(10), Algorithm 1]; pairwise matching for limited-lifetime lifeline multiplayer extension [P102, Sec. 7]; LLM-driven task assignment with analytic correction modules [P059, Defs. 3–5, Algorithms 2–4].

---

## 18. Mean-field and LQ tools (brief)

- *Two-level LQ differential games*: multipopulation SDE/ODE model with HJB backward PDE systems for three game protocols; ansatz-reduced coupled backward ODEs [P010, eqs. (1)–(5), Defs. 1–6].
- *Nonzero-sum LQ TAD with anomalies*: relative-coordinate single integrators, Riccati feedback masked by visibility matrices, anomaly parameter $\mu$ scaling the quadratic cost; inverse-game-theory construction of costs realizing given feedback as NE [P090, eqs. (1)–(20), Thms 1–2].
- *Value iteration for MPDGs*: best-response HJB equation (eq. (10)) with cooperative sequential adaptation and convergence to $V_i^*$ [P085, Lemma 2, Thm 1, pp. 692–693].
- *Hierarchical mean-field MARL*: pairwise decomposition $Q^k(s,a) = \frac{1}{\mathcal{N}^k}\sum_j Q^k(s,a^k,a^j)$ (eq. (1)) and group collapse (eq. (11)) [P110].
- *Min–max Q-learning as matrix-game learner*: per-stage $2\times 4$ payoff matrices learned by minimax Q-learning inside an exact zero-sum reduction with player-count-invariant features [P078, Secs. 2–3].

---

## Symbol conflicts observed

For later merge into `latex_notation.md`. Concept → symbols (archive ID first use):

- **Speed ratio**: $\alpha = v_T/V_A < 1$ [P022, eq. (1)]; $\alpha = v_A/v_D < 1$ [P011, eq. (1)]; $\alpha = v_E/v_P$ (written $a$) [P002, eq. (3); P031 eq. (2.3); P094, p. 3]; $\alpha_{ij} = v_{P_i}/v_{E_j} > 1$ [P100, Ass. 4; P103; P058]; $\alpha_{ji} = v^*_{A_j}/v^*_{D_i}$ (attacker-to-defender) [P091, p. 3]; $\beta_i = v_{P_i}/v_E > 1$ [P044, eq. (4)]; $\nu_i = v_{D_i}/v_A > 1$ [P050, eq. (1b); P017]; $\nu = v_E/v_P$ [P023, eq. (1); P071]; $\mu_{ji} = 1/\alpha_{ji}$ [P091, Thm 3]; $\lambda = V_P/V_T$ [P013, eq. (2)]. **Four different orientations coexist** — never reuse $\alpha$ without orientation.
- **Barrier**: $B$ = barrier set [P073, Lemma 1 vs. script $\mathscr{B}^i$ = BES plane, eq. (4) — same letter, two meanings, flagged in the archive]; $B(\mathbf{x}) = \max\{B_1, B_2\}$ barrier function [P035, eq. (21)]; $B_j$ = CBF [P046, eq. (7)]; $\mathcal{B}$ = barrier curve [P099, P102].
- **Hamiltonian vs. geometry**: $H$ = Hamiltonian [P022 eq. (8); P061 eq. (7)]; $\mathbf{H}_j$ = half-space [P001, eq. (1), p. 108]; $h(x)$ = target-defining convex function [P048, eq. (1); P018's $h_i$ = value functions eq. (7)].
- **$\delta$**: non-anticipative strategy map [P041, eq. (3)]; $\delta$-Apollonius circle (time-shift $\delta$) [P101, Def. 4.1]; capture distance $d_s$ [P002]; turret startup time $\Delta$ [P007].
- **$\rho$**: capture radius [P050 eq. (11); P091; P108 thrust bound $\rho^{P},\rho^{E}$]; sensing radius [P062, P067 $R^\alpha$, $\rho_s$]; intruder sensor range [P071 $\rho_A$, $\rho_T$].
- **Capture radius otherwise**: $l$ [P041; P094; P102]; $r$ [P031 A4; P080 (3); P098]; $r_i$ [P103; P106]; $r_c$ [P113]; $r_F, r_D$ [P034].
- **$E$**: evasion space [P073, eq. (4); P058]; energy function $E = kA + \|x_e - x_p\|^2$ [P113, Thm 3]; evader subscript [throughout]; $E$ = expected payoff [P051, p. 2].
- **$T$**: target set [P050, P041 $\mathcal{T}$]; terminal time $t_f$; capture time $T_i$ [P019, p. 561]; target player T [P022]; TPBVP.
- **$J$**: payoff [P044 eq. (2)]; $J_1, J_2$ branch values [P019 eq. (5)]; $J_P, J_G$ = pursuer/evader-side terminal payoffs [P102, eqs. (6)–(11)]; $J_{j,1}, J_{j,2}$ offensive/defensive payoffs [P091, eqs. (5), (7)].
- **$V$**: value function [P022 eq. (6)]; evader's evasion region $\mathcal{R}_e$ vs. pursuer winning region $\mathcal{W}_P$ [P102]; $V_i$ = max speeds [P066, eq. (1)].
- **$I$**: interception point [P022, eq. (39); P096 $\mathbf{I}^*_{k1}$ eq. (21)]; identity matrix [P027]; information set $I_P(t)$ [P062, P064]; index set $I$ [P019, Lemma 1].
- **$\Gamma$**: singular/dispersal surface [P019, Lemma 7]; boundary curves $\Gamma_1, \Gamma_2, \Gamma_3$ in $\mathcal{W}_P/\mathcal{W}_E$ [P102, eqs. (70), (73), (81)]; sightline/gamma heading [P007].
- **$\phi$**: heading angle [P011, P026, P091]; potential function $F(\mathbf{z})$ [P102, eq. (25)] vs. $f_{ij}$ potential [P058, eq. (2)]; $\phi(x,y) \le 0$ target-set function [P031, eq. (2.1); P048, eq. (1)] — three distinct "potential/level-set" meanings.
- **$S$**: safe/reachable set $S_e(t)$ [P066, eq. (3)]; Voronoi cell $S_e$ [P113, Sec. 3]; terminal set [P044, eq. (42)]; $s_j^*$ abscissa of optimal target point [P091, eq. (9)].
- **$\omega$**: line-of-sight angle [P091, Thm 3]; hybrid blend weight [P003, eq. (5)]; angular rate [P007, P114].
