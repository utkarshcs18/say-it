# say-It

> **Type it. Say it. Hear it. Learn it.**

say-It is a Python-powered command-line application that transforms words into an interactive learning experience. Whether you type a word or speak it through your microphone, say-It instantly recognizes it, pronounces it aloud, and displays its meaning—all from your terminal.

---

## Features

* **Voice Recognition** – Speak a word naturally using your microphone.
* **Text Input** – Prefer typing? Enter any word or sentence directly.
* **Text-to-Speech** – Hear the correct pronunciation of the word.
* **Instant Definitions** – Fetch word meanings and examples from a dictionary API.
* **Beautiful UI** – Features a clean and colorful terminal interface using Rich.
* **Fast & Lightweight** – Runs entirely from the terminal.

---

## Demo

```text
$ python main.py

╔══════════════════════════════════════╗
║                say-It                ║
║  Your voice & text dictionary assistant  ║
╚══════════════════════════════════════╝

╭── say-It — Initializing say-It ──╮
│ 1. TEXT                          │
│ 2. SPEAK                         │
│ 3. EXIT                          │
╰──────────────────────────────────╯
saY-It > 1
say-It: Please enter your text.
saY-It > eloquent
Looking up 'eloquent'...
say-It: The word is eloquent. It means: Fluent or persuasive in speaking or writing.
╭─ Dictionary Result ──────────────╮
│ eloquent                         │
│                                  │
│ Meaning: Fluent or persuasive in │
│ speaking or writing.             │
╰──────────────────────────────────╯
```

---

## 🏗️ How It Works

```text
                User
                  │
        ┌─────────┴─────────┐
        │                   │
    ⌨️ Type            🎤 Speak
        │                   │
        └─────────┬─────────┘
                  │
          Recognized Word
                  │
      ┌───────────┴───────────┐
      │                       │
🔊 Text-to-Speech      📚 Dictionary API
      │                       │
      └───────────┬───────────┘
                  │
       Hear the Word + Learn Meaning
```

---

## Tech Stack

| Technology           | Purpose                             |
| -------------------- | ----------------------------------- |
|    Python            | Core application logic              |
|    SpeechRecognition | Converts speech to text             |
|    PyAudio           | Captures microphone input           |
|    pyttsx3           | Offline text-to-speech              |
|    Rich              | Beautiful terminal UI formatting    |
|    Requests          | API communication                   |
|    Dictionary API    | Retrieves word definitions/examples |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/utkarshcs18/say-it.git
cd say-it
```

It is recommended to use a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install requests SpeechRecognition pyttsx3 rich pyaudio
```

Run the application:

```bash
python main.py
```

---

## Why say-It?

Learning a new word shouldn't require opening multiple websites or apps.

With say-It, you can:

* ✔️ Hear how a word is pronounced.
* ✔️ Learn its meaning and usage instantly.
* ✔️ Practice speaking it correctly.
* ✔️ Build your vocabulary effortlessly.

Everything happens in one simple, elegant terminal application.

---

## 📂 Project Structure

```text
say-it/
│
├── main.py       # Core application script
├── README.md     # Documentation
├── .gitignore    # Git ignore rules
└── venv/         # Virtual environment
```

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork the project.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Built With ❤️

> **Speak it. Hear it. Understand it.**
