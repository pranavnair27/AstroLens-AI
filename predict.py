"""
===========================================================
AstroLens AI
Prediction Script
===========================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PARENT_DIR = PROJECT_ROOT.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))

from src.downloader import download_lightcurve
from src.preprocessing import preprocess_lightcurve
from src.transit_detection import detect_transit
from src.feature_extraction import extract_features
from src.classifier import load_classifier, classify_candidate
from src.confidence import calculate_confidence
from src.visualization import generate_plots
from src.report import save_report
from src.utils import banner


def main():

    banner()

    model, scaler = load_classifier()

    tic = input("Enter TIC ID: ")

    print("\nDownloading TESS light curve...")
    lc = download_lightcurve(tic)

    print("Preprocessing...")
    lc = preprocess_lightcurve(lc)

    print("Running BLS...")
    transit = detect_transit(lc)

    if transit is None:
        print("No transit candidate detected.")
        return

    print("Extracting features...")
    features = extract_features(lc, transit)

    print("Running classifier...")
    prediction, probability = classify_candidate(
        model,
        scaler,
        features
    )

    confidence = calculate_confidence(
        probability,
        transit,
        features
    )

    print("\n==============================")
    print("Prediction")
    print("==============================")

    print("Class :", prediction)
    print(f"Confidence : {confidence:.2f}%")

    generate_plots(
        lc,
        transit,
        prediction,
        confidence
    )

    save_report(
        tic,
        prediction,
        confidence,
        transit,
        features
    )


if __name__ == "__main__":
    main()