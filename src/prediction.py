"""
prediction.py
=============
Handles inference and clinical risk interpretation.
"""

import os
import joblib
import numpy as np
import pandas as pd
from typing import Dict

MODEL_PATH = "models/trained_models/test_model.pkl"


def predict_risk(patient_features: pd.Series) -> Dict[str, object]:
    """
    Predict cardiovascular disease risk for a patient.

    Parameters
    ----------
    patient_features : pd.Series
        Feature vector

    Returns
    -------
    dict
        Risk score, category, and clinical message
    """

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Trained model not found")

    model = joblib.load(MODEL_PATH)

    X = np.asarray(patient_features.values).reshape(1, -1)
    probability = float(model.predict_proba(X)[0][1])

    if probability < 0.25:
        category = "LOW"
        advice = "Routine check-up recommended."
    elif probability < 0.5:
        category = "MODERATE"
        advice = "Lifestyle modification advised."
    elif probability < 0.75:
        category = "HIGH"
        advice = "Doctor consultation required."
    else:
        category = "CRITICAL"
        advice = "Immediate medical intervention needed."

    return {
        "risk_score": round(probability, 4),
        "risk_category": category,
        "clinical_advice": advice
    }
