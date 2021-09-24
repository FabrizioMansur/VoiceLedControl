# REMEMBER TO INSTALL PLAYAUDIO , PyObcJ, PLAYSOUND
import pyttsx3
import speech_recognition as sr
import ControlWithVoice as cnt

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# speak("Hello Iam Chando Dhar")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        audio = r.listen(source)
        try:
            print("Recognize............")
            query = r.recognize_google(audio, language='it-IT')
        except Exception as e:
            print("Try Again.......")
            return "None"
        return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'tutte' in query:
            print("accendo.........")
            speak("va bene....")
            cnt.led('accendi')
        elif 'spegni' in query:
            print("spengo.........")
            speak("ok.........")
            cnt.led('spegni')
        elif 'blu' in query:
            print("blu.........")
            speak("ok.........")
            cnt.led('blu')
        elif 'verde' in query:
            print("verde.........")
            speak("ok.........")
            cnt.led('verde')
        elif 'rosso' in query:
            print("rosso.........")
            speak("ok.........")
            cnt.led('rosso')
        elif 'giallo' in query:
            print("giallo.........")
            speak("ok.........")
            cnt.led('giallo')
        elif 'bianco' in query:
            print("bianco.........")
            speak("lutché bianca.........")
            cnt.led('bianco')
        elif 'prime due' in query:
            print("blu e verde.........")
            speak("blue e verdé.........")
            cnt.led('prime due')
        elif 'ultime due' in query:
            print("gialla e bianca.........")
            speak("gialla et biaenca.........")
            cnt.led('ultime due')
        elif 'prime tre' in query:
            print("verde blu rosso.........")
            speak("blue verde et rossa.........")
            cnt.led('prime tre')
        elif 'ultime tre' in query:
            print("rosso giallo bianco.........")
            speak("rossa gialla et biaenca.........")
            cnt.led('ultime tre')
        elif 'esci' in query:
            break
