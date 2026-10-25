# Literature Database — research-status map (lsh-game-paper library, 102 papers)

Narrative complement to `references/literature_index.md` (topic × paper lookup) and
`papers/manifest.json` (bibliographic data). Read this file first to understand what the
library covers, where the frontier stands, and where the gaps are. Every paper claim below
cites its PXXX archive; synthesis claims are marked [inference]. Verified counts (2026-10-11):
`papers/` holds 113 records — **101 full per-paper archives** (56 T1, 41 T2, 4 T3) plus 12
VARIANT stubs (P004/P016/P020/P024/P030/P032/P042/P043/P063/P068/P074/P109, which resolve to
their primaries); manifest items P081, P088, P116, P117 have **no full archive** (Section 5).
The "102" in the header follows the skill brief; use 101 as the exact count when citing sizes.

## 1. Coverage overview

**What the library is.** A curated archive of 117 items on differential-game /
pursuit-evasion / reach-avoid / target-defense research, of which 101 have deep per-paper
archives (biblio, contributions, theorem-level results list, verification notes, open
problems, citation value; see any PXXX.md). Temporal span 2009–2026 (P001, P039, P113 are the
oldest full entries) but heavily front-loaded to the current frontier: 48 of 101 archives are
2024–2026, and 2024 alone contributes 19. Tier mass: 56 T1 (Automatica 11; IEEE TAC ~10
across header variants; TAES 4–5; IEEE TRO 3; TCYB 4; TSMC 4; L-CSS 4; TMech, TCST, TII,
TIE, TCDS, TASE, TNSE, RAL 1–2 each), 41 T2 (ACC 6, CDC 4, AAAI 4, arXiv 6, ECC, AIAA,
Ocean Engineering 2, Neurocomputing 2, Nonlinear Dynamics 3, Frontiers, IJC 2, EJC, CJA,
Science China 2, JAIS, IJCAS, Unmanned Systems), 4 T3 (P001, P087, P101 — legacy or
unresolved venue, still full archives). The core is control-theory venues; an AI-conference
fringe (AAAI main tracks P051, P066, P110, P003; AAAI-SSS) and an applied-marine fringe
(P060, P072, P096, P107) are deliberately present.

**Strengths by problem class × method** (counts from `literature_index.md`): the library is
overwhelmingly an *analytic geometric game theory* library — Apollonius-family tools appear
in 53 archives, reach-avoid formulations in 43, barrier/game-of-kind analysis in 36,
multiplayer PE in 34, HJI/viscosity machinery in 23 (mostly as *verification*, not
computation), target defense in 25, task assignment in 12, RL/learning in 12, 3D settings in
10, perimeter defense in 10, CTF in 8, lifeline in 5, obstacles in 4, partial information in
4–6, reconnaissance in 4. Flagships per class are named in Section 2.

**Research groups / lineages visible in the archives** [library-evidenced from bylines and
funding lines; group-level "known for" characterizations are supported by the cited archives]:

- **AFRL/AFIT (Ohio) line** — Garcia, Casbeer, Pachter, Von Moll, Weintraub (Control Science
  Center WPAFB + AFIT). P022 (canonical active-target-defense closed form), P034/P038
  (capture-the-flag), P035/P036 (2P1E barriers, football), P037 (N-vs-M border defense),
  P044 (field tutorial + 2P1E template), P092 (surveillance of faster target), P086 (turret +
  mobile defender, with the DCIST line). Signature: complete closed-form Isaacs solutions
  with full HJI verification, orthogonal-bisector aimpoints, two-sided PMP.
- **Tsinghua analytic-barrier school** — Yan, Shi, Zhong (+ Deng R.; + Duan SJTU, Bullo
  UCSB, Ji Xiangyang). P099 (2D1A barrier), P100 (TRO, barriers + ILP assignment in convex
  domains), P101 (evader-side cooperation, δ-Apollonius), P102 (lifeline with limited
  lifetime), P103 (Automatica, 3D heterogeneous matching + evasion space), P104 (the
  library's M-RA review), P105 (Automatica, Dubins homicidal-chauffeur reach-avoid via
  pursuit enclosure functions), P106 (TAC, polygonal obstacles), P073 (3D barrier), P047
  (car-defender heading tracking), P018/P019/P021 (ellipses, value functions, convex CTF),
  P061 (damped double integrator). Signature: closed-form barriers → coalition reduction →
  0-1 ILP/matching assignment; function-based dominance regions; "geometric method validated
  by HJI" doctrine (P104 Sec. 3).
