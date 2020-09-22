import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print('Initializing Jarvis')

MASTER = "Tanish"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
       speak("Good Evening" + MASTER) 

    speak("Hi I am Jarvis. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please unable to recognize")
        query = None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tk3102008@gmail.com', 'Bullet@123*')
    server.sendmail("shubh9350@gmail.com", to, content)
    server.close()

def main():
    speak('Initializing Jarvis...')
    wishMe()
    query = takeCommand()


    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipidea", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "reddit.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        #webbrowser.open("youtube.com") 
        url = "https://play.google.com/music/listen?u=0#/home"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'vs' in query.lower():
        codePath = "E:\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "Shubh9350@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent Sucessfully")
        except Exception as e:
            print(e)



main()
