# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWidgets
from wordSearchFile import wordSearch
from playsound import playsound

#import png_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 230)
        Dialog.setStyleSheet("Background-color:rgb(0, 170, 255)")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 85, 180))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: black;\n"
"padding: 2px;\n"
"background-color:rgb(255, 255, 127)")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("original.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(120, 20, 391, 190))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color:rgb(172, 172, 172);\n"
"\n"
"font: 75 10pt \"Courier New\";\n"
"color: rgb(250, 250, 250);\n"
"https://thesmithfam.org/blog/2009/09/10/qt-stylesheets-tutorial/;\n"
"")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.pushButton_2.released.connect(press)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voice Controlled Shell"))
        self.textBrowser.setPlaceholderText(_translate("Dialog", "Press Mic Button To Record"))

    def changeText(self, str):
        self.textBrowser.setPlaceholderText(str)
        print("I am Called")





def press(firstPress=True):
    if firstPress==True:
        ui.textBrowser.append("Enter command")
        app.processEvents()
        playsound("command.mp3")
        print("Enter command")
        #ui.changeText("Enter command")
        app.processEvents()

    # obtain audio from the microphone
    r = sr.Recognizer()
    while True: #keep trying if expections occur, correctly chalne pr break hoga
        with sr.Microphone() as source:
            print("Listening...")
            ui.textBrowser.append("Listening...")
            app.processEvents()
            audio = r.listen(source)
            print("Done Listening. Processing...")
            ui.textBrowser.append("Done Listening. Processing...")
            app.processEvents()

    # recognize speech using Google Speech Recognition

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            string = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + string)

            if firstPress==False:
                return str

            wordSearch(string)
            break

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            ui.textBrowser.append("An error occured.")
            app.processEvents()
            playsound("error.mp3")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            ui.textBrowser.append("An error occured.")
            app.processEvents()
            playsound("error.mp3")

print("starting app")
import sys

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
print("ending app")

def getUI():
    return ui

