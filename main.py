import sys
import requests
import speech_recognition as sr
import pyttsx3

DICTIONARY_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

recognizer = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()
engine.setProperty("rate", 150)


def get_choice():
    choice = int(input("saY-It > "))

    engine.say(f"You have chosen option {choice}")
    engine.runAndWait()

    return choice


def speak(active, menu, voice_menu):
    print(f"say-It: {active}")
    print(menu)

    engine.say(f"{active}{voice_menu}")
    engine.runAndWait()
    
    return get_choice()


def initial(active, menu):
    voice_menu = (
        "   Choose one of the following options. "
        "Option one, Text. "
        "Option two, Speak. "
        "Option three, Exit."
    )

    return speak(active, menu, voice_menu)


if __name__ == "__main__":
    choice = initial(
        "Initializing say-It",
        "\nChoose any one among these:\n"
        "1. TEXT\n"
        "2. SPEAK\n"
        "3. EXIT"
    )

    print(f"Selected option: {choice}")