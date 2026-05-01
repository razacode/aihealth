import streamlit as st
import os
from whisperx_service import transcribe_with_diarization
from redact import redact_text
from utils import save_output

st.set_page_config(page_title="Clinical Audio AI", layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.title("🩺 Clinical Audio AI")
st.markdown("Upload audio → Transcribe → Detect Speakers → Redact Sensitive Data")

# -------------------------------
# TEXT CLEANING FUNCTION
# -------------------------------
def clean_text(text):
    text = text.strip()

    # remove junk patterns
    if len(text) < 3:
        return ""
    if text.count(".") > 5:
        return ""
    if text.replace(".", "").isdigit():
        return ""

    return text


# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader("📤 Upload .wav file", type=["wav"])

if uploaded_file:
    file_path = f"data/input/{uploaded_file.name}"

    # ensure directory exists
    os.makedirs("data/input", exist_ok=True)

    # save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded!")

    # 🎧 audio player
    st.audio(file_path)

    # -------------------------------
    # RUN ANALYSIS
    # -------------------------------
    if st.button("🚀 Run Analysis"):

        progress = st.progress(0)
        status = st.empty()

        # STEP 1: TRANSCRIPTION
        status.text("🔊 Transcribing audio...")
        progress.progress(20)

        segments = transcribe_with_diarization(file_path)

        # STEP 2: CLEANING
        status.text("🧠 Cleaning transcript...")
        progress.progress(50)

        cleaned_segments = []
        for seg in segments:
            cleaned = clean_text(seg["text"])
            if cleaned:
                cleaned_segments.append({**seg, "text": cleaned})

        full_text = " ".join([seg["text"] for seg in cleaned_segments])
        full_text = full_text.replace("  ", " ")

        # STEP 3: REDACTION
        status.text("🔐 Redacting sensitive data...")
        progress.progress(80)

        redacted_text, redaction_map = redact_text(full_text)

        output = {
            "segments": cleaned_segments,
            "redacted_transcript": redacted_text,
            "redaction_map": redaction_map
        }

        save_output(output)

        progress.progress(100)
        status.text("✅ Done!")

        # -------------------------------
        # TABS
        # -------------------------------
        tab1, tab2, tab3 = st.tabs([
            "📝 Transcript",
            "🔐 Redacted",
            "👥 Conversation (Timeline)"
        ])

        # -------------------------------
        # TAB 1 - TRANSCRIPT
        # -------------------------------
        with tab1:
            st.subheader("Full Transcript")
            st.write(full_text)

        # -------------------------------
        # TAB 2 - REDACTED
        # -------------------------------
        with tab2:
            st.subheader("Redacted Transcript")
            st.write(redacted_text)

        # -------------------------------
        # TAB 3 - CHAT WITH TIMELINE
        # -------------------------------
        with tab3:
            st.subheader("Doctor-Patient Conversation")

            for seg in cleaned_segments:
                time_range = f"[{seg['start']:.2f} - {seg['end']:.2f}]"
                speaker_id = seg["speaker"]

                if speaker_id == "S1":
                    st.markdown(
                        f"""
                        <div style='padding:10px;border-radius:10px;margin:5px'>
                        🧑‍⚕️ <b> ({speaker_id})</b> 
                        <span style="color:gray;font-size:12px">{time_range}</span><br>
                        {seg['text']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div style='padding:10px;border-radius:10px;margin:5px'>
                        🧑 <b> ({speaker_id})</b> 
                        <span style="color:gray;font-size:12px">{time_range}</span><br>
                        {seg['text']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        # -------------------------------
        # DOWNLOAD BUTTON
        # -------------------------------
        st.download_button(
            label="📥 Download Output JSON",
            data=str(output),
            file_name="output.json",
            mime="application/json"
        )