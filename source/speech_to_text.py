from fileinput import filename
from pkg_resources import safe_extra
import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)