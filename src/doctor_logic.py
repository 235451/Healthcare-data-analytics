"""
doctor_logic.py
---------------
Medical rule-based decision support system
"""

def doctor_decision_support(risk_score: float, patient: dict) -> str:
    recommendations = []

    if risk_score > 0.75:
        recommendations.append(
            "🚨 High risk detected. Immediate cardiology consultation advised."
        )

    if patient["bmi"] > 30:
        recommendations.append(
            "⚠️ Obesity detected. Weight reduction and diet counseling recommended."
        )

    if patient["systolic_bp"] > 140:
        recommendations.append(
            "⚠️ Hypertension detected. Blood pressure control required."
        )

    if patient["cholesterol"] > 240:
        recommendations.append(
            "⚠️ High cholesterol. Statin therapy evaluation suggested."
        )

    if patient["physical_activity"] < 3:
        recommendations.append(
            "ℹ️ Low physical activity. Encourage regular exercise."
        )

    if not recommendations:
        recommendations.append(
            "✅ Patient condition appears stable. Continue regular monitoring."
        )

    return " ".join(recommendations)
