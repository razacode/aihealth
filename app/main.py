import sys
from transcribe import transcribe_audio
from redact import redact_text
from segment import segment_text
from utils import save_output

def run_pipeline(audio_path):
    print("🔊 Transcribing...")
    text = transcribe_audio(audio_path)

    print("🔐 Redacting...")
    redacted_text, redaction_map = redact_text(text)

    print("🧩 Segmenting...")
    segments = segment_text(redacted_text)

    output = {
        "segments": segments,
        "redacted_transcript": redacted_text,
        "redaction_map": redaction_map
    }

    save_output(output)

    print("\n✅ Done! Output saved to data/output/output.json\n")
    print(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py data/input/sample.wav")
    else:
        run_pipeline(sys.argv[1])