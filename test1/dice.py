#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from appJar import gui
from playsound import playsound
from gtts import gTTS

from PyQt5 import QtCore, QtGui, QtWidgets

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
        print("Google Speech Recognition thinks you said " + string)

        tts = gTTS(text=string, lang='en')
        tts.save("hello.mp3")
        playsound('hello.mp3')

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.startBTN = QtWidgets.QPushButton(Dialog)
        self.startBTN.setGeometry(QtCore.QRect(20, 400, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startBTN.setFont(font)
        self.startBTN.setObjectName("startBTN")
        self.exitBTN = QtWidgets.QPushButton(Dialog)
        self.exitBTN.setGeometry(QtCore.QRect(530, 370, 75, 23))
        self.exitBTN.setObjectName("exitBTN")
        self.textBox = QtWidgets.QTextBrowser(Dialog)
        self.textBox.setGeometry(QtCore.QRect(30, 20, 581, 192))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBox.setFont(font)
        self.textBox.setObjectName("textBox")

        self.retranslateUi(Dialog)
        #self.startBTN.released.connect(self.textBox.setText(self,"say something"));
        self.startBTN.released.connect(press);
        self.exitBTN.released.connect(exit);
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startBTN.setText(_translate("Dialog", "Start"))
        self.exitBTN.setText(_translate("Dialog", "Exit"))
        self.textBox.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press the start button to begin</p></body></html>"))

if __name__ == "__main__":
    print("starting app")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    print("ending app")






# if 'copy' in string:
#     print("found copy")
#     commond="cp"