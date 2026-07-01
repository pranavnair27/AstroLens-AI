"""
===========================================================
AstroLens AI
Utility Functions
===========================================================
Shared helper functions
===========================================================
"""

import os
import random
import numpy as np

from config import RANDOM_STATE


# ==========================================================
# Random Seed
# ==========================================================

def set_seed(seed=RANDOM_STATE):
    """
    Make experiments reproducible.
    """

    random.seed(seed)
    np.random.seed(seed)


# ==========================================================
# Create Directory
# ==========================================================

def ensure_dir(path):
    """
    Create directory if it does not exist.
    """

    os.makedirs(path, exist_ok=True)


# ==========================================================
# Normalize Value
# ==========================================================

def normalize(value, minimum, maximum):

    if maximum == minimum:
        return 0.0

    return (value - minimum) / (maximum - minimum)


# ==========================================================
# Clamp Value
# ==========================================================

def clamp(value, low, high):

    return max(low, min(high, value))


# ==========================================================
# Print Header
# ==========================================================

def print_header(title):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ==========================================================
# Print Dictionary
# ==========================================================

def print_dictionary(dictionary):

    for key, value in dictionary.items():

        if isinstance(value, float):
            print(f"{key:20s}: {value:.5f}")
        else:
            print(f"{key:20s}: {value}")


# ==========================================================
# Save Dictionary
# ==========================================================

def save_dictionary(dictionary, filename):

    with open(filename, "w") as f:

        for key, value in dictionary.items():

            f.write(f"{key}: {value}\n")


# ==========================================================
# Check Model Files
# ==========================================================

def model_exists(model_path, scaler_path):

    return (
        os.path.exists(model_path)
        and
        os.path.exists(scaler_path)
    )


# ==========================================================
# Timer
# ==========================================================

class Timer:

    def __init__(self):
        import time
        self.time = time
        self.start = self.time.time()

    def stop(self):

        return self.time.time() - self.start


# ==========================================================
# Banner
# ==========================================================

def banner():

    print("""
===========================================================
             AstroLens AI
 Hybrid AI Exoplanet Detection Pipeline
===========================================================
""")