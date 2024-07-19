import pyttsx3
import datetime
import speech_recognition as sr
import time
from mtranslate import translate
from colorama import Fore,Style,init
init(autoreset=True)


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 240)  # Set speaking rate
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


def Trans_hindi_to_english(txt):
    english_Txt = translate(txt,to_language="en-in")
    return english_Txt


def save_file(query):
    print("visit")
    with open('C:\\Users\\snaku\\OneDrive\\Desktop\\python\\Advanced_Jarvis\\Txt\\Question.txt','w') as f:
            f.write(f"{query}")
            f.close()

def takecommand():
    """Listen to the user's command and convert it to text."""
    r = sr.Recognizer()
    # Adjust for ambient noise with dynamic energy threshold
    r.dynamic_energy_threshold = False
    r.energy_threshold =35000
    r.dynamic_energy_adjustment_damping = 0.03
    r.dynamic_energy_ratio = 1.9
    r.operation_timeout = None
    r.non_speaking_duration = 0.3
    r.pause_threshold = 0.5  # Set pause threshold
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTGREEN_EX + "I am Listening...")
            try:
                audio = r.listen(source,timeout=None)
                # print(Fore.LIGHTYELLOW_EX + "Got it Now Recognizing",end=" ",flush=True)
                query = r.recognize_google(audio, language='en-in')
                # print(Fore.LIGHTGREEN_EX,f"User said: {audio}\n",flush=True)
                if query:
                    translated_txt = Trans_hindi_to_english(query)
                    print("\r"+Fore.BLUE + "Mr Nakul : ", translated_txt)
                    
                    # query send to Question.txt
                    print("go")
                    save_file(translated_txt)
                else:
                    return ""
            
            except sr.UnknownValueError:
                print(Fore.LIGHTYELLOW_EX + "I didn't catch that. Please say it again.")
                return "None"
            except sr.RequestError:
                print(Fore.LIGHTYELLOW_EX + "Couldn't request results; check your network connection.")
                return "None"
            
            return translated_txt



if __name__ == '__main__':
    
    while True:
        command = takecommand()
        
