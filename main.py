"""
===========================================================
 AstroLens AI
 Hybrid AI Pipeline for Exoplanet Detection
===========================================================
Author : Team AstroLens
===========================================================
"""

import os
import time

from config import *

from src.downloader import download_lightcurve
from src.preprocessing import preprocess_lightcurve
from src.transit_detection import detect_transit
from src.feature_extraction import extract_features
from src.classifier import load_classifier
from src.classifier import classify_candidate
from src.confidence import calculate_confidence
from src.visualization import generate_plots
from src.report import save_report


def print_banner():

    print("=" * 60)
    print("        AstroLens AI")
    print(" Hybrid AI Exoplanet Detection Pipeline")
    print("=" * 60)
    print()


def main():

    print_banner()

    tic_id = input("Enter TESS TIC ID : ").strip()

    start = time.time()

    print("\nDownloading TESS Light Curve...")
    lc = download_lightcurve(tic_id)

    print("Preprocessing...")
    clean_lc = preprocess_lightcurve(lc)

    print("Searching for Transit Candidates...")

    transit = detect_transit(clean_lc)

    if transit is None:

        print("\nNo significant periodic signal found.")
        return

    print("Extracting Features...")

    features = extract_features(clean_lc, transit)

    print("Loading AI Model...")

    model, scaler = load_classifier()

    print("Running Classification...")

    prediction, probability = classify_candidate(
        model,
        scaler,
        features
    )

    print("Computing Confidence...")

    confidence = calculate_confidence(
        probability,
        transit,
        features
    )

    print("Generating Figures...")

    generate_plots(
        clean_lc,
        transit,
        prediction,
        confidence
    )

    print("Saving Report...")

    save_report(
        tic_id,
        prediction,
        confidence,
        transit,
        features
    )

    print("\n")
    print("=" * 60)

    print("RESULT")

    print("=" * 60)

    print(f"TIC ID              : {tic_id}")
    print(f"Classification      : {prediction}")

    print(f"Confidence          : {confidence:.2f}%")

    print(f"Orbital Period      : {transit['period']:.5f} days")

    print(f"Transit Depth       : {features['depth']:.6f}")

    print(f"Transit Duration    : {features['duration']:.3f} hr")

    print(f"SNR                 : {features['snr']:.2f}")

    print("=" * 60)

    print(
        f"\nFinished in {time.time()-start:.2f} seconds"
    )


if __name__ == "__main__":

    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/figures", exist_ok=True)
    os.makedirs("outputs/reports", exist_ok=True)

    main()
