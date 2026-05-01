#  Clinical Audio AI

AI-powered system to convert doctor–patient audio into:
- 📝 Clean transcript
- 👥 Speaker-separated conversation
- 🔐 Redacted sensitive information


##  Features

- 🎧 Upload `.wav` audio
- 🧠 Speech-to-text using WhisperX
- 👥 Speaker segmentation (S1 / S2)
- 💬 Chat-style Doctor–Patient UI
- 🔐 Automatic redaction (names, phone numbers, etc.)
- 📊 Timeline with timestamps
- 📥 Download structured JSON output



## Run

```bash
pip install -r requirements.txt
source venv/Scripts/activate
python -m streamlit run app/ui.py
