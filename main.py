import sys
import requests
import speech_recognition as sr
import pyttsx3

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from random_word import RandomWords
r = RandomWords()

r.get_random_word()

DICTIONARY_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

recognizer = sr.Recognizer()
mic = sr.Microphone()
console = Console()


def say(text, print_text=True):
    if print_text:
        console.print(f"[bold bright_cyan]say-It:[/bold bright_cyan] {text}")

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def lookup_word(word):

    try:
        with console.status(f"[yellow]Looking up '{word}'...[/yellow]", spinner="dots"):
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

    console.print(
        Panel(
            f"[bold white]{word}[/bold white]\n\n"
            f"[green]Meaning:[/green] {definition}"
            + (f"\n[magenta]Example:[/magenta] {example}" if example else ""),
            title="[bold]Dictionary Result[/bold]",
            border_style="green",
            box=box.ROUNDED,
            expand=False,
        )
    )

    say(message, print_text=False)


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
    text = console.input("[bold green]saY-It > [/bold green]")

    if not text.strip():
        say("Invalid input! You entered nothing.")
        return

    process_text(text)


def speakfn():
    say("Listening. Please speak now.")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            with console.status("[yellow]Listening...[/yellow]", spinner="point"):
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        with console.status("[yellow]Recognizing speech...[/yellow]", spinner="dots"):
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
    raw_choice = console.input("[bold green]saY-It > [/bold green]")

    try:
        choice = int(raw_choice)
    except ValueError:
        say("Invalid input! Please enter a number: 1, 2, 3 or 4.")
        return

    if choice == 1:
        textfn()
    elif choice == 2:
        speakfn()
    elif choice == 3:
        vocabfn()
    elif choice == 4:
        exitfn()
    else:
        say("No such option. Please choose 1, 2, or 3.")


def show_menu(active, menu, speak_options=True):
    voice_menu = (
        "   Choose one of the following options. "
        "Option one, Text. "
        "Option two, Speak. "
        "Option three, Vocab. "
        "Option four, Exit."
    )

    console.print()
    console.print(
        Panel(
            menu.strip(),
            title=f"[bold bright_cyan]say-It[/bold bright_cyan] — {active}",
            border_style="bright_cyan",
            box=box.ROUNDED,
            expand=False,
            padding=(1, 3),
        )
    )

    if speak_options:
        say(f"{active}{voice_menu}", print_text=False)
    else:
        say(active, print_text=False)


def main():
    console.print(
        Panel.fit(
            Text.from_markup(
                "[bold magenta]say-It[/bold magenta]\n"
                "[dim]Your voice & text dictionary assistant[/dim]",
                justify="center",
            ),
            border_style="magenta",
            box=box.DOUBLE,
        )
    )

    active_message = "Initializing say-It"
    menu_text = (
        "1. TEXT\n"
        "2. SPEAK\n"
        "3. VOCAB\n"
        "4. EXIT"
    )

    show_menu(active_message, menu_text)

    while True:
        get_choice()
        show_menu("Returning to menu", menu_text, speak_options=False)


if __name__ == "__main__":
    main()