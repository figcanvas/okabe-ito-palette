"""Okabe-Ito (Wong) colorblind-safe palette for matplotlib and seaborn.

Usage:
    from okabe_ito import OKABE_ITO, use_okabe_ito
    use_okabe_ito()            # set the matplotlib color cycle once
    use_okabe_ito(n=3)         # or only the recommended first three colors
"""
OKABE_ITO = {
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "bluish_green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "reddish_purple": "#CC79A7",
    "black": "#000000",
}

# Order to take colors in when a figure has fewer than eight groups;
# yellow comes last because it is nearly invisible on white (1.32:1).
RECOMMENDED_ORDER = ["#E69F00", "#0072B2", "#009E73", "#D55E00", "#56B4E9", "#CC79A7", "#000000", "#F0E442"]


def okabe_ito(n=8):
    """Return the first n colors in the recommended order."""
    if not 1 <= n <= 8:
        raise ValueError("Okabe-Ito has 8 colors; use a different palette for more groups.")
    return RECOMMENDED_ORDER[:n]


def use_okabe_ito(n=8):
    """Set the matplotlib color cycle (also used by seaborn) to Okabe-Ito."""
    import matplotlib.pyplot as plt
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=okabe_ito(n))


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    use_okabe_ito()
    fig, ax = plt.subplots(figsize=(6, 3))
    for i in range(8):
        ax.plot([0, 1], [i, i + 0.5], linewidth=3, label=RECOMMENDED_ORDER[i])
    ax.legend(fontsize=7, ncol=2)
    fig.savefig("okabe-ito-demo.png", dpi=200, bbox_inches="tight")
