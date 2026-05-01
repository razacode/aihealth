# Clinical Audio AI (Prototype)

## Features
Uses WhisperX for transcription and speaker diarization in a unified pipeline.
- Audio → Text (Whisper)
- Redaction (Name, Phone, Date)
- Structured Segments
- JSON Output

## Run

```bash
pip install -r requirements.txt
python app/main.py data/input/sample.wav