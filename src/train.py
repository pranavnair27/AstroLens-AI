"""
===========================================================
AstroLens AI
Model Training Script
===========================================================
"""

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