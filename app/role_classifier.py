def classify_role(text):
    text = text.lower()

    doctor_keywords = [
        "since when", "are you", "have you", "do you",
        "prescribe", "take this", "check", "recommend"
    ]

    patient_keywords = [
        "i have", "i am", "pain", "fever",
        "headache", "vomiting", "i feel"
    ]

    for word in doctor_keywords:
        if word in text:
            return "Doctor"

    for word in patient_keywords:
        if word in text:
            return "Patient"

    return "Unknown"