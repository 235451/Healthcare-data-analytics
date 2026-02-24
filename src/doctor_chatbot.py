def doctor_chatbot(query, patient_summary=None):
    response = "Based on clinical guidelines: "

    if "bp" in query.lower():
        response += "Uncontrolled BP increases cardiovascular risk."

    elif "diabetes" in query.lower():
        response += "HbA1c above 7 indicates poor glycemic control."

    elif "admission" in query.lower():
        response += "High-risk patients should be hospitalized."

    else:
        response += "Consider reviewing vitals and lab trends."

    if patient_summary:
        response += f" Patient risk category: {patient_summary.get('risk_category')}."

    return response