- **DCIST line (Shishika GMU / Kumar UPenn / Dorothy ARL / Maity UNCC / Von Moll AFRL)** —
  P015 (RA-L, local-game decomposition, provable team strategies), P083 (GameSec review of
  perimeter defense: MM/MIS/LGR taxonomy), P023 (one-Apollonius-circle Lyapunov containment),
  P025 (aerial defender vs ground intruder), P065 (sensing-limited evasion building block),
  P071 (sequentially arriving intruders), P086 (hybrid turret+defender). Signature:
  assignment/combinatorial lifting of small-game barriers, satisficing geometric guarantees,
  sensing-constrained engagements.
- **MSU/Purdue worst-case perimeter defense** — Bajaj (now Purdue), Bopardikar, Torng (+AFRL):
  P005 (ACC, line), P006 (CDC, cones), P007 (turret with startup time), P008 (T-RO,
  multivehicle cones), P009 (L-CSS, randomized). Signature: competitive-ratio analysis,
  impossibility thresholds, Yao-style randomized lower bounds — the only online-algorithms
  lens in the library.
- **Bakolas UT-Austin group** — Lee, Selvakumar: P048 (weighted cooperative attackers),
  P049 (reconnaissance game), P050 (TAC, viscosity/parametric-optimization verification of
  geometric target guarding), P077 (log-risk feedback evasion), P078 (min-max Q-learning),
  P098 (compact convex targets). Signature: rigorizing geometric methods via parametric
  nonlinear programming (Fiacco/SOSC, Clarke subdifferentials) and metric-projection barriers.
- **Beihang line** — Yan Rui (moved from Tsinghua), Dong Xiwang, Liu Hao, Ma Zihao (+Wen
  Guanghui SEU, +Lewis): P057 (CJA anti-UAV position paper), P058 (TCYB, multiplayer CTF
  pursuit), P059 (TII, TARA-LLM task assignment), P062 (TAC, 3D partial-information
  cooperative capture), P064 (TMech, heterogeneous partial information + quadrotor trials),
  P067 (TCST, deployment under partial information). Signature: the library's center of
  gravity for *partial/asymmetric information* and the LLM entry point.
- **BIT complex-systems cluster** — Deng Fang, Liang Li, Huang Weiwen, Xu Ningsheng (+Zha
  Wenzhong CETC, Chen Jie): P041 (Automatica, non-anticipative dominance regions),
  P056 (territorial-constrained defender), P087 (fishing-game barrier), P093/P094 (two-lifeline
  games), P095 (obstacle + partial information), P112 (three-player lifeline). Signature:
  explicit-policy barrier construction as an HJI substitute; lifeline problem family.
- **Tongji adversarial-information group** — Yi Peng, Fang Hongwei, Li Xiuxian, Meng Min,
  Hong Yiguang, Chen Jie: P027 (IBR+ADMM imperfect observation + motion capture), P028
  (TASE, robust safe-region estimation), P029 (level-k Bayesian rationality), P095 (with
  Tokyo Tech), P115 (Science China survey of adversarial decision making). Signature:
  estimation-coupled games, behavioral rationality, receding-horizon coalition solving.
- **Peking University isochron school** — Li Shuai, Wang Chen, Xie Guangming: P052 (ACC,
  dimension-heterogeneous Apollonius), P053 (TAC, isochron solution, 16-case taxonomy),
  P054 (TAC, minimum-makespan distributed allocation). Signature: isochrone geometry for
  heterogeneous second-order players.
- **ECUST/Fudan networked-games group** — Wang Jiali, Tang Yang, Ho Daniel, Jin Xin: P089
  (TCDS, matching-based CTF), P090 (TAC, anomalous defenders, inverse game theory),
  P091 (TCYB, all speed ratios with capture radii). Signature: LQ/networked formulations,
  visibility-graph information structures.
- **Smaller but distinct nodes**: NWPU (Xia Yuanqing P013 Voronoi+CBF swarm capture; Yuan
  P111 impulsive TAD RL; Cui P014 herding channels; Pan/Yuan P070 relay pursuit), Shanghai
  Jiao Tong (Zhang Yun P085 value-iteration ADP; Lin P060 USV theory-to-hull), Harbin
  (P055 speed-varying TAD; P108 satellite PE), KTH (Hu Xiaoming: P046 CBF+ADP PE, P114
  bio-inspired unicycles), Stanford/Berkeley legacy (P039/P040 HJI CTF; P113 Voronoi
  pursuit), Cranfield (P045 hedonic task allocation), CICESE (P076 FOV escape), Ocean
  Univ. China (P072 USV DRL), Dalian Maritime (P096, P107), Adelaide (P066 area-optimal
  pursuit), CASIA/KAIST (P051 imitation), SYSU (P084 distributed k-WTA; P110 mean-field RL),
  HUST/SCUT (P079 reconnaissance RL).

