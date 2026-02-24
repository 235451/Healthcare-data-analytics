"""
model_training.py
=================
Responsible for training, evaluating,
and persisting ML models.
"""

import os
import logging
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def train_model(
    X,
    y,
    model_path: str = "models/trained_models/test_model.pkl"
):
    """
    Train RandomForest model on healthcare data.

    Parameters
    ----------
    X : pd.DataFrame
        Training features
    y : pd.Series
        Labels
    model_path : str
        File path to save trained model

    Returns
    -------
    model : RandomForestClassifier
        Trained model
    """

    logger.info("Starting model training")

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        min_samples_split=5,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X, y)

    # Evaluate quickly
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    auc = roc_auc_score(y, model.predict_proba(X)[:, 1])

    logger.info(f"Training Accuracy: {acc:.4f}")
    logger.info(f"Training ROC-AUC: {auc:.4f}")

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    logger.info(f"Model saved at {model_path}")

    return model
