import re

def redact_text(text: str):
    redaction_map = []

    # Phone numbers
    def redact_phone(match):
        redaction_map.append({
            "type": "phone",
            "value": match.group(),
        })
        return "[REDACTED_PHONE]"

    # Names (simple heuristic: capitalized words)
    def redact_name(match):
        redaction_map.append({
            "type": "name",
            "value": match.group(),
        })
        return "[REDACTED_NAME]"

    # Dates (simple)
    def redact_date(match):
        redaction_map.append({
            "type": "date",
            "value": match.group(),
        })
        return "[REDACTED_DATE]"

    text = re.sub(r"\b\d{10}\b", redact_phone, text)
    text = re.sub(r"\b[A-Z][a-z]{3,}\b", redact_name, text)
    text = re.sub(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", redact_date, text)

    return text, redaction_map