"""
===========================================================
AstroLens AI
Preprocessing Module
===========================================================
Light Curve Cleaning and Detrending
===========================================================
"""

import numpy as np
from scipy.signal import savgol_filter

from config import (
    REMOVE_OUTLIERS,
    SIGMA_CLIP,
    NORMALIZE,
    DETREND,
    WINDOW_LENGTH,
    POLYORDER,
)


def remove_nan(lightcurve):
    """
    Remove NaN values.
    """
    return lightcurve.remove_nans()


def sigma_clip(lightcurve, sigma=SIGMA_CLIP):
    """
    Remove outliers using sigma clipping.
    """
    return lightcurve.remove_outliers(sigma=sigma)


def normalize(lightcurve):
    """
    Normalize flux around 1.
    """
    return lightcurve.normalize()


def detrend(lightcurve):
    """
    Remove long-term stellar trends using
    Savitzky-Golay filtering.
    """

    flux = lightcurve.flux.value

    window = WINDOW_LENGTH

    # Window must be odd
    if window % 2 == 0:
        window += 1

    # Window cannot exceed data length
    if window >= len(flux):
        window = len(flux) - 1

    if window % 2 == 0:
        window -= 1

    trend = savgol_filter(
        flux,
        window_length=window,
        polyorder=POLYORDER
    )

    detrended_flux = flux / trend

    new_lc = lightcurve.copy()
    new_lc.flux = detrended_flux

    return new_lc


def estimate_noise(lightcurve):
    """
    Estimate RMS noise level.
    """

    flux = lightcurve.flux.value

    return np.std(flux)


def compute_snr(lightcurve):
    """
    Simple SNR estimate.
    """

    flux = lightcurve.flux.value

    signal = np.abs(np.median(flux) - np.min(flux))

    noise = np.std(flux)

    if noise == 0:
        return 0

    return signal / noise


def preprocess_lightcurve(lightcurve):
    """
    Complete preprocessing pipeline.
    """

    print("\nRemoving NaNs...")
    lc = remove_nan(lightcurve)

    if REMOVE_OUTLIERS:
        print("Removing outliers...")
        lc = sigma_clip(lc)

    if NORMALIZE:
        print("Normalizing...")
        lc = normalize(lc)

    if DETREND:
        print("Detrending...")
        lc = detrend(lc)

    noise = estimate_noise(lc)
    snr = compute_snr(lc)

    print(f"Estimated Noise : {noise:.6f}")
    print(f"Estimated SNR   : {snr:.2f}")

    return lc


if __name__ == "__main__":

    from src.downloader import download_lightcurve

    tic = input("Enter TIC ID : ")

    lc = download_lightcurve(tic)

    clean = preprocess_lightcurve(lc)

    print(clean)