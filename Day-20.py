#Text to Speech Project

import pyttsx3

engine = pyttsx3.init()

def text_speech(text):
    engine.say(text)
    engine.runAndWait()
text_speech("Hello, I am Your Assistant")
    
