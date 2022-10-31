import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)
def reception():
    print("WELCOME")
    print("Your Health is our Priority")
    speech.say("WELCOME")
    speech.runAndWait()

    speech.say("Your Health is our Priority")
    speech.runAndWait()

    speech.say("How may i help you today?")
    speech.runAndWait()
