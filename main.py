import pyttsx3
import SpeechRecognition as sr
import datetime
import wikipedia
import webbrowser
import os

#Taking Voice form the system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',100)  

#speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello i am programmer,how are how?")