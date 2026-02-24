# webapp/components/forms.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

def create_patient_form(app: dash.Dash):
    """Patient health input form for risk prediction"""

    layout = html.Div([
        html.H3("Patient Risk Prediction Form"),
        html.Div([
            html.Label("Age"),
            dcc.Input(id="age-input", type="number", min=0, max=120, value=30)
        ]),
        html.Div([
            html.Label("Gender"),
            dcc.Dropdown(id="gender-input", options=[
                {'label': 'Male', 'value': 'Male'},
                {'label': 'Female', 'value': 'Female'},
                {'label': 'Other', 'value': 'Other'}
            ], value='Male')
        ]),
        html.Div([
            html.Label("Existing Conditions"),
            dcc.Checklist(
                id="conditions-input",
                options=[
                    {'label': 'Diabetes', 'value': 'diabetes'},
                    {'label': 'Hypertension', 'value': 'hypertension'},
                    {'label': 'Heart Disease', 'value': 'heart_disease'}
                ],
                value=[]
            )
        ]),
        html.Button("Predict Risk", id="predict-btn", n_clicks=0),
        html.Div(id="prediction-output", style={'marginTop': 20})
    ], style={'padding': 20, 'maxWidth': 500})

    @app.callback(
        Output("prediction-output", "children"),
        Input("predict-btn", "n_clicks"),
        State("age-input", "value"),
        State("gender-input", "value"),
        State("conditions-input", "value")
    )
    def predict_risk(n_clicks, age, gender, conditions):
        if n_clicks > 0:
            # Dummy risk calculation logic
            risk_score = 0
            risk_score += age / 2
            risk_score += len(conditions) * 15
            risk_category = "High" if risk_score > 50 else "Medium" if risk_score > 25 else "Low"
            return f"Predicted Risk Score: {risk_score:.2f} ({risk_category})"
        return ""

    return layout
