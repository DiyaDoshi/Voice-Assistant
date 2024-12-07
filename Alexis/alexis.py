import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pywin32_system32

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Change the voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female (in most setups)

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print("The current time is ", Time)

def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The current date is {day}/{month}/{year}")

def wishme() -> None:
    print("Welcome back Mam!!")
    speak("Welcome back Mam!!")

    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Mam!!")
        print("Good Morning Mam!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Mam!!")
        print("Good Afternoon Mam!!")
    elif 16 <= hour < 24:
        speak("Good Evening Mam!!")
        print("Good Evening Mam!!")
    else:
        speak("Good Night Mam, See You Tomorrow")

    speak("Alexis at your service Mam, please tell me how may I help you.")
    print("Alexis at your service Mam, please tell me how may I help you.")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)

def takecommand():
    r = sr.Recognizer()

    # Adjust the energy threshold to be more sensitive to low-volume speech
    r.energy_threshold = 300

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        print("Listening...")

        r.pause_threshold = 1  # Slight pause in speech before recognizing the next word
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Timeout and phrase limit
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")
            speak("I didn't hear anything. Please try again.")
            return "Try Again"
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            speak("Sorry, I couldn't understand. Please try again.")
            return "Try Again"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("There seems to be an issue with the speech recognition service.")
            return "Try Again"

    return query

if __name__ == "__main__":
    try:
        wishme()
        while True:
            query = takecommand().lower()

            if "time" in query:
                time()

            elif "date" in query:
                date()

            elif "who are you" in query:
                speak("I'm Alexis created by Miss Diya and I'm a desktop voice assistant.")
                print("I'm Alexis"
                      ""
                      ""
                      " created by Miss Diya and I'm a desktop voice assistant.")

            elif "how are you" in query:
                speak("I'm fine Mam, What about you?")
                print("I'm fine Mam, What about you?")

            elif "fine" in query or "good" in query:
                speak("Glad to hear that Mam!!")
                print("Glad to hear that Mam!!")

            elif "wikipedia" in query:
                try:
                    speak("Ok wait Mam, I'm searching...")
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=2)
                    print(result)
                    speak(result)
                except:
                    speak("Can't find this page Mam, please ask something else")

            elif "open youtube" in query:
                wb.open("youtube.com")

            elif "open google" in query:
                wb.open("google.com")

            elif "open stack overflow" in query:
                wb.open("stackoverflow.com")

            elif "play music" in query:
                song_dir = os.path.expanduser("~\\Music")
                songs = os.listdir(song_dir)
                print(songs)
                x = len(songs)
                y = random.randint(0, x - 1)  # Index should be within the list's range
                os.startfile(os.path.join(song_dir, songs[y]))

            elif "open chrome" in query:
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif "search on chrome" in query:
                try:
                    speak("What should I search?")
                    print("What should I search?")
                    chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    search = takecommand()
                    wb.get(chromePath).open_new_tab(search)
                    print(search)
                except Exception as e:
                    speak("Can't open now, please try again later.")
                    print("Can't open now, please try again later.")

            elif "remember that" in query:
                speak("What should I remember")
                data = takecommand()
                speak("You said me to remember that " + data)
                print("You said me to remember that " + str(data))
                remember = open("data.txt", "w")
                remember.write(data)
                remember.close()

            elif "do you remember anything" in query:
                remember = open("data.txt", "r")
                speak("You told me to remember that " + remember.read())
                print("You told me to remember that " + str(remember))

            elif "screenshot" in query:
                screenshot()
                speak("I've taken a screenshot, please check it.")

            elif "offline" in query:
                speak("Going offline. Goodbye, sir!")
                print("Going offline. Goodbye, sir!")
                break  # Exit the loop and end the program.

    except KeyboardInterrupt:
        speak("Program interrupted. Goodbye, Mam!")
        print("Program interrupted. Goodbye, Mam!")
        quit()
