import pyttsx3  # importinf the libary
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import face


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1])
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Evening!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Morning!")

    speak("I am jeetu Bhayia sir. Please tell me how may I help you!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_thresold = 1
        r.energy_thresold = 300
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("user said:" , query)
    except Exception as e:
        speak("Please say it again...")
        return "None"
    return(query)

def sendEmail(to, content):
    server = sntplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('virenderpalsingh1997@gmail.com','google1997')
    server.sendmail('virenderpalsingh1997@gmail.com',to,content)
    server.close()

def assistance():
    
    while 1:
        
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query or 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query or 'google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query or 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query or 'music' in query:
            music_dir = r'C:\Users\Virender Pal Singh\Desktop\songs\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(("sir the time is",strTime))
        elif 'open code' in query or 'code' in query:
            path =r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\pythonw.exe" "C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\Lib\idlelib\idle.pyw'
            os.startfile(path)
        elif 'email to veeru' in query:
            try:
                speak('what should I say')
                content = takeCommand()
                to = 'virenderpalsingh280@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("sorry my friend viru bahi . I am not able to send this email")
                
        
        elif 'thank you' in query:
            speak("Your welcome sir")
            speak("I am always there for helping you sir!")
            
            
name = face.camera_on()
if name != None:
    speak("Hello " + str(name) + "you looking Awsome today")
    speak("we met last time...!")
else:
    speak("You looking new to me, lets first we know each other.")
    speak("My name is Jeetu and pepole called me jeetu bhayia.")
    speak("My work is helping Student like You")
    speak("What your name")
    i = input("Enter the name: ")
    speak("Hello " + str(i) + "you looking Awsome today")
wishMe()
assistance()

