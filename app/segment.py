def segment_text(text: str, chunk_size: int = 12):
    words = text.split()
    segments = []

    speaker_toggle = True

    for i in range(0, len(words), chunk_size):
        chunk = words[i:i + chunk_size]

        speaker_id = "S1" if speaker_toggle else "S2"
        speaker_toggle = not speaker_toggle

        segment = {
            "start_ts": i,
            "end_ts": i + len(chunk),
            "speaker_id": speaker_id,
            "text": " ".join(chunk),
            "language_tag": "en"
        }

        segments.append(segment)

    return segments