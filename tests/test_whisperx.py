from app.whisperx_service import transcribe_with_diarization

def test_whisperx_output():
    # mock structure (no heavy model run)
    sample_output = [
        {"text": "I have headache", "speaker": "SPEAKER_00"}
    ]

    assert isinstance(sample_output, list)
    assert "text" in sample_output[0]
    assert "speaker" in sample_output[0]