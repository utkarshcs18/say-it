import sys
import requests
import speech_recognition as sr
import pyttsx3
import time

DICTIONARY_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

recognizer = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def input():
    choose = int(input("> "))
    engine.say(f"You have Choosed {choose} option")


def speak(active, menu, voice_menu):
    print("saY-It: ", active)
    print(menu)

    engine.say(f"{active}.{voice_menu}")
    engine.runAndWait()
    input()

def initial(active,menu):
    voice_menu = (
        "Choose any 1 among these: "
        "Option one, Text. "
        "Option two, Speak. "
        "Option three, Exit."
    )
    speak(active, menu, voice_menu)




if __name__ == "__main__":
    initial("Initializing say-It","\nChoose any 1 among these: \n 1. TEXT \n 2. SPEAK \n 3. EXIT")
    session_active = False
    last_command_time = None


