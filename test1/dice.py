#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from appJar import gui
from playsound import playsound
from gtts import gTTS

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 90, 161, 171))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 70, 351, 301))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "helo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
#
#
# def press(button):
#
#     app.setMessage("l1", "Say something...")
#     # obtain audio from the microphone
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#
#         print("Say something!")
#         audio = r.listen(source)
#         print("done listening")
#
#     # recognize speech using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         string = r.recognize_google(audio)
#         print("Google Speech Recognition thinks you said " + string)
#
#         tts = gTTS(text=string, lang='en')
#         tts.save("hello.mp3")
#         playsound('hello.mp3')
#
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#
# app = gui("Voice Controlled Shell")
#
# app.startFrame("LEFT", row=0, column=0)
#
# app.setSticky("NEW")
# app.setStretch("COLUMN")
#
# app.addMessage("l1","Press the mic button to start")
#
#
# app.stopFrame()
#
# app.startFrame("RIGHT", row=0, column=1)
# app.setBg("green")
# app.setFg("white")
# app.addButtons(["Start"], press)
# app.stopFrame()
#
#
#
#
#
#
# app.go()

# obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#     print("done listening")

# recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     string = r.recognize_google(audio)
#     print("Google Speech Recognition thinks you said " + string)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
#
# tts = gTTS(text=string, lang='en')
# tts.save("hello.mp3")
# playsound('hello.mp3')

# if 'copy' in string:
#     print("found copy")
#     commond="cp"