from ipaddress import ip_address
import ipaddress
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json').json()
    return ip_address['ip']

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    """Requires to be logged in whatsapp web"""

    kit.sendwhatmsg_instantly(f"+91{number}", message)

