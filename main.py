import sys
import requests
import speech_recognition as sr
import pyttsx3

DICTIONARY_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

recognizer = sr.Recognizer()
mic = sr.Microphone()


def say(text, print_text=True):
    if print_text:
        print(f"say-It: {text}")

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def lookup_word(word):

    try:
        response = requests.get(DICTIONARY_API_URL.format(word), timeout=5)

        if response.status_code == 404:
            return None

        response.raise_for_status()
        data = response.json()

        entry = data[0]
        phonetic = entry.get("phonetic", "")

        if not phonetic:
            for p in entry.get("phonetics", []):
                if p.get("text"):
                    phonetic = p["text"]
                    break

        meaning = entry["meanings"][0]
        definition_entry = meaning["definitions"][0]
        definition = definition_entry.get("definition", "")
        example = definition_entry.get("example", "")

        return phonetic, definition, example

    except requests.exceptions.RequestException:
        return "network_error"
    except (KeyError, IndexError):
        return None


def speak_word_result(word, result):
    if result == "network_error":
        say(f"Sorry, I could not reach the dictionary service to look up {word}. Please check your internet connection.")
        return

    if result is None:
        say(f"Sorry, I could not find a definition for {word}.")
        return

    phonetic, definition, example = result

    message = f"The word is {word}."
    message += f" It means: {definition}."
    if example:
        message += f" For example: {example}."

    say(message)


def process_text(text):
    say(f"{text}")

    words = text.strip().split()

    if not words:
        say("You entered an empty input. Please try again.")
        return

    if len(words) == 1:
        result = lookup_word(words[0])
        speak_word_result(words[0], result)
    else:
        say("You entered multiple words. I will look up the meaning of each word one by one.")
        for word in words:
            clean_word = word.strip(".,!?;:\"'").lower()
            if not clean_word:
                continue
            result = lookup_word(clean_word)
            speak_word_result(clean_word, result)


def textfn():
    say("Please enter your text.")
    text = input("saY-It > ")

    if not text.strip():
        say("Invalid input! You entered nothing.")
        return

    process_text(text)


def speakfn():
    say("Listening. Please speak now.")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        recognized_text = recognizer.recognize_google(audio)
        process_text(recognized_text)

    except sr.WaitTimeoutError:
        say("I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        say("Sorry, I could not understand what you said.")
    except sr.RequestError:
        say("Sorry, the speech recognition service is unavailable right now.")


def exitfn():
    say("Goodbye! Closing say-It now.")
    sys.exit(0)


def get_choice():
    raw_choice = input("saY-It > ")

    try:
        choice = int(raw_choice)
    except ValueError:
        say("Invalid input! Please enter a number: 1, 2, or 3.")
        return

    say(f"You entered option {choice}")

    if choice == 1:
        textfn()
    elif choice == 2:
        speakfn()
    elif choice == 3:
        exitfn()
    else:
        say("No such option. Please choose 1, 2, or 3.")


def show_menu(active, menu, speak_options=True):
    voice_menu = (
        "   Choose one of the following options. "
        "Option one, Text. "
        "Option two, Speak. "
        "Option three, Exit."
    )

    print(f"say-It: {active}")
    print(menu)

    if speak_options:
        say(f"{active}{voice_menu}", print_text=False)
    else:
        say(active, print_text=False)


def main():
    active_message = "Initializing say-It"
    menu_text = (
        "\nChoose any one among these:\n"
        "1. TEXT\n"
        "2. SPEAK\n"
        "3. EXIT"
    )

    show_menu(active_message, menu_text)

    while True:
        get_choice()
        show_menu("Returning to menu", menu_text, speak_options=False)


if __name__ == "__main__":
    main()