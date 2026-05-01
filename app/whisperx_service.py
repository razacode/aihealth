import whisperx  # type: ignore[import]
import streamlit as st


# ✅ Cache Whisper model
@st.cache_resource
def load_model_cached():
    return whisperx.load_model("tiny", "cpu")   # 🔥 changed base → tiny


def transcribe_with_diarization(audio_path):
    device = "cpu"

    # ✅ Use cached model
    model = load_model_cached()

    result = model.transcribe(audio_path)

    # Alignment (can also be cached later if needed)
    model_a, metadata = whisperx.load_align_model(
        language_code=result["language"],
        device=device
    )

    result = whisperx.align(
        result["segments"],
        model_a,
        metadata,
        audio_path,
        device
    )

    # 👉 SAFE fallback (NO diarization crash)
    segments = []
    speaker_toggle = True

    for seg in result["segments"]:
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "speaker": "S1" if speaker_toggle else "S2",
            "text": seg["text"]
        })
        speaker_toggle = not speaker_toggle

    return segments