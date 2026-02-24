"""
data_ingestion.py
=================
Responsible for loading raw healthcare data from multiple sources.

Supported sources:
- CSV files
- Future ready: DB, API, S3

Author: Mahesh (Gov Healthcare AI Project)
"""

import os
import logging
import pandas as pd
from typing import Optional

# ------------------------------------
# Logger configuration
# ------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def load_raw_data(
    file_path: str,
    encoding: Optional[str] = "utf-8"
) -> pd.DataFrame:
    """
    Load raw patient healthcare data from a CSV file.

    Parameters
    ----------
    file_path : str
        Absolute or relative path to CSV file
    encoding : str, optional
        File encoding (default utf-8)

    Returns
    -------
    pd.DataFrame
        Loaded raw dataset

    Raises
    ------
    FileNotFoundError
        If file path does not exist
    ValueError
        If dataset is empty or corrupted
    """

    logger.info("Starting raw data ingestion process")

    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        logger.exception("Failed to read CSV file")
        raise ValueError(f"CSV read error: {str(e)}")

    if df.shape[0] == 0:
        logger.error("Dataset loaded but contains zero rows")
        raise ValueError("Empty dataset is not allowed")

    logger.info(
        f"Successfully loaded dataset with {df.shape[0]} rows "
        f"and {df.shape[1]} columns"
    )

    return df
