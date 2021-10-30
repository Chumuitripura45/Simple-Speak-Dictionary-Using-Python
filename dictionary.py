from PyDictionary import PyDictionary
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice)
        print(text)
except:
    pass

def jak():
    dictionary = PyDictionary()
    go = dictionary.meaning(text)
    print(go)
    talk(go)

jak()