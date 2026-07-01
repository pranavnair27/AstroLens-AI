"""
===========================================================
AstroLens AI
Downloader Module
===========================================================
Downloads TESS Light Curves from MAST
===========================================================
"""

import os

import lightkurve as lk

from config import TESS_DIR


def download_lightcurve(
    tic_id,
    mission="TESS",
    author="SPOC",
    cadence="short"
):
    """
    Download a TESS light curve.

    Parameters
    ----------
    tic_id : str
        TESS TIC ID

    mission : str
        Default = TESS

    author : str
        Default = SPOC

    cadence : str
        short or long

    Returns
    -------
    LightCurve object
    """

    target = f"TIC {tic_id}"

    print(f"\nSearching for {target}...")

    search = lk.search_lightcurve(
        target,
        mission=mission,
        author=author
    )

    if len(search) == 0:
        raise Exception(
            f"No light curve found for {target}"
        )

    print(f"Found {len(search)} observation(s).")

    lc_collection = search.download_all(download_dir=TESS_DIR)

    if lc_collection is None:
        raise Exception("Download failed.")

    print("Combining sectors...")

    lc = lc_collection.stitch()

    return lc


def load_local_lightcurve(filepath):
    """
    Load a previously downloaded FITS file.
    """

    return lk.read(filepath)


def save_lightcurve(lightcurve, filename):
    """
    Save a light curve as FITS.
    """

    path = os.path.join(
        TESS_DIR,
        filename
    )

    lightcurve.to_fits(
        path,
        overwrite=True
    )

    print(f"Saved to {path}")


def list_downloaded():
    """
    List downloaded files.
    """

    print("\nDownloaded Light Curves:\n")

    if not os.path.exists(TESS_DIR):

        print("No folder found.")
        return

    files = os.listdir(TESS_DIR)

    if len(files) == 0:

        print("No downloaded light curves.")
        return

    for f in files:

        print(f)


if __name__ == "__main__":

    tic = input("Enter TIC ID : ")

    lc = download_lightcurve(tic)

    print(lc)

    print("\nDownload successful.")