## 2. State of the art by problem class

### 2.1 1v1 pursuit–evasion & geometric foundations
*Solved.* The simple-motion 1v1 canon is completely settled and repeatedly re-verified:
state-feedback saddle-point solutions with C1 values and HJI certificates (P022 two-cutters
template; P044 Theorem 1–3 workflow); Apollonius-circle dominance geometry and its
generalizations — Cartesian ovals for nonzero capture radius (P094, P080, P082), Apollonius
spheres in 3D (P013, P033, P075, P002), isochrones for damped double-integrator pursuers
(P053, P054, P061), dimension-heterogeneous circles (P052), limaçons under obstacles (P069).
Rigorization is itself a finished sub-field: the geometric solution of multi-defender
target-guarding is proven to solve the HJI equation for arbitrary convex targets (P031) and
via viscosity/Clarke-subdifferential arguments with exact differentiability characterization
(P050); non-anticipative dominance regions with obstacles are proven reachable-set-exact
(P041). Modern additions: Lyapunov containment "one Apollonius circle is enough" (P023),
time-optimal escape from a conical FOV with five singular surfaces and a no-barrier
speed-ratio criterion (P076), and the intermittent-sensing evasion catalog with elliptic-
integral boundary riding and a Stackelberg equilibrium over the sensing horizon (P065).
*Open.* Focal-surface construction beyond local patches (P019, explicitly deferred);
singular-surface resolution in degenerate configurations (P023 App. A, answers unresolved);
faster evaders require multi-pursuer cooperation and are unsolved in general (P023, P104 §7.4);
feedback (non-open-loop) robustness of optimal evasion when the opponent deviates (P065
Remark 4); strategies for region R_II ("might be caught") of the damped game (P061).

### 2.2 Multiplayer reach-avoid games (the library's core)
*Solved.* For simple motion with pursuers at least as fast: closed-form barriers for 1v1,
2v1 (P099, P100, P036, P077-style partitions), arbitrary coalitions (P100 Theorems 1–4),
and 3D spherical-patch barriers up to four players (P073); coalition degeneracy theorems —
at most two pursuers matter per evader in 2D (P100, P105) and at most three in 3D (P103,
P033) — collapse assignment complexity from exponential to polynomial; evasion-space/
function-based dominance machinery handles heterogeneous speeds and nonzero capture radii
(P103, P091); barrier-measure-driven assignment via bipartite matching (P033, P075) or 0-1
ILP with NP-hardness proof and a 1/3-approximation Sequential Matching Algorithm (P103,
P104 §5). Value-function-grade results exist for small teams: two cooperative attackers with
singular-surface analysis (P019), 2v1 simultaneous capture with verified values (P035),
3D subgame values + teaming (P033), football barrier (P036). Cooperative pursuit laws with
capture proofs: Voronoi area-descent (P113), covering + CBF layer for slower UAVs vs a
faster intruder (P013), relay pursuit with switching regions (P070), enclosure-region
pursuit for Dubins pursuers (P105). *Standard tools*: Apollonius/Voronoi/function-based
dominance regions, semipermeable barriers, ES tangency tests, weighted bipartite matching,
receding-horizon rematching. *Open* (mostly consolidated in P104 §7 and P057): fast evaders;
sequential capture (myopic barrier constructions, dynamic VRP structure); spatio-temporal
coupling between assigned pairs (collisions, shared environment); instantaneous-heading
assumption; differentiability sets of 3D values — barrier/singular surfaces unhandled (P103);
dispersal surfaces in bounded 3D domains; guarantee-level multiplayer Homicidal Chauffeur
beyond enclosure sufficiency (P105).

### 2.3 Target defense / TAD & turret defense
*Solved.* The three-player active target defense differential game is the library's most
complete solved object: full Game-of-Kind + Game-of-Degree closed form in R6 (P022), the
game-of-degree in the capture region excepted. Extensions now cover: speed-varying
second-order plants via an average-speed-ratio reduction (P055), nonzero attacker capture
radius via the Apollonius oval + limit interception curve (P080), both radii nonzero under
equal speeds (P082), impulsive CW-dynamics spacecraft engagements (P111), multiple defenders
vs one attacker with heterogeneous weights under sequential exogenous capture order (P048),
convex targets of arbitrary shape (P031, P050, P098), turret defense with finite range and
startup time as a TRP-with-time-windows equivalent (P007) and turret+mobile-defender hybrid
dominance regions (P086), multi-agent TAD as LQ games with anomalous defenders and inverse-
game-theory equilibria under visibility constraints (P090). Learning-side attack guidance
that converts defender turn-rate constraints into wins exists (P026). *Open*: the
attacker-winning region analysis is unsolved in essentially every member of the lineage
(P022 p. 555, P050 §II-C, P082); focal surfaces (P019); 3D TAD with nonzero radii (P082
Remark 7); multi-target/multi-TAD tasking (P080, P086); dispersal handling in the turret
game requires communication assumptions (P086); rigorous saddle-point verification for
asymmetric-thrust orbital games (P108 — PMP candidates only).

