# utils.py
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def contains_keywords(text, keywords):
    return any(keyword in text for keyword in keywords)
