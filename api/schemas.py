"""
Pydantic schemas for request & response validation
"""

from pydantic import BaseModel
from typing import Dict

class PatientInput(BaseModel):
    age: int
    gender: str
    bmi: float
    systolic_bp: int
    diastolic_bp: int
    cholesterol: int
    glucose: int
    smoking: int
    alcohol: int
    physical_activity: int


class PredictionResponse(BaseModel):
    risk_score: float
    risk_level: str
    feature_importance: Dict[str, float]
    doctor_recommendation: str


class ChatbotInput(BaseModel):
    query: str
    patient: dict
