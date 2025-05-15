import streamlit as st
import joblib
import whisper
import tempfile
@st.cache_resource
def load_model():
    return joblib.load("emotion_model.pkl")
@st.cache_resource
def load_whisper():
    return whisper.load_model("tiny")
emotion_model = load_model()
whisper_model = load_whisper()
def predict_emotion(text):
    return emotion_model.predict([text])[0]

st.title("Emotion Detection from Text & Audio")
option = st.radio("Choose input type:", ("Text", "Audio"))

if option == "Text":
    user_text = st.text_area(" Enter your text:")
    if st.button("Predict Emotion"):
        if not user_text.strip():
            st.warning("Please enter some text.")
        else:
            emotion = predict_emotion(user_text)
            st.success(f"Predicted Emotion: **{emotion}**")
else:
    uploaded_audio = st.file_uploader(" Upload audio file (.mp3 or .wav)", type=["mp3", "wav"])
    if uploaded_audio is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_audio.read())
            tmp_path = tmp.name

        if st.button("Transcribe & Predict"):
            result = whisper_model.transcribe(tmp_path)
            transcribed_text = result["text"]
            st.markdown(f"**Transcribed Text:** {transcribed_text}")
            emotion = predict_emotion(transcribed_text)
            st.success(f"Predicted Emotion: **{emotion}**")
