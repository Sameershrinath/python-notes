from datetime import datetime

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
def speak(text):
     engine.say(text)
     engine.runAndWait()

current = datetime.now()
hour = current.hour  # Extract the hour directly from the datetime object
print(f'Time is {current}')
if 3 <= hour < 12:
    print("Good Morning Sir!")
    speak("Good Morning Sir")
elif 12 <= hour < 16:
    print('Good Afternoon')
    speak("Good Afternoon Sir")
elif 16 <= hour < 21:
    print('Good Evening')
    speak("Good Evening Sir")
else:
    print("Good Night")
    speak("Good Night Sir")
