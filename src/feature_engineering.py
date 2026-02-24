"""
feature_engineering.py
======================
Creates machine-learning ready features
from cleaned healthcare data.
"""

import logging
import pandas as pd
from typing import Tuple

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def engineer_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Separate features and target variable.

    Target:
    - heart_disease (0/1)

    Parameters
    ----------
    df : pd.DataFrame
        Preprocessed dataset

    Returns
    -------
    X : pd.DataFrame
        Feature matrix
    y : pd.Series
        Target vector
    """

    logger.info("Starting feature engineering")

    required_columns = [
        "age", "gender", "systolic_bp", "diastolic_bp",
        "cholesterol", "glucose", "bmi",
        "smoking", "diabetes", "heart_disease"
    ]

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    X = df.drop(columns=["heart_disease"])
    y = df["heart_disease"].astype(int)

    logger.info(
        f"Feature engineering completed: "
        f"{X.shape[1]} features selected"
    )

    return X, y
