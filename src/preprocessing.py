"""
preprocessing.py
================
Handles cleaning, normalization and transformation
of raw healthcare patient data.
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess raw healthcare data.

    Steps:
    - Missing value handling
    - Categorical encoding
    - Outlier handling
    - Type enforcement

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataset

    Returns
    -------
    pd.DataFrame
        Cleaned dataset
    """

    logger.info("Starting preprocessing pipeline")

    data = df.copy(deep=True)

    # -----------------------------
    # Numeric columns
    # -----------------------------
    numeric_columns = [
        "age",
        "systolic_bp",
        "diastolic_bp",
        "cholesterol",
        "glucose",
        "bmi"
    ]

    for col in numeric_columns:
        if col in data.columns:
            median_val = data[col].median()
            data[col] = data[col].fillna(median_val)
            data[col] = data[col].clip(lower=0)

    # -----------------------------
    # Gender Encoding
    # -----------------------------
    if "gender" in data.columns:
        data["gender"] = data["gender"].str.lower().map({
            "male": 1,
            "female": 0
        }).fillna(0)

    # -----------------------------
    # Boolean features
    # -----------------------------
    boolean_features = ["smoking", "diabetes", "heart_disease"]

    for col in boolean_features:
        if col in data.columns:
            data[col] = data[col].apply(lambda x: 1 if x else 0)

    # -----------------------------
    # Remove infinite values
    # -----------------------------
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.fillna(0, inplace=True)

    logger.info("Preprocessing completed successfully")

    return data
