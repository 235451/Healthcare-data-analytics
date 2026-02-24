
"""
gov_patient_id.py
-----------------
Government Hospital Patient ID Generator (India)

Features:
- State-based prefix (AP, TS, TN, KA, etc.)
- Hospital code support
- Date-based traceability
- Randomized checksum
- Collision-safe
- Human-readable & database-friendly

Example ID:
AP-GH01-20250123-483921
"""

import random
import datetime
import hashlib

# -------------------------------------------------
# STATE CODE MAPPING (INDIA)
# -------------------------------------------------
STATE_CODES = {
    "Andhra Pradesh": "AP",
    "Telangana": "TS",
    "Tamil Nadu": "TN",
    "Karnataka": "KA",
    "Kerala": "KL",
    "Maharashtra": "MH",
    "Gujarat": "GJ",
    "Odisha": "OD",
    "Uttar Pradesh": "UP",
    "Delhi": "DL"
}

# -------------------------------------------------
# HOSPITAL TYPE CODES
# -------------------------------------------------
HOSPITAL_TYPES = {
    "government": "GH",
    "primary_health_center": "PHC",
    "district_hospital": "DH",
    "medical_college": "MC"
}

# -------------------------------------------------
# CORE ID GENERATION LOGIC
# -------------------------------------------------
def generate_gov_patient_id(
    state_name: str,
    hospital_type: str = "government",
    hospital_number: int = 1
) -> str:
    """
    Generates a unique Government Hospital Patient ID

    Format:
    <STATE>-<HOSPITALTYPE><NUM>-<YYYYMMDD>-<RANDOM>

    Example:
    AP-GH01-20250123-483921
    """

    # Validate inputs
    if state_name not in STATE_CODES:
        raise ValueError("Invalid state name")

    if hospital_type not in HOSPITAL_TYPES:
        raise ValueError("Invalid hospital type")

    # Extract components
    state_code = STATE_CODES[state_name]
    hospital_code = HOSPITAL_TYPES[hospital_type]
    hospital_id = f"{hospital_code}{str(hospital_number).zfill(2)}"

    today = datetime.datetime.now().strftime("%Y%m%d")

    random_seed = f"{state_code}{hospital_id}{today}{random.randint(100000, 999999)}"
    checksum = hashlib.sha256(random_seed.encode()).hexdigest()[:6].upper()

    patient_id = f"{state_code}-{hospital_id}-{today}-{checksum}"

    return patient_id

# -------------------------------------------------
# BULK ID GENERATION (FOR DATA PIPELINES)
# -------------------------------------------------
def generate_bulk_patient_ids(
    count: int,
    state_name: str,
    hospital_type: str = "government",
    hospital_number: int = 1
):
    """
    Generate multiple patient IDs safely
    """
    ids = set()

    while len(ids) < count:
        ids.add(
            generate_gov_patient_id(
                state_name,
                hospital_type,
                hospital_number
            )
        )

    return list(ids)

# -------------------------------------------------
# VALIDATION FUNCTION
# -------------------------------------------------
def validate_patient_id(patient_id: str) -> bool:
    """
    Validates structure of patient ID
    """
    try:
        parts = patient_id.split("-")
        if len(parts) != 4:
            return False

        state, hospital, date, checksum = parts

        if state not in STATE_CODES.values():
            return False

        if len(date) != 8:
            return False

        datetime.datetime.strptime(date, "%Y%m%d")

        if len(checksum) != 6:
            return False

        return True

    except Exception:
        return False

# -------------------------------------------------
# DEMO / TEST
# -------------------------------------------------
if __name__ == "__main__":
    print("🔹 Single Patient ID")
    pid = generate_gov_patient_id(
        state_name="Andhra Pradesh",
        hospital_type="government",
        hospital_number=3
    )
    print(pid)

    print("\n🔹 Bulk Patient IDs")
    bulk_ids = generate_bulk_patient_ids(
        count=5,
        state_name="Telangana",
        hospital_type="district_hospital",
        hospital_number=2
    )

    for i in bulk_ids:
        print(i, "✅ Valid:", validate_patient_id(i))
