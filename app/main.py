from whisperx_service import transcribe_with_diarization
from redact import redact_text
from utils import save_output

audio_path = "data/input/dp.wav"

segments = transcribe_with_diarization(audio_path)

full_text = " ".join([seg["text"] for seg in segments])

redacted_text, redaction_map = redact_text(full_text)

output = {
    "segments": segments,
    "redacted_transcript": redacted_text,
    "redaction_map": redaction_map
}

save_output(output)

print(output)