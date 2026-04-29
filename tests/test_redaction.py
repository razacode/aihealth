from app.redact import redact_text

def test_redaction():
    text = "My name is John and my number is 9876543210"
    redacted, mapping = redact_text(text)

    assert "[REDACTED_NAME]" in redacted
    assert "[REDACTED_PHONE]" in redacted
    assert len(mapping) >= 2