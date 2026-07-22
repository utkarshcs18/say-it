# 🎙️ say-It

> **Type it. Say it. Hear it. Learn it.**

SpeakSense is a Python-powered command-line application that transforms words into an interactive learning experience. Whether you type a word or speak it through your microphone, SpeakSense instantly recognizes it, pronounces it aloud, and displays its meaning—all from your terminal.

---

## 🚀 Features

* 🎤 **Voice Recognition** – Speak a word naturally using your microphone.
* ⌨️ **Text Input** – Prefer typing? Enter any word directly.
* 🔊 **Text-to-Speech** – Hear the correct pronunciation instantly.
* 📚 **Instant Definitions** – Fetch word meanings from a dictionary API.
* ⚡ **Fast & Lightweight** – Runs entirely from the terminal.
* 🐍 **Built with Python** – Simple, clean, and easy to extend.

---

## 🖥️ Demo

```text
$ python main.py

──────────────────────────────────────
        Welcome to say-It
──────────────────────────────────────

1. Type a Word
2. Speak a Word

> 2

🎤 Listening...

✅ You said: eloquent

🔊 Pronouncing...

📖 Meaning:
Fluent or persuasive in speaking or writing.
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
      Hear the Word + Learn the Meaning
```

---

## 🛠️ Tech Stack

| Technology           | Purpose                    |
| -------------------- | -------------------------- |
| 🐍 Python            | Core application           |
| 🎤 SpeechRecognition | Converts speech to text    |
| 🎙️ PyAudio           | Captures microphone input  |
| 🔊 pyttsx3           | Offline text-to-speech     |
| 🌐 Requests          | API communication          |
| 📖 Dictionary API    | Retrieves word definitions |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/utkarshcs18/say-it.git
```

Move into the project directory:

```bash
cd say-it
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 💡 Why SpeakSense?

Learning a new word shouldn't require opening multiple websites or apps.

With SpeakSense, you can:

* ✔️ Hear how a word is pronounced.
* ✔️ Learn its meaning instantly.
* ✔️ Practice speaking it correctly.
* ✔️ Build your vocabulary effortlessly.

Everything happens in one simple terminal application.

---

## 📂 Project Structure

```text
say-it/
│
├── main.py
├── README.md
└── assets/
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

**Speak it. Hear it. Understand it.**
