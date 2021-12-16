import pyttsx3 #pip install
import datetime
import speech_recognition as sr #pip install
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')#windows voice 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)






def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else:
        speak("good evening")
    speak("I am your assistant sir. Pleas tell me how may i help you")

def takeCommand():
    #it takes audio input and returns string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .5
        r.energy_threshold = 1000
        audio=r.listen(source)
    try:
        print("Recognising.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")       
    except Exception as e:     
        print("say that again please....")
        return "None"
    return query



if __name__=="__main__" :
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
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
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        

 