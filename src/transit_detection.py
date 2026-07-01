"""
===========================================================
AstroLens AI
Transit Detection Module
===========================================================
Uses Box Least Squares (BLS) to detect exoplanet transits
===========================================================
"""

import numpy as np

from astropy.timeseries import BoxLeastSquares

from config import (
    MIN_PERIOD,
    MAX_PERIOD,
    MIN_DURATION,
    MAX_DURATION,
    PERIOD_STEPS,
    MIN_BLS_POWER,
)


def detect_transit(lightcurve):
    """
    Detect the strongest periodic transit using
    Box Least Squares.

    Parameters
    ----------
    lightcurve : LightCurve

    Returns
    -------
    dict
        Transit parameters
    """

    print("\nRunning Box Least Squares...")

    time = lightcurve.time.value
    flux = lightcurve.flux.value

    mask = np.isfinite(time) & np.isfinite(flux)

    time = time[mask]
    flux = flux[mask]

    model = BoxLeastSquares(time, flux)

    periods = np.linspace(
        MIN_PERIOD,
        MAX_PERIOD,
        PERIOD_STEPS
    )

    durations = np.linspace(
        MIN_DURATION,
        MAX_DURATION,
        10
    )

    results = model.power(
        periods,
        durations
    )

    best = np.argmax(results.power)

    best_period = results.period[best]
    best_duration = results.duration[best]
    best_power = results.power[best]
    best_t0 = results.transit_time[best]
    best_depth = results.depth[best]

    print(f"Best Period     : {best_period:.5f} days")
    print(f"Transit Depth   : {best_depth:.6f}")
    print(f"Duration        : {best_duration*24:.2f} hr")
    print(f"BLS Power       : {best_power:.2f}")

    if best_power < MIN_BLS_POWER:

        print("\nNo significant transit detected.")

        return None

    return {

        "period": float(best_period),

        "duration": float(best_duration),

        "depth": float(best_depth),

        "power": float(best_power),

        "transit_time": float(best_t0),

        "results": results
    }


def fold_lightcurve(lightcurve, period, epoch):
    """
    Fold the light curve.

    Returns
    -------
    FoldedLightCurve
    """

    return lightcurve.fold(
        period=period,
        epoch_time=epoch
    )


def print_transit_summary(transit):
    """
    Print transit information.
    """

    print("\n")
    print("=" * 50)
    print("Transit Candidate")
    print("=" * 50)

    print(f"Period      : {transit['period']:.5f} days")

    print(f"Depth       : {transit['depth']:.6f}")

    print(
        f"Duration    : {transit['duration']*24:.2f} hr"
    )

    print(f"BLS Power   : {transit['power']:.2f}")

    print("=" * 50)


if __name__ == "__main__":

    from src.downloader import download_lightcurve
    from src.preprocessing import preprocess_lightcurve

    tic = input("Enter TIC ID : ")

    lc = download_lightcurve(tic)

    clean = preprocess_lightcurve(lc)

    transit = detect_transit(clean)

    if transit:

        print_transit_summary(transit)