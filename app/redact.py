import re

def redact_text(text):
    redaction_map = []

    def redact_name(match):
        redaction_map.append({
            "type": "name",
            "value": match.group(2)
        })
        return match.group(1) + " [REDACTED_NAME]"

    text = re.sub(
        r"(my name is|I am|this is)\s+([A-Z][a-z]+)",
        redact_name,
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"\b\d{10}\b", "[REDACTED_PHONE]", text)

    text = re.sub(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", "[REDACTED_DATE]", text)

    return text, redaction_map