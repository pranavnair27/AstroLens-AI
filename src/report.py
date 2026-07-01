"""
===========================================================
AstroLens AI
Report Generation Module
===========================================================
Creates text reports and CSV summaries
===========================================================
"""

import os
import csv
from datetime import datetime

from config import REPORT_DIR, RESULT_CSV


def save_report(
    tic_id,
    prediction,
    confidence,
    transit,
    features
):
    """
    Save a detailed text report.
    """

    os.makedirs(REPORT_DIR, exist_ok=True)

    filename = os.path.join(
        REPORT_DIR,
        f"TIC_{tic_id}_report.txt"
    )

    with open(filename, "w") as f:

        f.write("=" * 60 + "\n")
        f.write("AstroLens AI Report\n")
        f.write("=" * 60 + "\n\n")

        f.write(
            f"Generated : {datetime.now()}\n\n"
        )

        f.write(f"TIC ID : {tic_id}\n\n")

        f.write("Prediction\n")
        f.write("-------------------------\n")

        f.write(f"Classification : {prediction}\n")
        f.write(f"Confidence     : {confidence:.2f}%\n\n")

        f.write("Transit Parameters\n")
        f.write("-------------------------\n")

        f.write(f"Period      : {transit['period']:.5f} days\n")
        f.write(f"Duration    : {features['duration']:.2f} hr\n")
        f.write(f"Depth       : {features['depth']:.6f}\n")
        f.write(f"BLS Power   : {transit['power']:.3f}\n\n")

        f.write("Extracted Features\n")
        f.write("-------------------------\n")

        for key, value in features.items():

            f.write(f"{key:15s}: {value:.6f}\n")

        f.write("\n")

        f.write("Pipeline\n")
        f.write("-------------------------\n")

        f.write("✓ Downloaded TESS data\n")
        f.write("✓ Preprocessed light curve\n")
        f.write("✓ Box Least Squares detection\n")
        f.write("✓ Feature extraction\n")
        f.write("✓ Machine Learning classification\n")
        f.write("✓ Confidence estimation\n")

    print(f"\nReport saved:\n{filename}")

    append_csv(
        tic_id,
        prediction,
        confidence,
        transit,
        features
    )


def append_csv(
    tic_id,
    prediction,
    confidence,
    transit,
    features
):
    """
    Append result to CSV.
    """

    file_exists = os.path.exists(RESULT_CSV)

    with open(
        RESULT_CSV,
        "a",
        newline=""
    ) as csvfile:

        writer = csv.writer(csvfile)

        if not file_exists:

            writer.writerow([

                "TIC",

                "Prediction",

                "Confidence",

                "Period",

                "Duration",

                "Depth",

                "SNR",

                "BLS Power"

            ])

        writer.writerow([

            tic_id,

            prediction,

            round(confidence, 2),

            round(transit["period"], 5),

            round(features["duration"], 3),

            round(features["depth"], 6),

            round(features["snr"], 3),

            round(transit["power"], 3)

        ])


def print_summary(
    prediction,
    confidence
):

    print("\n")
    print("=" * 50)

    print("FINAL RESULT")

    print("=" * 50)

    print(f"Prediction : {prediction}")

    print(f"Confidence : {confidence:.2f}%")

    print("=" * 50)


if __name__ == "__main__":

    print("Report Module")