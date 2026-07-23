import pyttsx3

engine = pyttsx3.init(driverName="sapi5")

engine.say("Hello")
engine.say("How are you?")
engine.say("Third sentence")

engine.runAndWait()