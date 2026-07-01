"""
===========================================================
 AstroLens AI
 Configuration File
===========================================================
"""

import os

# ==========================================================
# Project Directories
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
TESS_DIR = os.path.join(DATA_DIR, "tess")
MODEL_DIR = os.path.join(BASE_DIR, "models")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
FIGURE_DIR = os.path.join(OUTPUT_DIR, "figures")
REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")

# Create folders automatically
for folder in [
    DATA_DIR,
    TESS_DIR,
    MODEL_DIR,
    OUTPUT_DIR,
    FIGURE_DIR,
    REPORT_DIR
]:
    os.makedirs(folder, exist_ok=True)

# ==========================================================
# Model Files
# ==========================================================

MODEL_PATH = os.path.join(MODEL_DIR, "classifier.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

# ==========================================================
# Training Dataset
# ==========================================================

KEPLER_DATASET = os.path.join(DATA_DIR, "kepler.csv")

# ==========================================================
# Light Curve Preprocessing
# ==========================================================

REMOVE_OUTLIERS = True

SIGMA_CLIP = 5

NORMALIZE = True

DETREND = True

WINDOW_LENGTH = 401

POLYORDER = 2

# ==========================================================
# Box Least Squares Parameters
# ==========================================================

MIN_PERIOD = 0.5        # days

MAX_PERIOD = 30.0       # days

PERIOD_STEPS = 5000

MIN_DURATION = 0.05     # days

MAX_DURATION = 0.50     # days

# ==========================================================
# Signal Detection Thresholds
# ==========================================================

MIN_SNR = 7.0

MIN_TRANSIT_DEPTH = 0.0005

MIN_BLS_POWER = 8.0

# ==========================================================
# Machine Learning
# ==========================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20

N_ESTIMATORS = 300

MAX_DEPTH = 15

MIN_SAMPLES_SPLIT = 5

# ==========================================================
# Confidence Score Weights
# ==========================================================

WEIGHT_MODEL = 0.40

WEIGHT_BLS = 0.25

WEIGHT_SNR = 0.20

WEIGHT_QUALITY = 0.10

WEIGHT_CONSISTENCY = 0.05

# ==========================================================
# Visualization
# ==========================================================

FIGURE_DPI = 300

SAVE_PLOTS = True

SHOW_PLOTS = True

# ==========================================================
# Output Files
# ==========================================================

RESULT_CSV = os.path.join(
    OUTPUT_DIR,
    "results.csv"
)

REPORT_FILE = os.path.join(
    REPORT_DIR,
    "report.txt"
)

# ==========================================================
# Logging
# ==========================================================

VERBOSE = True

# ==========================================================
# Version
# ==========================================================

PROJECT_NAME = "AstroLens AI"

VERSION = "1.0.0"

AUTHOR = "Team Pratyagra"

DESCRIPTION = (
    "Hybrid Physics + AI Pipeline for "
    "Explainable Exoplanet Detection"
)
