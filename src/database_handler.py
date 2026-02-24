"""
database_handler.py
-------------------
Manages patient records and predictions
"""

import sqlite3
from datetime import datetime

DB_NAME = "patients.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def insert_prediction(patient_data: dict, risk_score: float, risk_level: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO patients (
            age, bmi, systolic_bp, diastolic_bp,
            cholesterol, glucose, risk_score, risk_level, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient_data["age"],
        patient_data["bmi"],
        patient_data["systolic_bp"],
        patient_data["diastolic_bp"],
        patient_data["cholesterol"],
        patient_data["glucose"],
        risk_score,
        risk_level,
        datetime.now()
    ))

    conn.commit()
    conn.close()
