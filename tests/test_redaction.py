from app.redact import redact_text

def test_redaction():
    text = "My name is Rahul and my number is 9876543210"

    redacted_text, redaction_map = redact_text(text)

    assert "[REDACTED_NAME]" in redacted_text
    assert "[REDACTED_PHONE]" in redacted_text