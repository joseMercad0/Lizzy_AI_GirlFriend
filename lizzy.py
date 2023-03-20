import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia, datetime, keyboard
from pygame import mixer

name = "lizzy"
listener=sr.Recognizer() 
engine = pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',145)


def talk(text):
      engine.say(text)
      engine.runAndWait()
def listen():
     try:
         with sr.Microphone() as source:
             print("Escuchando ...")
             pc = listener.listen(source)
             rec = listener.recognize_google(pc, language="es")
             re= rec.lower()
             if name in rec:
                 rec = rec.replace(name,'')

     except:
        pass
     return rec

def run_juanita():
   rec = listen()
   if 'reproduce' in rec:
      music = rec.replace('reproduce','')
      print("Reproduciendo " +  music) 
      talk("Reproduciendo " + music) 
      pywhatkit.playonyt(music)
    
   elif 'busca'in rec:
        search = rec.replace('busca','')
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(search, 1)
        print(search +": "+ wiki) 
        talk(wiki)
   elif 'alarma' in rec:
        num = rec.replace('alarma','')
        num = num.strip()
        talk("Alarma activada a las " + num + "horas") 
        while True:
            if datetime.datetime.now().strftime('%H:%M') == num:
             print("DESPIERTA!!!") 
             mixer.init()
             mixer.music.load("alarma1.mp3")
             mixer.music.play()
             if keyboard .read_key() == 's':
                mixer.music.stop()
                break

    
      
if __name__=='__main__': 
    run_juanita()