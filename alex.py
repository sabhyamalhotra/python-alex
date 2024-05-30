import  pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import warnings
import datetime
import os
import pyautogui

warnings.simplefilter('ignore')

def speak(text):
    engine = pyttsx3.init()
    voices= engine.getProperty('voices')
    id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', id)
    print("")
    print(f"==> Alex AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")
        return query.lower()
    except:
        return ""
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alex Sir. Please tell me how may I help you")

def MainExecution(query):
    query = str(query).lower()

    
    if "hello" in query:
        speak("Hello sir, what soul")
    elif "bye" in query:
        speak("Bye everyone")
    elif "time" in query:
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        speak(f"The time now is : {time} ")
    elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")

    elif 'open worst' in query:
            webbrowser.open("https://www.alliance.edu.in")
            
    elif 'open alliance' in query:
            webbrowser.open("https://www.alliance.edu.in")
    elif 'open presentation' in query:
            codePath = "C:\\Users\\sabhya100\\Desktop\\AI Voice assistant.pptx"
            os.startfile(codePath)
    elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("alex","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
         

wishMe()
while True:
    print(" ")
   
    query=speechrecognition()
    MainExecution(query)