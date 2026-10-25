#!/usr/bin/env python3
"""simulation_plotting.py -- IEEE-style plotting helpers for lsh-game-paper figures.

Import as a module to get rcParams tuned for IEEE double-column papers, or run
directly to regenerate the style demo figure into assets/.

    from simulation_plotting import ieee_rcparams, TrajFig
    ieee_rcparams()
    ...

Style contract (see references/visualization_guidelines.md):
- column width 3.5 in (single) / 7.16 in (double); font 8pt, labels 8-9pt
- distinguishable in grayscale: line styles carry meaning, not only color
- every axis labelled with quantity + unit; no chartjunk
"""
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

COL1, COL2 = 3.5, 7.16  # IEEE column widths in inches

# player colors (also grayscale-safe via distinct linestyles)
C_P, C_E, C_D, C_A, C_T = "#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#7f7f7f"


def ieee_rcparams():
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "STIXGeneral", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 9,
        "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 7,
        "lines.linewidth": 1.2, "lines.markersize": 4,
        "axes.grid": True, "grid.alpha": 0.3, "grid.linewidth": 0.4,
        "legend.framealpha": 0.9, "legend.edgecolor": "0.8",
        "figure.constrained_layout.use": True,
        "savefig.dpi": 600, "savefig.bbox": "tight",
    })


def new_fig(width=COL1, height=None, aspect=1.0):
    if height is None:
        height = width * aspect
    return plt.subplots(figsize=(width, height))


def save(fig, name, outdir=None):
    outdir = outdir or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
    os.makedirs(outdir, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(outdir, f"{name}.{ext}"))
    print(f"saved {name}.pdf/.png -> {outdir}")


def plot_trajectory(ax, xy, color, label, ls="-", marker_every=20, zorder=3):
    x, y = np.asarray(xy)
    ax.plot(x, y, color=color, ls=ls, label=label, zorder=zorder)
    ax.plot(x[::marker_every], y[::marker_every], color=color, ls="none",
            marker="o", markersize=2.5, zorder=zorder + 1)


def apollonius_circle(p, e, vp, ve):
    """Classical Apollonius circle for P(p) vs E(e), speeds vp>ve.

    Returns (center c, radius r): |x-p|/|x-e| = ve/vp.
    Derivation: Apollonius circle of the two foci with ratio k=ve/vp<1.
    """
    p, e = np.asarray(p, float), np.asarray(e, float)
    k = ve / vp
    c = (p - k ** 2 * e) / (1 - k ** 2)
    r = k * np.linalg.norm(p - e) / (1 - k ** 2)
    return c, r


def demo_apollonius(outdir=None):
    """Regenerate assets/demo_apollonius: P, E, Apollonius circle (capture
    boundary for equal-target-time geometry) and dominance shading."""
    ieee_rcparams()
    fig, ax = new_fig(COL1, aspect=0.85)
    P = np.array([0.0, 0.0]); E = np.array([1.2, 0.8])
    vp, ve = 1.0, 0.7
    c, r = apollonius_circle(P, E, vp, ve)
    th = np.linspace(0, 2 * np.pi, 256)
    ax.add_patch(plt.Circle(c, r, fill=False, color=C_T, lw=1.4, zorder=2))
    ax.fill(c[0] + r * np.cos(th), c[1] + r * np.sin(th), color=C_T, alpha=0.08)
    ax.plot(*P, "o", color=C_P, ms=6, zorder=4); ax.annotate("$P$", P, xytext=(6, 4), textcoords="offset points")
    ax.plot(*E, "s", color=C_E, ms=6, zorder=4); ax.annotate("$E$", E, xytext=(6, 4), textcoords="offset points")
    ax.plot([P[0], E[0]], [P[1], E[1]], "k--", lw=0.6, zorder=1)
    ax.set_aspect("equal"); ax.set_xlim(-1.4, 2.6); ax.set_ylim(-1.6, 2.2)
    ax.set_xlabel("$x$ [m]"); ax.set_ylabel("$y$ [m]")
    ax.set_title(f"Apollonius circle, $v_E/v_P={ve/vp:.1f}$", fontsize=8)
    save(fig, "demo_apollonius", outdir)
    plt.close(fig)


