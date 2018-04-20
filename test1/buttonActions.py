#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
from wordSearchFile import wordSearch
#from interface import Ui_Dialog
#from main import getObject
#testing k liye tha
def test():
    tts = gTTS(text="hello", lang='en')
    print(tts)
   # if os.path.isfile("hello.mp3"):
    #    os.remove("hello.mp3")
    tts.save("a.mp3")
    print("saved")
    playsound("a.mp3")
    print("sound played")

def press():



    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Say something!")
        audio = r.listen(source)
        print("done listening")

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        string = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said: " + string)

        #if os.path.isfile("audio.mp3"):
        #    os.remove("audio.mp3")

        #tts = gTTS(text="hello", lang='en')
        #tts.save("hello.mp3")
        #playsound("hello.mp3")

        wordSearch(string)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# if 'copy' in string:
#     print("found copy")
#     commond="cp"