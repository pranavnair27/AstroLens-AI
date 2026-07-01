"""
===========================================================
AstroLens AI
Model Training Script
===========================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PARENT_DIR = PROJECT_ROOT.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))

from src.classifier import train_classifier
from src.utils import banner


def main():

    banner()

    print("Training AstroLens AI...\n")

    model, scaler = train_classifier()

    print("\nTraining Complete!")

    print("\nSaved Files:")
    print("models/classifier.pkl")
    print("models/scaler.pkl")


if __name__ == "__main__":
    main()