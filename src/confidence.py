"""
===========================================================
AstroLens AI
Confidence Engine
===========================================================
Adaptive Multi-Stage Confidence Engine (AMCE)
===========================================================
"""

from config import (
    WEIGHT_MODEL,
    WEIGHT_BLS,
    WEIGHT_SNR,
    WEIGHT_QUALITY,
    WEIGHT_CONSISTENCY,
    MIN_BLS_POWER,
    MIN_SNR
)


def normalize(value, minimum, maximum):
    """
    Normalize value to range [0,1]
    """

    if value <= minimum:
        return 0.0

    if value >= maximum:
        return 1.0

    return (value - minimum) / (maximum - minimum)


def calculate_confidence(probability, transit, features):
    """
    Compute final confidence score.
    """

    model_score = probability

    bls_score = normalize(
        transit["power"],
        MIN_BLS_POWER,
        30.0
    )

    snr_score = normalize(
        features["snr"],
        MIN_SNR,
        30.0
    )

    quality_score = 1.0

    consistency = 1.0

    if features["depth"] <= 0:
        consistency = 0.0

    confidence = (

        WEIGHT_MODEL * model_score +

        WEIGHT_BLS * bls_score +

        WEIGHT_SNR * snr_score +

        WEIGHT_QUALITY * quality_score +

        WEIGHT_CONSISTENCY * consistency

    )

    confidence *= 100

    confidence = max(0, min(100, confidence))

    return confidence


def explain_confidence(confidence):
    """
    Human-readable confidence level.
    """

    if confidence >= 90:
        return "Very High"

    elif confidence >= 75:
        return "High"

    elif confidence >= 60:
        return "Moderate"

    elif confidence >= 40:
        return "Low"

    return "Very Low"


def print_confidence_report(confidence):

    print("\n")
    print("=" * 50)
    print("Confidence Report")
    print("=" * 50)

    print(f"Confidence : {confidence:.2f}%")

    print(f"Level      : {explain_confidence(confidence)}")

    print("=" * 50)


if __name__ == "__main__":

    transit = {

        "power": 18

    }

    features = {

        "snr": 15,

        "quality": 0.95,

        "depth": 0.002

    }

    c = calculate_confidence(

        probability=0.92,

        transit=transit,

        features=features

    )

    print_confidence_report(c)