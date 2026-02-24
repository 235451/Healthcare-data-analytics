

import os
import logging
import joblib
import shap
import numpy as np
import pandas as pd
from typing import Dict, Any

# -------------------------------------------------
# Logger configuration
# -------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# -------------------------------------------------
# Constants
# -------------------------------------------------
MODEL_PATH = "models/trained_models/test_model.pkl"


def _load_model():
    """
    Internal utility to load trained ML model safely.
    """
    if not os.path.exists(MODEL_PATH):
        logger.error("Trained model not found")
        raise FileNotFoundError("Model file missing")

    return joblib.load(MODEL_PATH)


def generate_shap_values(
    X: pd.DataFrame,
    patient_index: int = 0
) -> Dict[str, Any]:
    """
    Generate SHAP values for explainability.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix used for training or inference
    patient_index : int
        Index of patient row to explain

    Returns
    -------
    dict
        SHAP values, base value, and feature contributions
    """

    logger.info("Starting SHAP explainability pipeline")

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame")

    if patient_index < 0 or patient_index >= len(X):
        raise IndexError("Invalid patient index")

    model = _load_model()

    try:
        explainer = shap.TreeExplainer(model)
    except Exception as e:
        logger.exception("Failed to initialize SHAP explainer")
        raise RuntimeError(f"SHAP explainer error: {str(e)}")

    # SHAP expects numpy array
    shap_values = explainer.shap_values(X)

    # Binary classification safety
    if isinstance(shap_values, list):
        shap_values = shap_values[1]

    patient_shap = shap_values[patient_index]
    base_value = explainer.expected_value
    
    # Handle case where expected_value is a list (binary classification)
    if isinstance(base_value, list):
        base_value = base_value[1]

    explanation = {
        "base_value": float(base_value), # type: ignore
        "patient_index": patient_index,
        "feature_contributions": {
            feature: float(value)
            for feature, value in zip(X.columns, patient_shap)
        }
    }

    logger.info("SHAP explainability generated successfully")

    return explanation
