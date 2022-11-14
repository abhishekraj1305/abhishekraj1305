import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")

    elif hour>=12 and hour<18:
        speak("good Afternoon!")    

    else:
        speak("good evening!")

    speak("i'm your Assistant sir, please tell me how may i help you")   

def takecommand():
    #it takes command input from the user and return string output
         
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        print("recognizing...")    
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")        
        return"None"
    return query    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')  

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')  

        elif 'play music' in query:
            music_dir = 'D:\\songs\\new temprory songs'
            songs = os.listdir(music_dir)
            print(songs)        
            os.startfile(os.path.join(music_dir, songs[0]))

