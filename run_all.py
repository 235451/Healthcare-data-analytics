# run_all.py
import subprocess
import os

# Run ML scripts
ml_scripts = [
    "src/data_ingestion.py",
    "src/database_handler.py",
    "src/doctor_logic.py",
    "src/explainability.py",
    "src/feature_engineering.py",
    "src/govt_patient_id.py",
    "src/medical_history.py",
    "src/model_training.py",
    "src/preprocessing.py",
    "src/prediction.py"
]

for script in ml_scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])

# Run web app
print("Starting web app...")
subprocess.run(["python", "webapp/app.py"])
