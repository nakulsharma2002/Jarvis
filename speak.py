import pyttsx3
import datetime
import speech_recognition as sr
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 130)  # Set speaking rate
engine.setProperty('volume', 1.0)  # Set volume level (1.0 is the maximum)

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().strftime('%H'))
    if 0 <= hour < 12:
        speak('Good morning, sir')
    elif 12 <= hour < 18:
        speak('Good afternoon, sir')
    elif 18 <= hour < 20:
        speak('Good evening, sir')
    else:
        speak('Good night, sir')

def takecommand():
    """Listen to the user's command and convert it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise with dynamic energy threshold
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1  # Set pause threshold
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("I didn't catch that. Please say it again.")
        return "None"
    except sr.RequestError:
        print("Couldn't request results; check your network connection.")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
        command = takecommand()
        if command.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye, sir")
            break
        time.sleep(2)  # Wait for 5 seconds before listening again
