import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import cam
import os
import subprocess as sub
from pygame import mixer
from tkinter import *
from PIL import Image, ImageTk

main_window = Tk()
main_window.title = ("Lizzy AI")

main_window.geometry("800x400")

main_window.resizable(False, False)


name = "lizzy"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites = {
    'google': 'https://google.com/',
    'bing': 'https://www.bing.com/search?q=',
    'wikipedia': 'https://en.wikipedia.org/wiki/'
}

files = {
    'mi arte': 'mi arte.png',
    'documento': 'documento.docx'
}

programs = {
    'brave': r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",

}


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    while True:
        try:
            with sr.Microphone() as source:
                print("Escuchando ...")
                pc = listener.listen(source)
                rec = listener.recognize_google(pc, language="es")
                rec = rec.lower()
                if name in rec:
                    rec = rec.replace(name, '')
        except:
            pass
        return rec


def run_lizzy():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
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
        elif 'puedes verme' in rec:
            talk("Esta bien")
            cam.mirame()
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
            for app in programs:
                if app in rec:
                    talk(f'Abriendo {app}')
                    os.startfile(programs[app])
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abriendo {file}')
        elif 'escribe' in rec:
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", 'a')
                write(file)

        elif 'termina' in rec:
            talk('Adios!')
            break


def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)
    
main_window.mainloop()