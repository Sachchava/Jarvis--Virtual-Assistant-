import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
   
   def takecommand():
       r = sr.Recognizer()
       with sr.Microphone()  as source:
           print("listening......")
           r.pause_threshold = 1
           audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            print("recognizing.....")
            query = r.recognize_google(audio, language'en-in')
            print(f"user said: {query}")

        except Exception as e:
           speak("SAY THAT AGAIN PLEASE")
           return "none"
           return query

    if __name__ == "__main__":
        speak("this is advance jarvis")