# api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# Define the EXACT same data structure as your client
class PatientData(BaseModel):
    name: str
    age: int
    gender: str
    blood_pressure: int
    cholesterol: int
    diabetes: bool
    smoking: bool
    alcohol_intake: bool
    physical_activity_level: str  # "low", "medium", "high"

app = FastAPI(title="Healthcare Risk Prediction API")

# Add CORS middleware - CRITICAL for allowing connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {
        "message": "Healthcare Risk Prediction API",
        "status": "running",
        "endpoints": {
            "predict": "POST /predict",
            "health": "GET /health"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(data: PatientData):
    """Predict health risk based on patient data"""
    
    # Calculate a simple risk score (replace with your actual ML model)
    risk_score = 0.0
    
    # Age factor
    if data.age > 50:
        risk_score += 0.2
    elif data.age > 40:
        risk_score += 0.1
    
    # Blood pressure factor
    if data.blood_pressure > 140:
        risk_score += 0.3
    elif data.blood_pressure > 130:
        risk_score += 0.15
    
    # Cholesterol factor
    if data.cholesterol > 240:
        risk_score += 0.25
    elif data.cholesterol > 200:
        risk_score += 0.1
    
    # Lifestyle factors
    if data.smoking:
        risk_score += 0.3
    if data.diabetes:
        risk_score += 0.25
    if data.alcohol_intake:
        risk_score += 0.1
    
    # Physical activity reduces risk
    if data.physical_activity_level == "high":
        risk_score -= 0.2
    elif data.physical_activity_level == "medium":
        risk_score -= 0.1
    
    # Cap risk score between 0 and 1
    risk_score = max(0.0, min(1.0, risk_score))
    
    # Determine risk category
    if risk_score > 0.7:
        risk_category = "High Risk"
        recommendation = "Immediate medical consultation recommended"
    elif risk_score > 0.4:
        risk_category = "Moderate Risk"
        recommendation = "Schedule a check-up within 2 weeks"
    else:
        risk_category = "Low Risk"
        recommendation = "Maintain healthy lifestyle"
    
    return {
        "patient_name": data.name,
        "risk_category": risk_category,
        "risk_score": round(risk_score, 3),
        "confidence": 0.89,  # Placeholder
        "recommendation": recommendation,
        "analysis": {
            "age_contribution": "Increased risk" if data.age > 50 else "Normal",
            "bp_status": "Hypertensive" if data.blood_pressure > 140 else "Normal",
            "cholesterol_status": "High" if data.cholesterol > 200 else "Normal"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)