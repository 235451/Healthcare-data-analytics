"""
doctor_chatbot_ui.py
--------------------
Doctor-facing AI Clinical Assistant UI

Features:
- Government hospital theme (India)
- Patient-aware chatbot
- Clinical context injection
- Risk-based suggestions
- Expandable history
- Ready for FastAPI / LLM integration

Author: Mahesh
"""

import streamlit as st
from datetime import datetime

# Import backend chatbot logic
from src.doctor_chatbot import doctor_chatbot

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Doctor Assistant | Govt Hospital",
    page_icon="🩺",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS (GOVT HOSPITAL THEME)
# -------------------------------------------------
st.markdown("""
<style>
.chat-container {
    background-color: #f4f6f8;
    padding: 15px;
    border-radius: 10px;
}
.user-msg {
    background-color: #d1e7dd;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
}
.bot-msg {
    background-color: #ffffff;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
    border-left: 4px solid #0d6efd;
}
.header {
    font-size: 28px;
    font-weight: bold;
    color: #0d6efd;
}
.sub-header {
    color: #555;
}
.risk-high { color: red; font-weight: bold; }
.risk-medium { color: orange; font-weight: bold; }
.risk-low { color: green; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "patient_context" not in st.session_state:
    st.session_state.patient_context = {
        "patient_id": "AP-GH01-20250123-483921",
        "age": 58,
        "gender": "Male",
        "risk_category": "High",
        "conditions": ["Hypertension", "Diabetes"],
        "latest_vitals": {
            "bp": "158/96",
            "spo2": 94,
            "heart_rate": 88
        }
    }

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("<div class='header'>🩺 AI Clinical Assistant</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-header'>Government Hospital • Doctor Decision Support</div>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------
# SIDEBAR – PATIENT CONTEXT
# -------------------------------------------------
with st.sidebar:
    st.subheader("👤 Patient Summary")

    patient = st.session_state.patient_context

    st.write(f"**Patient ID:** {patient['patient_id']}")
    st.write(f"**Age:** {patient['age']}")
    st.write(f"**Gender:** {patient['gender']}")

    risk = patient["risk_category"]
    if risk == "High":
        st.markdown(f"**Risk:** <span class='risk-high'>{risk}</span>", unsafe_allow_html=True)
    elif risk == "Medium":
        st.markdown(f"**Risk:** <span class='risk-medium'>{risk}</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"**Risk:** <span class='risk-low'>{risk}</span>", unsafe_allow_html=True)

    st.subheader("🧪 Latest Vitals")
    for k, v in patient["latest_vitals"].items():
        st.write(f"- **{k.upper()}** : {v}")

    st.subheader("🩻 Known Conditions")
    for c in patient["conditions"]:
        st.write(f"• {c}")

    st.divider()
    st.caption("⚠️ AI suggestions are advisory only")

# -------------------------------------------------
# CHAT DISPLAY AREA
# -------------------------------------------------
st.subheader("💬 Clinical Chat")

chat_container = st.container()

with chat_container:
    for chat in st.session_state.chat_history:
        if chat["role"] == "doctor":
            st.markdown(
                f"<div class='user-msg'><b>Doctor:</b> {chat['message']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='bot-msg'><b>AI:</b> {chat['message']}</div>",
                unsafe_allow_html=True
            )

# -------------------------------------------------
# INPUT AREA
# -------------------------------------------------
st.divider()

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area(
        "Ask a clinical question:",
        placeholder="e.g. Should this patient be admitted? What tests are needed?",
        height=80
    )

    col1, col2 = st.columns([1, 5])
    with col1:
        submit = st.form_submit_button("Send 💬")

# -------------------------------------------------
# CHAT PROCESSING
# -------------------------------------------------
if submit and user_input.strip():
    # Save doctor message
    st.session_state.chat_history.append({
        "role": "doctor",
        "message": user_input,
        "time": datetime.now()
    })

    # Build patient-aware prompt
    patient_context = st.session_state.patient_context
    summary = {
        "risk_category": patient_context["risk_category"],
        "conditions": patient_context["conditions"],
        "vitals": patient_context["latest_vitals"]
    }

    # Get AI response
    ai_response = doctor_chatbot(
        query=user_input,
        patient_summary=summary
    )

    # Save AI message
    st.session_state.chat_history.append({
        "role": "ai",
        "message": ai_response,
        "time": datetime.now()
    })

    st.rerun()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption(
    "🧠 AI-powered clinical assistance | Govt of India Hospital System | Prototype"
)
