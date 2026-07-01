"""
===========================================================
AstroLens AI
Visualization Module
===========================================================
Creates publication-quality plots
===========================================================
"""

import os
import matplotlib.pyplot as plt

from config import (
    FIGURE_DIR,
    FIGURE_DPI,
    SAVE_PLOTS,
    SHOW_PLOTS
)


def plot_lightcurve(lightcurve):

    plt.figure(figsize=(12,5))

    plt.scatter(
        lightcurve.time.value,
        lightcurve.flux.value,
        s=2,
        color="black"
    )

    plt.xlabel("Time (Days)")
    plt.ylabel("Normalized Flux")
    plt.title("Preprocessed TESS Light Curve")

    plt.grid(alpha=0.3)

    if SAVE_PLOTS:

        plt.savefig(
            os.path.join(
                FIGURE_DIR,
                "lightcurve.png"
            ),
            dpi=FIGURE_DPI,
            bbox_inches="tight"
        )

    if SHOW_PLOTS:
        plt.show()
    else:
        plt.close()


def plot_folded(lightcurve, transit):

    folded = lightcurve.fold(
        period=transit["period"],
        epoch_time=transit["transit_time"]
    )

    plt.figure(figsize=(10,5))

    plt.scatter(
        folded.phase.value,
        folded.flux.value,
        s=2,
        color="royalblue"
    )

    plt.xlabel("Phase")
    plt.ylabel("Normalized Flux")
    plt.title("Phase Folded Transit")

    plt.grid(alpha=0.3)

    if SAVE_PLOTS:

        plt.savefig(
            os.path.join(
                FIGURE_DIR,
                "folded_transit.png"
            ),
            dpi=FIGURE_DPI,
            bbox_inches="tight"
        )

    if SHOW_PLOTS:
        plt.show()
    else:
        plt.close()


def plot_bls(transit):

    results = transit["results"]

    plt.figure(figsize=(10,5))

    plt.plot(
        results.period,
        results.power,
        color="darkred"
    )

    plt.axvline(
        transit["period"],
        color="blue",
        linestyle="--",
        label=f"{transit['period']:.3f} d"
    )

    plt.xlabel("Period (Days)")
    plt.ylabel("BLS Power")
    plt.title("Box Least Squares Periodogram")

    plt.legend()

    plt.grid(alpha=0.3)

    if SAVE_PLOTS:

        plt.savefig(
            os.path.join(
                FIGURE_DIR,
                "bls_periodogram.png"
            ),
            dpi=FIGURE_DPI,
            bbox_inches="tight"
        )

    if SHOW_PLOTS:
        plt.show()
    else:
        plt.close()


def generate_plots(lightcurve,
                   transit,
                   prediction,
                   confidence):

    print("\nGenerating plots...")

    plot_lightcurve(lightcurve)

    plot_folded(lightcurve, transit)

    plot_bls(transit)

    print("Plots saved to outputs/figures/")


if __name__ == "__main__":

    print("Visualization Module")