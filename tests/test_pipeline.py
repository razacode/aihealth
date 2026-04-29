from app.segment import segment_text

def test_segmentation():
    text = "This is a sample medical conversation about paracetamol and BP levels"
    segments = segment_text(text)

    assert len(segments) > 0
    assert "speaker_id" in segments[0]