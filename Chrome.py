import speech_recognition as sr
import pyttsx3
import pywhatkit
from facerecognition import *
from eyeballmouse import *

listener = sr.Recognizer ()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('hello sir i am chrome')
engine.say('what can i do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
             command= command.replace('alexa', '')
             print(command)

                

    except:
        pass
    return command

command = take_command()

def run_chrome():

    if 'play' in command:
        object = command.replace('play' , '')
        talk('playing' + object)
        pywhatkit.playonyt(object)


run_chrome()

def hello():

    if 'alexa hello' in command:
        talk('hello sir')
        talk('how may i help you')

hello()

def facerecognition ():

    if 'face' in command:
        facerecog()

facerecognition()

def eyeballmouse():
    if 'initiate i' in command:
        mouse()

eyeballmouse()
