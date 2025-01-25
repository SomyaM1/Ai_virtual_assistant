import text_to_speech
import speech_to_text
import datetime
import webbrowser
def Action (data):
    user_data = data.lower()
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is virtual assistant")
        return "my name is virtual assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hi, how can i help you")
        return "hi, how can i help you"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning!")
        return "Good Morning!"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        time = (str)(current_time) + "hour:" ,(str)(current_time.minute) + "minute"
        text_to_speech.text_to_speech(time)
        return time
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay")
        return "Okay"
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com")
        text_to_speech.text_to_speech("spotify is ready to run")
        return "spotify is ready to run"
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com")
        text_to_speech.text_to_speech("youtube is ready to run")
        return "youtube is ready to run"
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com")
        text_to_speech.text_to_speech("Opening google")
        return "Opening google"
    else:
        text_to_speech.text_to_speech("i'm not able to understand")
        return "i'm not able to understand"