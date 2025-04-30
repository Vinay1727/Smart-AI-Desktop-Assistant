from assistant import greet_user, perform_task, speak
from recognizer import listen_command
import time
from datetime import datetime

def banner():
    print(r"""
     ____                  _     _     _             _     
    / ___| _ __ ___   ___ | |__ (_)___| |_ __ _ _ __| |__  
    \___ \| '_ ` _ \ / _ \| '_ \| / __| __/ _` | '__| '_ \ 
     ___) | | | | | | (_) | | | | \__ \ || (_| | |  | | | |
    |____/|_| |_| |_|\___/|_| |_|_|___/\__\__,_|_|  |_| |_|    
    ~ Smart AI Desktop Assistant ~
    """)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Launching assistant...")

def main():
    banner()
    greet_user()

    WAKE_WORD = "hey assistant"
    activated = False

    try:
        while True:
            if not activated:
                command = input("Type something: ").lower()
                if WAKE_WORD in command:
                    speak("Yes, I am listening.")
                    print("Activated. Awaiting command...")
                    activated = True
                else:
                    print("Waiting for wake word...")
                time.sleep(1)
            else:
                user_command = input("Command: ").lower()
                if user_command:
                    if "exit" in user_command or "quit" in user_command:
                        speak("Goodbye! Have a great day.")
                        print("Session ended.")
                        break
                    perform_task(user_command)
                    speak("What is the next task? I am waiting...")
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n[!] Assistant terminated manually.")
        speak("Shutting down. Goodbye!")

if __name__ == "__main__":
    main()
