import os
import numpy as np
import pandas as pd
import joblib
import pytest

from src.data_ingestion import load_raw_data
from src.preprocessing import preprocess_data
from src.feature_engineering import engineer_features
from src.model_training import train_model
from src.prediction import predict_risk


# =====================================================
# GLOBAL TEST CONFIG
# =====================================================
TEST_DATA_PATH = "data/raw/synthetic_patients.csv"
MODEL_SAVE_PATH = "models/trained_models/test_model.pkl"


# =====================================================
# FIXTURES
# =====================================================
@pytest.fixture(scope="session")
def raw_data():
    """Load raw data for testing"""
    df = load_raw_data(TEST_DATA_PATH)
    return df


@pytest.fixture(scope="session")
def processed_data(raw_data):
    """Preprocess raw data"""
    df = preprocess_data(raw_data)
    return df


@pytest.fixture(scope="session")
def feature_data(processed_data):
    """Apply feature engineering"""
    X, y = engineer_features(processed_data)
    return X, y


@pytest.fixture(scope="session")
def trained_model(feature_data):
    """Train model once for all tests"""
    X, y = feature_data
    model = train_model(X, y)
    joblib.dump(model, MODEL_SAVE_PATH)
    return model


# =====================================================
# DATA TESTS
# =====================================================
def test_raw_data_loaded(raw_data):
    assert raw_data is not None
    assert isinstance(raw_data, pd.DataFrame)
    assert len(raw_data) > 0


def test_required_columns_present(raw_data):
    required_columns = [
        "age", "gender", "systolic_bp", "diastolic_bp",
        "cholesterol", "glucose", "bmi", "smoking",
        "diabetes", "heart_disease"
    ]
    for col in required_columns:
        assert col in raw_data.columns


# =====================================================
# PREPROCESSING TESTS
# =====================================================
def test_no_missing_values_after_preprocessing(processed_data):
    assert processed_data.isnull().sum().sum() == 0


def test_data_types_valid(processed_data):
    assert processed_data["age"].dtype in [np.int64, np.float64]
    assert processed_data["bmi"].dtype in [np.float64, np.int64]


# =====================================================
# FEATURE ENGINEERING TESTS
# =====================================================
def test_feature_engineering_output(feature_data):
    X, y = feature_data
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] > 5  # Must have multiple features


def test_target_variable_binary(feature_data):
    _, y = feature_data
    assert set(y.unique()).issubset({0, 1})


# =====================================================
# MODEL TRAINING TESTS
# =====================================================
def test_model_training_success(trained_model):
    assert trained_model is not None
    assert hasattr(trained_model, "predict")


def test_model_saved_to_disk():
    assert os.path.exists(MODEL_SAVE_PATH)


def test_model_load_from_disk():
    model = joblib.load(MODEL_SAVE_PATH)
    assert model is not None
    assert hasattr(model, "predict")


# =====================================================
# PREDICTION TESTS
# =====================================================
def test_prediction_output_shape(trained_model, feature_data):
    X, _ = feature_data
    preds = trained_model.predict(X[:10])
    assert len(preds) == 10


def test_prediction_values_binary(trained_model, feature_data):
    X, _ = feature_data
    preds = trained_model.predict(X[:50])
    assert set(np.unique(preds)).issubset({0, 1})


def test_predict_risk_function(feature_data):
    X, _ = feature_data
    sample = X.iloc[0]

    result = predict_risk(sample)

    assert isinstance(result, dict)
    assert "risk_score" in result
    assert "risk_category" in result


def test_risk_score_range(feature_data):
    X, _ = feature_data
    sample = X.iloc[1]

    result = predict_risk(sample)
    risk_score = result["risk_score"]
    # Ensure risk_score is convertible to float
    assert 0.0 <= float(str(risk_score)) <= 1.0


def test_risk_category_values(feature_data):
    X, _ = feature_data
    sample = X.iloc[2]

    result = predict_risk(sample)
    assert result["risk_category"] in [
        "Low", "Medium", "High", "Critical"
    ]


# =====================================================
# EDGE CASE TESTS
# =====================================================
def test_extreme_patient_values(trained_model):
    extreme_patient = pd.DataFrame([{
        "age": 95,
        "systolic_bp": 210,
        "diastolic_bp": 130,
        "cholesterol": 350,
        "glucose": 320,
        "bmi": 45,
        "smoking": 1,
        "diabetes": 1
    }])

    preds = trained_model.predict(extreme_patient)
    assert preds[0] in [0, 1]


def test_young_healthy_patient(trained_model):
    healthy_patient = pd.DataFrame([{
        "age": 22,
        "systolic_bp": 110,
        "diastolic_bp": 70,
        "cholesterol": 150,
        "glucose": 85,
        "bmi": 21,
        "smoking": 0,
        "diabetes": 0
    }])

    preds = trained_model.predict(healthy_patient)
    assert preds[0] == 0 or preds[0] == 1


# =====================================================
# PERFORMANCE SMOKE TEST
# =====================================================
def test_bulk_prediction_speed(trained_model, feature_data):
    X, _ = feature_data
    preds = trained_model.predict(X[:1000])
    assert len(preds) == 1000


# =====================================================
# CLEANUP
# =====================================================
def teardown_module(module):
    if os.path.exists(MODEL_SAVE_PATH):
        os.remove(MODEL_SAVE_PATH)
