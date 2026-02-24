import streamlit as st

def patient_input_sidebar():
    st.sidebar.header("🧑‍⚕️ Patient Information")

    age = st.sidebar.number_input("Age", 1, 120, 45)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    bmi = st.sidebar.number_input("BMI", 10.0, 60.0, 27.5)
    systolic_bp = st.sidebar.number_input("Systolic BP", 80, 200, 130)
    diastolic_bp = st.sidebar.number_input("Diastolic BP", 50, 130, 85)
    cholesterol = st.sidebar.number_input("Cholesterol (mg/dL)", 100, 400, 220)
    glucose = st.sidebar.number_input("Glucose (mg/dL)", 60, 300, 110)

    smoking = st.sidebar.selectbox("Smoking", ["No", "Yes"])
    alcohol = st.sidebar.selectbox("Alcohol Consumption", ["No", "Yes"])
    physical_activity = st.sidebar.slider("Physical Activity Level", 0, 10, 4)

    return {
        "age": age,
        "gender": gender,
        "bmi": bmi,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "cholesterol": cholesterol,
        "glucose": glucose,
        "smoking": 1 if smoking == "Yes" else 0,
        "alcohol": 1 if alcohol == "Yes" else 0,
        "physical_activity": physical_activity
    }
