import wikipedia
import pyjokes
import requests
import pywhatkit
import speech_recognition as sr
import pyttsx3
from decouple import config
from datetime import datetime
from random import choice
from utils import opening_text
from os_ops import *
from online_ops import *

USERNANE = config("USER")
BOTNAME = config("BOT")

engine = pyttsx3.init("sapi5")
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 190)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Speaks Whatever text is passed"""

    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets user whenever called"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNANE}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNANE}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNANE}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    """Takes user input, recognises it using speech-recognition, and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        if 'exit' in query or 'stop' in query or 'quit' in query:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        elif "free" in query:
            speak(choice(opening_text))
        else: 
            print(query)
            query="None"
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

if __name__=='__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        if query:
            if 'open notepad' in query:
                open_notepad()

            elif 'open discord' in query:
                open_discord()

            elif 'open command prompt' in query or 'open cmd' in query:
                open_cmd()

            elif 'open camera' in query:
                open_camera

            elif 'open calculator' in query:
                open_calculator()

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif 'wikipedia' in query:
                speak('What do you want to search on Wikipedia, sir?')
                search_query = take_user_input().lower()
                try:
                    results = search_on_wikipedia(search_query)
                    speak(f"According to Wikipedia, {results}")
                    speak("For your convenience, I am printing it on the screen sir.")
                    print(results)
                except wikipedia.exceptions.PageError:
                    speak(f"No page matches {search_query}")

            elif 'youtube' in query:
                speak('What do you want to play on Youtube, sir?')
                video = take_user_input().lower()
                play_on_youtube(video)

            elif 'search on google' in query:
                ('What do you want to search on Google, sir?')
                query = take_user_input().lower()
                search_on_google(query)

            elif "send whatsapp message" in query:
                speak('On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message sir?")
                message = take_user_input().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message sir.")