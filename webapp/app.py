"""
Main Streamlit Application for Healthcare Risk Prediction
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="AI Healthcare Risk Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #374151;
        margin-top: 1.5rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
    }
    .risk-high {
        color: #DC2626;
        font-weight: bold;
    }
    .risk-medium {
        color: #D97706;
        font-weight: bold;
    }
    .risk-low {
        color: #059669;
        font-weight: bold;
    }
    .stButton button {
        width: 100%;
        background-color: #3B82F6;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Load CSS
    load_css()
    
    # Sidebar Navigation
    st.sidebar.image("https://img.icons8.com/color/96/000000/heart-health.png", width=100)
    st.sidebar.title("🏥 HealthAI")
    st.sidebar.markdown("---")
    
    menu = ["📊 Dashboard", "👤 Patient Entry", "🔍 Risk Prediction", "📈 Analytics", "⚙️ Settings"]
    choice = st.sidebar.radio("Navigation", menu)
    
    # Authentication (simplified for demo)
    st.sidebar.markdown("---")
    user_type = st.sidebar.selectbox("User Role", ["Doctor", "Admin", "Nurse"])
    
    # Dashboard Page
    if choice == "📊 Dashboard":
        show_dashboard()
    
    # Patient Entry Page
    elif choice == "👤 Patient Entry":
        show_patient_entry()
    
    # Risk Prediction Page
    elif choice == "🔍 Risk Prediction":
        show_risk_prediction()
    
    # Analytics Page
    elif choice == "📈 Analytics":
        show_analytics()
    
    # Settings Page
    elif choice == "⚙️ Settings":
        show_settings()

def show_dashboard():
    """Display main dashboard"""
    st.markdown('<h1 class="main-header">🏥 AI Healthcare Risk Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Real-time Monitoring & Early Warning System")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Patients", "1,247", "+12 today")
    
    with col2:
        st.metric("High Risk Cases", "89", "-3 this week")
    
    with col3:
        st.metric("Avg Prediction Accuracy", "94.2%", "+2.1%")
    
    with col4:
        st.metric("System Uptime", "99.8%", "✓")
    
    # Risk Distribution Chart
    st.markdown('<div class="sub-header">📊 Risk Distribution</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Sample chart data
        risk_data = pd.DataFrame({
            'Risk Level': ['Low', 'Medium', 'High'],
            'Patients': [850, 308, 89],
            'Color': ['#10B981', '#F59E0B', '#EF4444']
        })
        
        fig = px.bar(risk_data, x='Risk Level', y='Patients', 
                    color='Risk Level', color_discrete_map={
                        'Low': '#10B981',
                        'Medium': '#F59E0B', 
                        'High': '#EF4444'
                    })
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🚨 Alerts")
        st.warning("⚠️ 3 patients require immediate attention")
        st.info("ℹ️ 12 new lab results pending review")
        st.success("✅ System updated to v1.2.0")
        
        # Quick Actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🔄 Run All Predictions"):
            st.success("Predictions completed!")
        
        if st.button("📥 Import Patient Data"):
            st.info("Import feature coming soon!")
    
    # Recent Predictions Table
    st.markdown('<div class="sub-header">📋 Recent Predictions</div>', unsafe_allow_html=True)
    
    sample_data = pd.DataFrame({
        'Patient ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
        'Name': ['John Smith', 'Jane Doe', 'Robert Brown', 'Maria Garcia', 'David Lee'],
        'Age': [45, 62, 58, 34, 71],
        'Cardio Risk': ['Medium', 'High', 'High', 'Low', 'High'],
        'Diabetes Risk': ['Low', 'Medium', 'High', 'Low', 'Medium'],
        'Last Check': ['2024-01-20', '2024-01-19', '2024-01-18', '2024-01-17', '2024-01-16']
    })
    
    st.dataframe(sample_data, use_container_width=True)

def show_patient_entry():
    """Patient data entry form"""
    st.markdown('<h1 class="main-header">👤 Patient Data Entry</h1>', unsafe_allow_html=True)
    
    with st.form("patient_form", clear_on_submit=True):
        st.markdown("### Personal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            age = st.number_input("Age", 0, 120, 45)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            phone = st.text_input("Phone Number")
        
        with col2:
            email = st.text_input("Email")
            address = st.text_area("Address")
            date_of_birth = st.date_input("Date of Birth", 
                                         value=datetime(1980, 1, 1),
                                         min_value=datetime(1900, 1, 1),
                                         max_value=datetime.today())
        
        st.markdown("---")
        st.markdown("### Medical Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            bp_systolic = st.slider("Systolic BP (mmHg)", 60, 200, 120)
            bp_diastolic = st.slider("Diastolic BP (mmHg)", 40, 120, 80)
            cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 400, 200)
            cholesterol_hdl = st.slider("HDL Cholesterol (mg/dL)", 20, 100, 50)
        
        with col2:
            glucose = st.slider("Fasting Glucose (mg/dL)", 50, 300, 95)
            bmi = st.slider("BMI", 15.0, 50.0, 25.0)
            weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
            height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
        
        st.markdown("### Lifestyle & History")
        
        col1, col2 = st.columns(2)
        
        with col1:
            smoking = st.selectbox("Smoking Status", 
                                  ["Never", "Former", "Current"])
            alcohol = st.selectbox("Alcohol Consumption",
                                 ["None", "Light", "Moderate", "Heavy"])
            activity = st.selectbox("Physical Activity",
                                  ["Sedentary", "Light", "Moderate", "Active"])
        
        with col2:
            diabetes_family = st.checkbox("Family History of Diabetes")
            heart_disease_family = st.checkbox("Family History of Heart Disease")
            stroke_family = st.checkbox("Family History of Stroke")
        
        st.markdown("### Symptoms")
        
        symptoms = st.multiselect("Select Symptoms",
                                 ["Chest Pain", "Shortness of Breath", "Fatigue",
                                  "Dizziness", "Headache", "Nausea", "Palpitations",
                                  "Swelling", "Vision Problems", "Numbness"])
        
        notes = st.text_area("Additional Notes")
        
        # Form submission
        submitted = st.form_submit_button("📥 Save Patient & Predict Risk")
        
        if submitted:
            # Validate input
            if not first_name or not last_name:
                st.error("Please enter patient name")
            else:
                # Simulate prediction
                with st.spinner("Analyzing data and predicting risks..."):
                    # Simulate processing time
                    import time
                    time.sleep(1)
                    
                    # Show success message
                    st.success(f"✅ Patient {first_name} {last_name} added successfully!")
                    
                    # Show mock prediction results
                    st.markdown("### 🎯 Risk Prediction Results")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Cardiovascular Risk", "MEDIUM", "72% confidence")
                    
                    with col2:
                        st.metric("Diabetes Risk", "LOW", "85% confidence")
                    
                    with col3:
                        st.metric("Overall Risk", "MEDIUM", "Needs monitoring")
                    
                    # Recommendations
                    st.markdown("### 💡 Recommendations")
                    st.info("""
                    1. Schedule follow-up in 6 months
                    2. Recommend cholesterol-lowering diet
                    3. Increase physical activity to 150 mins/week
                    4. Monitor blood pressure weekly
                    """)

def show_risk_prediction():
    """Risk prediction interface"""
    st.markdown('<h1 class="main-header">🔍 Disease Risk Prediction</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📋 Single Prediction", "📊 Batch Prediction", "📈 Model Comparison"])
    
    with tab1:
        st.markdown("### Predict Risk for Individual Patient")
        
        # Model selection
        col1, col2 = st.columns(2)
        with col1:
            model_choice = st.selectbox(
                "Select Prediction Model",
                ["Random Forest Ensemble", "XGBoost", "Neural Network", "All Models"]
            )
        
        with col2:
            diseases = st.multiselect(
                "Select Diseases to Predict",
                ["Cardiovascular Disease", "Diabetes", "Stroke", "Hypertension", "Kidney Disease"],
                default=["Cardiovascular Disease", "Diabetes"]
            )
        
        # Input form for prediction
        with st.expander("Enter Patient Data", expanded=True):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                age = st.slider("Age", 20, 90, 55)
                bp_systolic = st.slider("Systolic BP", 90, 200, 135)
                bmi = st.slider("BMI", 18, 45, 28)
            
            with col2:
                cholesterol = st.slider("Cholesterol", 150, 350, 220)
                glucose = st.slider("Glucose", 70, 250, 110)
                smoking = st.select_slider("Smoking", 
                                          options=["Never", "Former", "Current"])
            
            with col3:
                diabetes_history = st.checkbox("Diabetes History")
                heart_history = st.checkbox("Heart Disease History")
                physical_activity = st.select_slider("Activity Level",
                                                   options=["Sedentary", "Light", "Moderate", "Active"])
        
        # Prediction button
        if st.button("🎯 Predict Risk", type="primary", use_container_width=True):
            with st.spinner("Running AI analysis..."):
                # Simulate prediction
                import time
                time.sleep(2)
                
                # Show results
                st.success("✅ Prediction Complete!")
                
                # Results in metrics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("#### Cardiovascular")
                    st.metric("Risk Level", "HIGH", "89% confidence")
                    st.progress(89)
                
                with col2:
                    st.markdown("#### Diabetes")
                    st.metric("Risk Level", "MEDIUM", "67% confidence")
                    st.progress(67)
                
                with col3:
                    st.markdown("#### Overall")
                    st.metric("Risk Level", "HIGH", "Urgent attention needed")
                    st.progress(85)
                
                # Feature importance
                st.markdown("### 📊 Feature Importance")
                features = ['Age', 'BP', 'Cholesterol', 'Smoking', 'BMI', 'Glucose', 'Family History']
                importance = [0.25, 0.20, 0.15, 0.15, 0.10, 0.10, 0.05]
                
                fig = go.Figure(data=[go.Bar(x=importance, y=features, orientation='h')])
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)
                
                # Recommendations
                st.markdown("### 🩺 Medical Recommendations")
                st.warning("""
                **URGENT ACTION REQUIRED:**
                - Schedule cardiology consultation within 7 days
                - Start statin therapy immediately
                - Monitor BP twice daily
                - Lifestyle modification program
                """)
    
    with tab2:
        st.markdown("### Batch Prediction for Multiple Patients")
        st.info("Upload CSV file with patient data")
        
        uploaded_file = st.file_uploader("Choose CSV file", type="csv")
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())
            
            if st.button("🔮 Predict All", type="primary"):
                st.success(f"✅ Predictions completed for {len(df)} patients!")
                
                # Mock results
                results_df = pd.DataFrame({
                    'Patient ID': df.iloc[:5, 0] if len(df) > 0 else ['P001', 'P002', 'P003', 'P004', 'P005'],
                    'Cardio Risk': ['High', 'Medium', 'Low', 'High', 'Medium'],
                    'Diabetes Risk': ['Medium', 'Low', 'Low', 'High', 'Medium'],
                    'Confidence': [0.89, 0.75, 0.92, 0.81, 0.68]
                })
                
                st.dataframe(results_df)
                
                # Download button
                csv = results_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Predictions",
                    data=csv,
                    file_name="risk_predictions.csv",
                    mime="text/csv"
                )
    
    with tab3:
        st.markdown("### Model Performance Comparison")
        
        # Mock model comparison data
        models = ['Random Forest', 'XGBoost', 'Neural Net', 'Logistic Reg', 'SVM']
        accuracy = [0.94, 0.92, 0.91, 0.87, 0.85]
        precision = [0.93, 0.91, 0.90, 0.86, 0.84]
        recall = [0.92, 0.90, 0.89, 0.85, 0.83]
        
        comparison_df = pd.DataFrame({
            'Model': models,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall
        })
        
        st.dataframe(comparison_df.style.highlight_max(axis=0))
        
        # Performance chart
        fig = go.Figure(data=[
            go.Bar(name='Accuracy', x=models, y=accuracy),
            go.Bar(name='Precision', x=models, y=precision),
            go.Bar(name='Recall', x=models, y=recall)
        ])
        fig.update_layout(barmode='group', height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_analytics():
    """Analytics dashboard"""
    st.markdown('<h1 class="main-header">📈 System Analytics</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Prediction Trends")
        
        # Sample trend data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        predictions = [120, 145, 180, 210, 240, 280]
        high_risk = [15, 18, 22, 28, 32, 40]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=predictions, name='Total Predictions',
                                line=dict(color='blue', width=3)))
        fig.add_trace(go.Scatter(x=months, y=high_risk, name='High Risk Cases',
                                line=dict(color='red', width=3)))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Risk Factors Distribution")
        
        factors = ['High BP', 'High Chol', 'Diabetes', 'Smoking', 'Obesity']
        prevalence = [35, 28, 22, 18, 32]
        
        fig = px.pie(values=prevalence, names=factors, hole=0.4)
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Additional analytics
    st.markdown("### Patient Demographics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Age distribution
        st.markdown("#### Age Groups")
        age_data = pd.DataFrame({
            'Age Group': ['<30', '30-50', '50-70', '>70'],
            'Count': [120, 450, 520, 157]
        })
        st.dataframe(age_data, use_container_width=True)
    
    with col2:
        # Gender distribution
        st.markdown("#### Gender Distribution")
        gender_data = pd.DataFrame({
            'Gender': ['Male', 'Female'],
            'Count': [680, 567]
        })
        fig = px.pie(gender_data, values='Count', names='Gender')
        fig.update_layout(height=250)
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Risk by age
        st.markdown("#### High Risk by Age")
        risk_by_age = pd.DataFrame({
            'Age': ['<30', '30-50', '50-70', '>70'],
            'High Risk %': [2, 15, 42, 68]
        })
        st.bar_chart(risk_by_age.set_index('Age'))

def show_settings():
    """System settings"""
    st.markdown('<h1 class="main-header">⚙️ System Settings</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["General", "Model Settings", "Notifications"])
    
    with tab1:
        st.markdown("### General Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Hospital Name", "City General Hospital")
            st.selectbox("Timezone", ["UTC", "EST", "PST", "IST"])
            st.number_input("Data Retention (days)", 30, 3650, 730)
        
        with col2:
            st.checkbox("Enable Auto-backup", True)
            st.checkbox("Enable Audit Logging", True)
            st.checkbox("Enable Multi-language Support", False)
        
        if st.button("Save General Settings", type="primary"):
            st.success("Settings saved!")
    
    with tab2:
        st.markdown("### Model Configuration")
        
        model = st.selectbox("Active Model", 
                        ["Random Forest v2.1", "XGBoost v1.8", "Ensemble v3.0"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.slider("Confidence Threshold", 0.5, 0.95, 0.7, 0.05)
            st.slider("Retraining Frequency (days)", 7, 90, 30)
        
        with col2:
            st.checkbox("Enable Explainable AI", True)
            st.checkbox("Enable Ensemble Learning", True)
            st.checkbox("Auto-update Models", True)
        
        if st.button("Update Model Settings"):
            st.success("Model configuration updated!")
    
    with tab3:
        st.markdown("### Notification Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.checkbox("Email Alerts", True)
            st.checkbox("SMS Alerts", False)
            st.checkbox("Push Notifications", True)
        
        with col2:
            st.checkbox("High Risk Alerts", True)
            st.checkbox("System Health Alerts", True)
            st.checkbox("Daily Reports", True)
        
        st.text_input("Alert Email", "admin@hospital.com")
        
        if st.button("Save Notification Settings"):
            st.success("Notification settings saved!")

if __name__ == "__main__":
    main()