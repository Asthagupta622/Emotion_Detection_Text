# Emotion_Detection_Text
# 🧠 Emotion Detection Web App (Text + Audio)

This project is a local web app that detects human emotions from either text input or audio speech using a trained machine learning model and OpenAI's Whisper for audio transcription. It is built with Streamlit and runs completely offline — no external APIs used.

---

## 🚀 Features

- 📄 **Text Input**: Enter a sentence or paragraph and detect its emotional tone  
- 🎤 **Audio Input**: Upload a voice clip (MP3/WAV) — Whisper transcribes and classifies the emotion  
- 💾 **Runs locally**: All models are run on your machine  
- 🔧 **Built with**: `streamlit`, `scikit-learn`, `openai-whisper`, `joblib`, `torch`  

---

## 📁 Project Structure

```
Emotion_Detection_Website/
├── app.py                 # Main Streamlit app
├── emotion_model.pkl      # Trained ML model for emotion classification
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
```

---

## 🛠️ Installation

1. 🔁 Clone this repository or download the files:

```bash
git clone https://github.com/yourusername/emotion-detection-streamlit.git
cd emotion-detection-streamlit
```

2. 📦 Install required packages:

```bash
pip install -r requirements.txt
```

> Make sure `ffmpeg` is installed and added to your system PATH if using audio.

3. ▶️ Run the app locally:

```bash
streamlit run app.py
```

---

## 🧪 Example Emotions

| Sample Text                              | Predicted Emotion |
|------------------------------------------|--------------------|
| I am feeling very low today              | sadness            |
| This is the best day of my life!         | joy                |
| I'm so angry I could scream              | anger              |

---

## 🔊 Audio Input

- Upload a `.wav` or `.mp3` file of you speaking  
- Whisper will transcribe it to text  
- The model will predict the emotion of the transcribed sentence  

---

## 📦 requirements.txt

```
streamlit
joblib
openai-whisper
torch
scikit-learn
ffmpeg-python
```

---

## 🤖 Model Details

- Trained using `train.txt` with text and emotion labels  
- Preprocessed using `neattext`, `TfidfVectorizer`  
- Classifier: `Multinomial Naive Bayes`  
- Saved using `joblib` as `emotion_model.pkl`  

---

## 📌 Notes

- Whisper can be slow to load on first run  
- For fast startup, switch from `"base"` to `"tiny"` model in `app.py`  
- All processing is done locally — no internet required after setup  

---

## 📜 License

This project is open-source and free to use for learning and academic purposes.

---

## 🙋‍♀️ Author

**Astha Gupta**  
*Aspiring Machine Learning Engineer*
![Screenshot 2025-05-15 193837](https://github.com/user-attachments/assets/80f5860a-5dc6-421d-8df1-ccd4a246ad66)
