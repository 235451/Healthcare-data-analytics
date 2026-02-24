/* =========================================================
SAMPLE DATA – GOVERNMENT HOSPITAL (INDIA)
   ========================================================= */

/* ============================
PATIENTS
   ============================ */
INSERT INTO patients VALUES
('GOV-IND-0001','Ramesh Kumar',45,'Male','4821','9876543210','Chennai',CURRENT_TIMESTAMP),
('GOV-IND-0002','Sita Devi',60,'Female','9274','9123456780','Delhi',CURRENT_TIMESTAMP),
('GOV-IND-0003','Arjun Singh',32,'Male','1109','9988776655','Lucknow',CURRENT_TIMESTAMP);

/* ============================
DOCTORS
   ============================ */
INSERT INTO doctors VALUES
('DOC-001','Dr. Anil Sharma','Cardiology','Senior Consultant','9991112222','ADMIN',CURRENT_TIMESTAMP),
('DOC-002','Dr. Meena Iyer','General Medicine','Medical Officer','8882223333','DOCTOR',CURRENT_TIMESTAMP);

/* ============================
MEDICAL HISTORY
   ============================ */
INSERT INTO medical_history
(patient_id, condition, diagnosed_date, severity, notes)
VALUES
('GOV-IND-0001','Hypertension','2018-06-10','Moderate','On medication'),
('GOV-IND-0002','Diabetes Type 2','2015-03-22','Severe','Poor glucose control'),
('GOV-IND-0003','Asthma','2020-11-01','Mild','Seasonal');

/* ============================
VITALS
   ============================ */
INSERT INTO vitals
(patient_id, systolic_bp, diastolic_bp, heart_rate, spo2, temperature)
VALUES
('GOV-IND-0001',150,95,88,96,98.6),
('GOV-IND-0002',170,100,92,94,99.1),
('GOV-IND-0003',120,80,72,98,98.4);

/* ============================
LAB REPORTS
   ============================ */
INSERT INTO lab_reports
(patient_id, test_name, result_value, normal_range, report_date)
VALUES
('GOV-IND-0001','Cholesterol','240 mg/dL','<200 mg/dL','2024-01-15'),
('GOV-IND-0002','HbA1c','9.2%','<5.7%','2024-01-20'),
('GOV-IND-0003','Pulmonary Function','Normal','Normal','2024-01-18');

/* ============================
AI PREDICTIONS
   ============================ */
INSERT INTO ai_predictions
(patient_id, disease, risk_score, risk_category, model_version)
VALUES
('GOV-IND-0001','Heart Disease',0.78,'High','v1.0'),
('GOV-IND-0002','Diabetic Complications',0.89,'Critical','v1.0'),
('GOV-IND-0003','Respiratory Issue',0.22,'Low','v1.0');

/* ============================
PRESCRIPTIONS
   ============================ */
INSERT INTO prescriptions
(patient_id, doctor_id, medicine_name, dosage, duration, notes)
VALUES
('GOV-IND-0001','DOC-001','Amlodipine','5mg once daily','30 days','Monitor BP'),
('GOV-IND-0002','DOC-002','Metformin','500mg twice daily','60 days','Diet control advised');

/* ============================
DOCTOR–AI CHAT LOGS
   ============================ */
INSERT INTO doctor_ai_chats
(patient_id, doctor_id, doctor_query, ai_response)
VALUES
('GOV-IND-0001','DOC-001',
'Patient BP persistently high. Next steps?',
'Increase antihypertensive dose and suggest lifestyle changes.'),
('GOV-IND-0002','DOC-002',
'High HbA1c detected. Risk assessment?',
'High risk of complications. Immediate glucose control required.');
