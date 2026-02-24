/* =========================================================
GOVERNMENT HOSPITAL AI MEDICAL SYSTEM
DATABASE SCHEMA
   ========================================================= */

PRAGMA foreign_keys = ON;

/* ============================
PATIENT MASTER
   ============================ */
CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK(age >= 0),
    gender TEXT CHECK(gender IN ('Male','Female','Other')),
    aadhaar_last4 TEXT,
    phone TEXT,
    address TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

/* ============================
DOCTORS TABLE
   ============================ */
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    designation TEXT,
    phone TEXT,
    role TEXT CHECK(role IN ('ADMIN','DOCTOR')) DEFAULT 'DOCTOR',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

/* ============================
MEDICAL HISTORY
   ============================ */
CREATE TABLE IF NOT EXISTS medical_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    condition TEXT,
    diagnosed_date DATE,
    severity TEXT CHECK(severity IN ('Mild','Moderate','Severe')),
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

/* ============================
VITALS DATA
   ============================ */
CREATE TABLE IF NOT EXISTS vitals (
    vitals_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    systolic_bp INTEGER,
    diastolic_bp INTEGER,
    heart_rate INTEGER,
    spo2 INTEGER,
    temperature REAL,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

/* ============================
LAB REPORTS
   ============================ */
CREATE TABLE IF NOT EXISTS lab_reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    test_name TEXT,
    result_value TEXT,
    normal_range TEXT,
    report_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

/* ============================
AI RISK PREDICTIONS
   ============================ */
CREATE TABLE IF NOT EXISTS ai_predictions (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    disease TEXT,
    risk_score REAL CHECK(risk_score BETWEEN 0 AND 1),
    risk_category TEXT CHECK(risk_category IN ('Low','Medium','High','Critical')),
    model_version TEXT,
    predicted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

/* ============================
MEDICAL PRESCRIPTIONS
   ============================ */
CREATE TABLE IF NOT EXISTS prescriptions (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    doctor_id TEXT,
    medicine_name TEXT,
    dosage TEXT,
    duration TEXT,
    notes TEXT,
    prescribed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

/* ============================
DOCTOR–AI CHAT LOGS
   ============================ */
CREATE TABLE IF NOT EXISTS doctor_ai_chats (
    chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    doctor_id TEXT,
    doctor_query TEXT,
    ai_response TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
