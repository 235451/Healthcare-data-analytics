# webapp/components/history_timeline.py

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

history_df = pd.read_csv("Data/raw/patient_health_india.csv")  # Example dataset

def create_history_timeline(app: dash.Dash):
    """Patient history timeline visualization"""

    fig = px.line(history_df, x="date", y="risk_score", color="patient_id",
                title="Patient Risk History Timeline")

    layout = html.Div([
        html.H3("Patient History Timeline"),
        dcc.Graph(figure=fig)
    ], style={'padding': 20})

    return layout
