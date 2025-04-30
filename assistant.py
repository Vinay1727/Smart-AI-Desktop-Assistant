import os
import webbrowser
import pyttsx3
import pywhatkit as kit
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import time

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# assistant.py

def greet_user():
    speak("Hello! How can I assist you today?")

def perform_task(command):
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open instagram" in command or "open insta" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "open whatsapp" in command or "open whatsapp" in command:
        webbrowser.open("https://www.whatsapp.com")
    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            os.startfile(chrome_path)
            speak("Opening Chrome")
        else:
            speak("Chrome is not installed in the default location.")
    elif "open file explorer" in command or "open this pc" in command:
        os.startfile("explorer.exe")
        speak("Opening File Explorer")
    elif "open vscode" in command:
        vscode_path = r"C:\\Users\\PCLP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.lnk"
        if os.path.exists(vscode_path):
            os.startfile(vscode_path)
            speak("Opening Visual Studio Code")
        else:
            speak("VS Code is not installed in the default location.")
    elif "open notepad" in command:
        os.startfile("notepad.exe")
        speak("Opening Notepad")

def send_email(recipient, subject, body):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    receiver_email = recipient

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            speak("Email sent!")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

def play_music():
    speak("Playing music from YouTube.")
    webbrowser.open("https://www.youtube.com/results?search_query=music")

def authenticate():
    with open('credentials.json') as f:
        credentials = json.load(f)

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == credentials["username"] and password == credentials["password"]:
        speak("Authentication successful!")
    else:
        speak("Authentication failed.")

# Example of calling the function
if __name__ == "__main__":
    while True:
        command = input("Type a command: ").lower()

        if "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            break

        perform_task(command)