def demo_reachavoid_barrier(outdir=None):
    """Regenerate assets/demo_reachavoid_barrier: target region, dominance
    regions and analytic barrier schematic for a simple reach-avoid game."""
    ieee_rcparams()
    fig, ax = new_fig(COL1, aspect=0.85)
    # target region
    tgt = plt.Rectangle((1.6, 0.6), 0.8, 0.8, facecolor=C_T, alpha=0.25, edgecolor=C_T)
    ax.add_patch(tgt); ax.annotate("$\\mathcal{T}$", (2.0, 1.0), ha="center", va="center")
    # barrier: circular-arc schematic of dominance boundary
    th = np.linspace(-0.55 * np.pi, 0.55 * np.pi, 200)
    bx, by = 0.6 + 1.5 * np.cos(th), 1.0 + 1.5 * np.sin(th) * 0.55
    ax.plot(bx, by, color="k", lw=1.5)
    ax.annotate("barrier $\\mathcal{B}$", (1.15, 1.72), fontsize=7)
    # winning regions
    ax.fill_between(bx, by, 2.1, color=C_E, alpha=0.10)
    ax.text(1.0, 1.95, "$\\mathcal{R}_E$", color=C_E)
    ax.fill_between(bx, -0.4, by, color=C_P, alpha=0.10)
    ax.text(1.0, 0.05, "$\\mathcal{R}_P$", color=C_P)
    # players
    ax.plot(0.2, 0.5, "o", color=C_P, ms=6); ax.annotate("$P$", (0.2, 0.5), xytext=(5, 4), textcoords="offset points")
    ax.plot(1.5, 1.7, "s", color=C_E, ms=6); ax.annotate("$E$", (1.5, 1.7), xytext=(5, 4), textcoords="offset points")
    ax.set_aspect("equal"); ax.set_xlim(-0.4, 2.7); ax.set_ylim(-0.4, 2.1)
    ax.set_xlabel("$x$ [m]"); ax.set_ylabel("$y$ [m]")
    save(fig, "demo_reachavoid_barrier", outdir)
    plt.close(fig)


def demo_metric_curves(outdir=None):
    """Regenerate assets/demo_metric_curves: capture-time distribution +
    success-rate comparison in IEEE style (box + curve panels)."""
    ieee_rcparams()
    rng = np.random.default_rng(42)
    fig, axes = plt.subplots(1, 2, figsize=(COL2, 1.9))
    ax = axes[0]
    data = [rng.gamma(5.0, 0.35 + 0.1 * i, 200) for i in range(3)]
    try:
        bp = ax.boxplot(data, tick_labels=["Apol.", "HJI", "Prop."], widths=0.5,
                        medianprops=dict(color="k"), patch_artist=True)
    except TypeError:  # matplotlib < 3.9 uses `labels`
        bp = ax.boxplot(data, labels=["Apol.", "HJI", "Prop."], widths=0.5,
                        medianprops=dict(color="k"), patch_artist=True)
    for patch, col in zip(bp["boxes"], [C_T, C_D, C_P]):
        patch.set_facecolor(col); patch.set_alpha(0.4)
    ax.set_ylabel("capture time [s]"); ax.set_xlabel("strategy")
    ax = axes[1]
    eps = np.linspace(0.5, 1.0, 25)  # speed ratio ve/vp
    for ls, col, lab in (("--", C_T, "Apollonius"), ("-.", C_D, "HJI"), ("-", C_P, "Proposed")):
        ax.plot(eps, 1 - 0.8 * (eps - 0.5) ** 2 - 0.12 * (lab == "Apollonius") - 0.05 * (lab == "HJI"),
                ls=ls, color=col, label=lab)
    ax.set_xlabel("speed ratio $v_E/v_P$"); ax.set_ylabel("success rate")
    ax.set_ylim(0.4, 1.02); ax.legend(loc="lower left")
    save(fig, "demo_metric_curves", outdir)
    plt.close(fig)


if __name__ == "__main__":
    demo_apollonius()
    demo_reachavoid_barrier()
    demo_metric_curves()
    print("demo figures regenerated. Import ieee_rcparams() in your own scripts.")
