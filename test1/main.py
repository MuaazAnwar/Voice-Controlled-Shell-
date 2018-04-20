# from PyQt5 import QtCore, QtGui, QtWidgets
# import interface
# from interface import Ui_Dialog
# import speech_recognition as sr
# from playsound import playsound
# from gtts import gTTS
# import os
# from wordSearchFile import wordSearch


# print("starting app")
# import sys
#
#
#
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = interface.Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())
# print("ending app")
#

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

        # if os.path.isfile("audio.mp3"):
        #    os.remove("audio.mp3")

        # tts = gTTS(text="hello", lang='en')
        # tts.save("hello.mp3")
        # playsound("hello.mp3")

        wordSearch(string)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))