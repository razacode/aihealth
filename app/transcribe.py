import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.1-essentials_build\ffmpeg-8.1-essentials_build\bin"
import whisper

_model = None

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model

def transcribe_audio(audio_path: str) -> str:
    model = get_model()
    result = model.transcribe(audio_path, fp16=False)
    return result.get("text", "")