# recognizer.py
import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, service is down.")
        return ""
    
    return command.lower()