### 2.4 Perimeter defense
*Solved.* Two coexisting paradigms. (i) Game-theoretic, perimeter-confined defenders:
1v1 barriers on circles and arbitrary convex shapes (involute construction at ν=1; P083
Items 3–5), 2v1 pincer regions, and the LGR decomposition giving a genuine intruder-team
lower bound and an equilibrium sandwich for a class of configurations (P015, P083 Items
10–12); 3D aerial-defender-vs-ground-intruder geometry (P025); cooperative team strategies
with weighted intruders reducible to the Hungarian algorithm (P083 Item 13). (ii) Worst-case
online defense against arbitrary intruder release streams: sharp competitive-ratio phase
transitions on a line and in cones, impossibility regimes, optimal sweeping algorithms,
TRP-TW equivalence and a 2-approximation for turret startup (P005–P008), and randomized
lower bounds (2 and 4/3) with algorithms beating the deterministic frontier (P009).
Learning hybrid: analytic Apollonius Nash payoffs as terminal rewards for MARL border
defense under late detection (P017). *Open* (P083 §5, verbatim seeds): defenders leaving
the perimeter (sequential capture ⇒ vehicle routing + lure/offense behaviors); fast
intruders ν>1 (degenerate under point capture + perimeter confinement; remedy = capture
radius); partial information (neither patroller teams nor learned communication "directly
addressed the issue of unseen intruders"); nontrivial regime characterization when
N_A > N_D.

### 2.5 Capture-the-flag
*Solved.* The full arc from numerical to analytic to multiplayer: founding two-phase HJI
formulation with sequential composition of reach-avoid sets (P039), journal-grade numerical
treatment with Elliott–Kalton values (P040), closed-form attack/retreat values with HJI
verification (P034), the transition phase as an inter-phase optimization (P038), complete
solution of multi-defender CTF with general convex flag/return regions via a quasi-convex
program and a two-defender sufficiency theorem (P021), multiplayer pursuit with half-plane
regions, heterogeneous speeds, nonzero capture radii and via-point potential functions
(P058), and alliance-level matching with MADDPG comparison (P089). *Open*: unequal speeds
and positive capture radii change all closed forms (P038 §VI.A); flag regions and non-point
objects (P038, P089 Remarks); 3D convex flags (P058 §VII); obstacles in CTF; the
attack-transition-retreat structure for teams.

### 2.6 Lifeline and reach-a-line games
*Solved.* Isaacs' lifeline problem rebuilt with modern tools: limited-lifetime lifeline with
l-Apollonius evasion region and OTP construction (P102), two-lifeline game with Cartesian-
oval reachable regions and closed-loop pursuit (P094), one superior pursuer vs many evaders
with delay-aware barriers and cooperative sacrifice analysis (P093), three-player barriers
via sub-game bonding (P112). *Open*: multiplayer lifeline beyond assignment schemes; complex
dynamics and general (non-half-plane) domains (P102 §7); pursuit-order optimization is
factorial by exhaustive enumeration (P093).

### 2.7 Reconnaissance / penetration–return games
*Solved.* Two-phase (approach–retreat) reconnaissance with half-planar target and retreat
regions, closed-form values with HJI verification (P049); territorial-constrained defenders
solved by explicit-policy/Apollonius geometry (P056); learning-based multi-stage
reconnaissance with GAN-predicted defender trajectories under unequal sensing (P079). *Open*:
rigorous optimality of the retreat point is unproven (P049 item 1); chattering under myopic
phase switching (P049); accuracy–duration trade-off in learned policies (P079); obstacles
+ reconnaissance with visibility (announced in P106 §7).

### 2.8 Sensing-limited / partial- and asymmetric-information games
*State.* The fastest-growing class (≥8 archives since 2022). Building blocks: two-phase
deployment/capture decomposition with a partial-information value dominating the
complete-information value at detection (P062); speed-ratio thresholds (α ≥ √2) for provably
safe Apollonius pursuit under sensing limits (P064); deployment optimization with a
fuzzy-region phase transition at R^α = (1+α^{-1})l/2 (P067); robust safe-region estimation
with 3σ guarantees and minimal-coalition formation from Cartesian-oval geometry (P028);
Kalman-belief virtual-evader chance-constrained games with IBR/ADMM receding-horizon
solving on hardware (P027); sequentially arriving sensing-enabled intruders with an
engagement-surface device (P071); obstacle-plus-partial-information target defense with
guaranteed angular gains (P095); Kalman-filter games with Bayesian rationality-level
inference (P029); visibility-masked LQ TAD with anomalous teammates (P090); inter-sensing
evasion windows (P065). *Open*: optimal pursuer deployment under partial information in
multiplayer games (P062 item 2); cooperative capture among sensing-limited pursuers
(P064 §7); strategies independent of the evader's observed input (P062 item 1); validated
models of intruder behavior in the blind phase (P071 footnote 1 concedes assumption);
identifiability of opponent models (P029 Remark 4); the full costly-active-sensing game —
timing + heading while blind — is explicitly future work (P065).

### 2.9 Obstacle environments
*Solved.* Isochrone-intersection dominance with polygonal obstacles — every isochrone piece
is a circular arc about a known center, boundary pieces are limaçons/vertex-centered circles,
with singular-surface architecture (P069, Automatica); reach-avoid winning regions with
general polygonal obstacles via goal-covering polygons, expanded Apollonius onsite regions,
and ESP-anchored safe distances, fused into receding-horizon allocation (P106, TAC);
obstacle-aware non-anticipative dominance regions (P041); tangent line-segment obstacle in
partial-information defense (P095); virtual channels around Dubins guide paths extending
barrier analysis to non-convex domains (P014); penetration with convex/non-convex target
regions and yaw constraints (P107). *Open*: capture radii > 0 combined with obstacles is
"not straightforward" (P106 Remark 1); completeness of the sufficient winning regions
(P106 is explicitly conservative); general obstacle configurations beyond single corners
(P041); evasion strategies that exploit obstacles to hide (P106 notes obstacles shield
capture but neither side's strategy exploits hiding).

### 2.10 Learning-based approaches
*State.* Twelve RL/learning archives, none of which replaces the analytic core; the
dominant pattern is *learning around a geometric skeleton*: Apollonius-partition state
features with ordinal-potential-game NE existence and finite-time capture certificates
(P097); game-theory-assisted MAPPO with analytic subgame values as terminal rewards (P017);
hybrid classical-guidance + PPO with curriculum (P003); CBF safeguarding layer composed with
ADP game solvers under unknown dynamics (P046); TD3 attacker with defender-aware shaped
rewards (P026); Hamilton-regularized MATD3 for impulsive spacecraft TAD (P111); MA-POCA
multi-USV pursuit in Unity3D obstacle fields (P072); fuzzy actor-critic with 3D Apollonius
spheres (P002); min-max Q-learning that learns payoff-matrix entries of a player-count-
invariant matrix-game abstraction (P078); latent strategy representation + exploitability
indicators for imitation (P051); hierarchical mean-field MARL (P110); value-iteration
cooperative adaptive optimal control for N-player games with incomplete information (P085).
*Open*: essentially no convergence/optimality theory anywhere in this class (P111
"heuristic loss-shaping"; P110's approximation error unbounded; P078 flags multi-agent
Q-learning instability); observation noise robustness (P111 Fig. 14 shows failure at
moderate noise; P097 assumes none); reward shaping with feasibility guarantees (P078 §7);
sim-to-real and adversarial co-evolution stability (P072).

### 2.11 Task assignment & multi-robot allocation
*Solved.* Hedonic-game decentralized allocation with Nash-stability existence and O(n_a^2)
convergence (P045); minimum-makespan distributed allocation over isochron-annotated
heterogeneous pursuit games (P054); game-outcome-annotated 0-1 ILP and matching with
provable capture-count bounds (P100, P103, P033, P089); distributed k-WTA dynamical-network
allocation with load reassignment, validated on wheeled/legged/aerial hardware (P084);
LLM-driven assignment with analytic knowledge prompts and analytic revision modules,
validated on 6 AAVs (P059). *Open*: NP-hardness vs real time — all exact formulations are
APX-hard, polynomial algorithms are 1/N_c- or 1/3-approximations (P103, P104 §5); LLM
latency blocks high-frequency replanning and the claimed 1/2-approximation is "inferred",
not proven (P059 §7); distributed computation with guarantees is announced but absent
(P100 §7); capture-order optimization treated as exogenous (P048); fair head-to-head
benchmarking of decentralized methods (P045).

## 3. Cross-cutting trends

1. **Analytic-barrier renaissance with HJI as verifier, not solver.** The library's
   methodological center: geometric dominance/barrier construction first, then HJI
   verification — canonized as doctrine in P104 (regular equilibrium trajectories of
   simple-motion games are straight lines, so geometry is exact) and executed by P031/P050
   (rigorization), P023 (containment instead of barriers), P087/P112/P056 (explicit-policy
   method). Numerical HJI (P039, P040, P113 comparisons) is now the minority method,
   retained for rich dynamics.
2. **Two-layer architecture: local differential game + combinatorial teaming.** Small-game
   barriers/regions feed matching/ILP/set-selection for team-level play — articulated as
   the field's recipe in P083, instantiated by P015 (LGR + equilibrium sandwich), P100,
   P103, P089, P037, P033, P075, P106. The DCIST and Tsinghua lines converged on it
   independently [inference from archives].
3. **Coalition-reduction degeneracy theorems as the scaling engine.** "At most two pursuers
   matter" in 2D (P100, P105), "at most three" in 3D (P103, P033), "two defenders suffice"
   for convex CTF (P021 Thm 15), "one Apollonius circle is enough" (P023) — these turn
   exponential team games into polynomial objects.
4. **RL with geometric priors / hybrid analytic-learning.** P017, P097, P003, P046, P026,
   P111 all inject Apollonius/CBF/PMP structure into learning pipelines; P089 and P078
   benchmark learned vs analytic play, finding parity or context-dependent advantage — the
   library's evidence says learning earns its keep on partial information, dynamics, and
   scale, not on small full-information geometry [inference from P017, P078, P089, P111].
5. **LLM-driven planning entry points.** P059 (TARA-LLM: analytic knowledge as prompts,
   analytic revision of LLM output, hardware demo) and the P057 call for LLM-assisted
   matching; both stress that formal guarantees must come from the analytic layer.
6. **Competitive-ratio / worst-case analysis as a parallel paradigm.** P005–P009 import
   online-algorithms tools (impossibility thresholds, Yao's principle) — the library's only
   non-equilibrium solution concept, positioned explicitly against game-theoretic and
   stochastic-routing approaches (P008).
7. **Partial information as the current frontier.** After the 2020–2021 reviews declared it
   open (P083 §5, P104 §7.5), a wave of 2024–2026 T1 papers attacks it piecewise (P062,
   P064, P067, P028, P017, P090, P079) — but always under specific information graphs;
   no unified partial-information game theory exists in the library [library-evidenced].
8. **Dynamics escalation beyond simple motion, one relaxation at a time.** Damped double
   integrators (P061, P053, P054), Dubins cars (P047, P105, P114), speed-varying forces
   (P055), underactuated ASVs via guidance-point reduction (P096), unicycles with
   centripetal agility bounds (P114), CW/impulsive spacecraft (P108, P111) — each paper
   still solves a 1v1/2v1 core, confirming that multiplayer + realistic dynamics remains
   unsolved jointly (P104 §7.1, P057 challenge 1).
9. **Hardware validation entering the loop.** USV lake trials (P060), quadrotor swarms
   (P064, P067), three-locomotion-mode pursuit (P084), 6-AAV LLM assignment (P059),
   motion-capture AGVs (P027), Unity3D USV (P072) — a recent and uneven trend; most T1
   theory papers still have no experiments [library-evidenced].
10. **Application-domain diversification.** Anti-UAV defense as an organizing application
    (P057), border/boundary defense (P005–P009, P017), marine attack–defense (P060, P072,
    P096, P107), orbital/spacecraft (P108, P111), intelligent vehicles (P080).
11. **Inverse game theory and behavioral models.** Anomalous-teammate cost reverse-engineering
    (P090), level-k rationality with Bayesian inference (P029), imitation-based strategy
    representation (P051) — small but a clear third way between equilibrium analysis and RL.

## 4. Research gaps & opportunities

Consolidated from the archives' own open-problem sections (P057 §7, P083 §5, P104 §7,
P115 §6, and the per-paper Section 7s) plus synthesis. Each item: description — evidence —
difficulty — starting tools from within the library. This section feeds the skill's
novelty_analysis mode: a new paper is credible novelty work only if it lands in one of
these gaps or closes a named caveat.

- **G1. Faster/equal-speed evaders and defectors in multiplayer games.** Nearly all
  multiplayer results assume pursuers strictly faster (P100 Ass. 4, P103 Ass. 2.2, P075
  Ass. 1); faster evaders break dominance-region convexity, the property that underpins
  every barrier (P104 §7.4, P023 §4, P091 Scenario 2, P099 p. 1037 asserts α>1 degeneracy
  without proof). Difficulty: high (geometry changes qualitatively). Starting tools: P091's
  advantage-angle/Cartesian-oval method for faster attackers, P021's quasi-convex two-phase
  program, P036's heterogeneous-speed barrier segments, P023's containment idea.
- **G2. Sequential capture and adversarial routing.** Barriers are myopic — built for
  currently-pursued evaders only; defenders capable of multiple captures face a dynamic VRP
  with luring behaviors, and no multiplayer construction handles it (P104 §7.2; P083 §5
  items 1–2; P093's exhaustive pursuit-order enumeration; P071's arrival-process framing).
  Difficulty: high. Starting tools: P071 (engagement surface + state carry-over), P101
  (δ-Apollonius time-shifted dominance), P005–P009 (competitive lens for arrival streams).
- **G3. Unified partial-information theory.** Every existing result is a bespoke information
  graph (P062 deployment/capture split, P064 detection-based heterogeneity, P067 fuzzy
  region, P017 late-sensing transition, P090 visibility adjacency, P028 estimation-robust
  regions); the reviews demand a framework, not cases (P104 §7.5, P083 §5 item 4, P057
  challenge 4). Difficulty: high. Starting tools: P067's sensing-winning/fuzzy-region
  vocabulary, P062's two-phase value domination, P017's analytic-terminal-reward MARL
  pattern, P027's chance-constrained belief games.
- **G4. Multiplayer games under realistic dynamics.** Dubins/acceleration/energy constraints
  are acknowledged as game-changing and deferred everywhere (P022, P037, P038, P104 §7.1,
  P057 challenge 1, P091 item v). Only 1v1/2v1 cores are solved for non-simple motion
  (P061, P053, P055, P047, P105). Difficulty: high (HJI dimensionality + loss of straight-
  line equilibrium trajectories). Starting tools: P061's isochrone/MRR machinery, P047's
  heading-tracking reduction, P055's average-speed-ratio reduction, P105's forward
  enclosure analysis (the only multiplayer non-simple-motion device in the library).
- **G5. Obstacles with nonzero capture radii and completeness.** P106 leaves
  Cartesian-oval capture radii + obstacles "not straightforward" and its winning regions are
  deliberately conservative sufficient conditions; P041 proves optimality only for a single
  corner obstacle; P095 restricts the parameter space. Difficulty: medium. Starting tools:
  P069 (limaçon boundary algebra), P106 (GCP/ESP constructs), P095 (endpoint-detour gains).
- **G6. Global value theory: singular surfaces, differentiability sets, unproven linchpins.**
  Recurrent, explicitly admitted proof debts: focal surfaces (P019), 3D value
  differentiability sets (P103), R_II region of damped games (P061), permanent-escape proof
  (P054), retreat-point optimality (P049), turret-game state-space partition (P086), γ>1
  assertion in P099. Difficulty: medium-hard, classical-Isaacs skill set. Starting tools:
  P019's m-branch viscosity lemma, P050's parametric-optimization/Clarke machinery, P031's
  implicit-function justification pattern.
- **G7. Scalable, real-time, distributed allocation with guarantees.** Exact allocation is
  NP-hard/APX-complete (P103); approximations are 1/3 or 1/N_c; distributed versions
  sacrifice optimality (P027) or lack proofs (P059's 1/2 claim); LLM latency forbids
  replanning (P059 §7). Difficulty: medium (algorithms + approximation analysis). Starting
  tools: P100's ILP + barrier-annotation interface, P103's SMA, P084's distributed k-WTA
  networks, P045's hedonic convergence analysis.
- **G8. Certified learning for adversarial games.** No archive in the RL class provides
  convergence, equilibrium-quality, or safety guarantees (P111, P110, P078, P097 §7); noise
  robustness is unresolved (P111). Difficulty: high. Starting tools: P017 (analytic subgame
  value as terminal reward — the strongest guarantee-bearing pattern in the library), P097
  (potential-game NE existence + CSCT capture certificate), P046 (CBF invariance throughout
  learning), P078 (matrix-game abstraction with exact discretization).
- **G9. Cross-pair coupling and safety in team execution.** Assignment assumes coalition
  independence; shared-space collisions and trajectory coupling are acknowledged open
  (P104 §7.3), and allocation layers are centralized (P106 §7). Difficulty: medium.
  Starting tools: P096's CBF-QP safety layer over game strategies, P014's virtual-channel
  construction, P027's distributed ADMM.
- **G10. Capture/actuation realism inside the game model.** Capture styles (net/laser/
  collision) are asserted, not modeled (P057 challenge 3); turret slew/startup exists only
  in the competitive line (P007, P086); sideslip/underactuation handled by reduction only
  (P096, P060); energy constraints absent (P084 §7). Difficulty: medium. Starting tools:
  P086's hybrid dominance-region method, P007's TRP-TW equivalence, P060's guidance-point
  + backstepping stack.
- **G11. Opponent modeling and equilibrium over information timing.** Full games with costly
  active sensing (when to look + where to head while blind) are explicitly open (P065 §7);
  level-k inference lacks convergence theory (P029 §7); mixed anomaly teams are unanalyzed
  (P090 Remark 8). Difficulty: medium. Starting tools: P065's Stackelberg-over-horizon
  construction, P029's trajectory-scoring Bayesian update, P090's inverse-game template.
- **G12. Full 3D game theory.** 3D results are games of kind (P073), sufficiency-based
  (P105 is 2D+Dubins), or restricted (P033 plane-goal, P062 partial info); games of degree
  with complete values in R^{3n} are absent (P073 item 1, P082 Remark 7, P092 item i).
  Difficulty: high. Starting tools: P103's ES/tangency machinery, P033's Apollonius-sphere
  subgame values, P073's spherical-patch barrier, P013's projection-ellipse coverage.

## 5. Library gaps (meta)

What the library does **not** cover — the skill should say "outside the library" rather than
overclaim when a query lands here:

- **Numerical HJI/level-set methodology as a subject.** Only P039/P040 (2011/2015) and
  P113's comparisons treat HJI computation; modern solver toolchains (helperOC/level-set
  packages, grid interpolation, warm-starting) are absent. Queries about implementing HJI
  solvers must go outside the library.
- **Mean-field games and mean-field-type control.** Absent as primary subjects; nearest
  neighbors are P010 (multipopulation LQ over graphs) and P110 (mean-field MARL, no MFG
  theory). No MFG existence/uniqueness/numerics archives.
- **Stochastic differential games with noise in the dynamics.** All differential-game
  archives are deterministic; uncertainty enters only through estimation layers (P027, P028,
  P111's noise experiments) or the LQ privacy setting (P085, P090). No stochastic HJI,
  no ergodic MFGs.
- **Security-game / Stackelberg-security-game line (SSG, patrol scheduling).** Covered only
  as context inside P115; no Tambe-style archives.
- **Dubins-car reach-avoid barriers as the main object.** P105 uses Dubins pursuers but via
  forward enclosure functions, not barrier surfaces; P047 is a tracking reduction. The
  classical Dubins PE literature (Isaacs' line, Lewin, circumnavigation) is not archived.
- **Bearing-only / limited-FOV sensing games beyond P076; active-sensing cost games beyond
  P065's subproblem** (its abstract's "sensing boundary" never enters the math — the archive
  flags this).
- **Nonzero-sum multiplayer reach-avoid with heterogeneous objectives** (beyond P048's
  weighted team cost, P090's LQ anomalies, P010's populations).
- **Biological/empirical pursuit literature** beyond P114's modeling citations; no
  experimental-animal or human-subject game archives.
- **Venue gaps**: no Dyn. Games Appl., no GameSec beyond P083, no ICRA/IROS as primary
  venues, no IEEE TAC/Automatica-level MFG or stochastic-game papers, no European groups
  beyond KTH/Cranfield/CICESE/Groningen/Tokyo Tech, and no Israeli groups (Shima, Turetsky,
  Prokopov appear only inside P044's taxonomy and P083's reference list, never as archives).
- **Skipped / unarchived manifest items** — present-but-unarchived; cite only with
  manifest-level confidence, never with archive-level claims:
  - **P081** (Shi et al., "Determination of barrier surface in Target-Attacker-Defender
    game with capture radius for superior pursuer", T2) — no archive file.
  - **P088** (Wang et al., cooperative decision-making for multiple UAVs, Unmanned
    Systems, T2) — no archive file; flagged in the brief as intentionally skipped.
  - **P116, P117** (T3; P117 is the Chinese thesis 多对多协同区域攻防博弈) — no archive
    files; Chinese-language theses, out of the archive pipeline.
- **VARIANT stubs** (duplicate builds of archived papers): P004→P055, P016→P017, P020→P019,
  P024→P037, P030→P029, P032→P031, P042→P041, P043→P044, P063→P062, P068→P067, P074→P073,
  P109→P108. Cite the primary archive only.
- **Known archive-level caveats to respect when citing**: several flagship preprints are
  T2 with unprinted venues or later-journal discrepancies (P015, P025, P036, P061, P098);
  P087's venue was resolved to IEEE-era publication only by external check; P104 contains
  two printed errata (δ-threshold sign, conflict-graph wording) — quote from primary
  sources (P104 §7); P057 is a 4-page position paper with heavy self-citation — cite it for
  the mapping, not for theorems (P057 §7); P115's differential-game section is a shallow
  annotated bibliography (P115 §7). Tier-band judgment calls (e.g., P083 as LNCS T2 despite
  review status) are recorded in each archive's biblio block.
