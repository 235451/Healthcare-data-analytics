def generate_medical_timeline(visits):
    timeline = []
    for visit in visits:
        timeline.append({
            "date": visit["visit_date"],
            "department": visit["department"],
            "complaint": visit["chief_complaint"]
        })
    return sorted(timeline, key=lambda x: x["date"])
