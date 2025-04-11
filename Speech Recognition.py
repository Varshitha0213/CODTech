!pip install -q SpeechRecognition
!pip install -q pydub
import speech_recognition as sr
from pydub import AudioSegment
import io
from IPython.display import Audio
from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
    if fn.endswith(".mp3"):
        sound = AudioSegment.from_mp3(fn)
        fn = fn.replace(".mp3", ".wav")
        sound.export(fn, format="wav")
recognizer = sr.Recognizer()
audio_file = sr.AudioFile(fn)

with audio_file as source:
    audio_data = recognizer.record(source)
    print("🎙️ Recognizing...")
    try:
        text = recognizer.recognize_google(audio_data)
        print("✅ Transcribed Text:\n", text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print("❌ API error:", e)
