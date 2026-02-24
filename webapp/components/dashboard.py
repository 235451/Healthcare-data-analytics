import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render_gauge(risk_score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score * 100,
        title={"text": "Health Risk (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#e63946"},
            "steps": [
                {"range": [0, 40], "color": "#2ec4b6"},
                {"range": [40, 75], "color": "#ffb703"},
                {"range": [75, 100], "color": "#e63946"}
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

def render_dashboard(patient_data, result):
    st.subheader("📊 Risk Assessment Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Risk Level",
            result["risk_level"],
            delta=f"{round(result['risk_score']*100,2)}%"
        )

    with col2:
        render_gauge(result["risk_score"])

    st.subheader("🧠 Model Explanation (Key Factors)")
    importance_df = pd.DataFrame(
        result["feature_importance"].items(),
        columns=["Feature", "Impact"]
    ).sort_values("Impact", ascending=False)

    st.bar_chart(importance_df.set_index("Feature"))

    st.subheader("🧑‍⚕️ Doctor Recommendation")
    st.success(result["doctor_recommendation"])
