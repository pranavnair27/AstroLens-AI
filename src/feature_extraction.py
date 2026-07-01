"""
===========================================================
AstroLens AI
Feature Extraction Module
===========================================================
Extracts astrophysical features from detected transit
===========================================================
"""

import numpy as np


def compute_snr(lightcurve, depth):
    """
    Estimate signal-to-noise ratio.
    """

    flux = lightcurve.flux.value

    noise = np.std(flux)

    if noise == 0:
        return 0.0

    return abs(depth) / noise


def estimate_local_noise(lightcurve):
    """
    RMS noise estimate.
    """

    flux = lightcurve.flux.value

    return np.std(flux)


def estimate_transit_shape(lightcurve, transit):
    """
    Simple transit shape metric.

    Returns value between 0 and 1.

    Higher = sharper transit.
    """

    flux = lightcurve.flux.value

    depth = abs(transit["depth"])

    minimum = np.min(flux)

    median = np.median(flux)

    shape = abs(median - minimum)

    if depth == 0:
        return 0

    return min(shape / depth, 1.0)


def estimate_symmetry(lightcurve):
    """
    Approximate symmetry score.

    Placeholder implementation.
    """

    flux = lightcurve.flux.value

    left = flux[:len(flux)//2]

    right = flux[len(flux)//2:]

    m = min(len(left), len(right))

    difference = np.mean(np.abs(left[:m] - right[:m]))

    score = 1 / (1 + difference)

    return score


def estimate_data_quality(lightcurve):
    """
    Estimate overall data quality.

    Higher is better.
    """

    flux = lightcurve.flux.value

    missing = np.sum(~np.isfinite(flux))

    quality = 1 - (missing / len(flux))

    return max(0.0, quality)


def extract_features(lightcurve, transit):
    """
    Extract all ML features.
    """

    print("\nExtracting astrophysical features...")

    depth = abs(transit["depth"])

    duration_hours = transit["duration"] * 24

    period = transit["period"]

    snr = compute_snr(
        lightcurve,
        depth
    )

    noise = estimate_local_noise(
        lightcurve
    )

    shape = estimate_transit_shape(
        lightcurve,
        transit
    )

    symmetry = estimate_symmetry(
        lightcurve
    )

    quality = estimate_data_quality(
        lightcurve
    )

    features = {

    "period": period,

    "duration": duration_hours,

    "depth": depth,

    "snr": snr

}

    print("\nFeature Summary")

    print("-" * 40)

    for key, value in features.items():

        print(f"{key:15s}: {value:.5f}")

    print("-" * 40)

    return features


def feature_vector(features):
    """
    Convert feature dictionary to ML vector.

    Feature order MUST match classifier.py
    """

    return np.array([

        features["period"],

        features["duration"],

        features["depth"],

        features["snr"]

    ]).reshape(1, -1)

if __name__ == "__main__":

    print("Feature Extraction Module")