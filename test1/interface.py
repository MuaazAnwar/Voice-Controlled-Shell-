# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from playsound import playsound


#import png_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 252)
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
        self.textBrowser.setGeometry(QtCore.QRect(120, 20, 391, 221))
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
        ##muaaz
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 91, 23))
        self.pushButton.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"padding: 2px;\n"
"background-color:rgb(170, 85, 255)")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.pushButton_2.released.connect(press)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Voice Controlled Shell"))
        self.textBrowser.setPlaceholderText(_translate("Dialog", "Press Mic Button To Record"))
        #muaaz
        self.pushButton.setText(_translate("Dialog", "Break!"))
    def changeText(self, str):
        self.textBrowser.setPlaceholderText(str)
        print("I am Called")

def fixString(str):
#    for i in range(0, len(str)):
#        print(str[i]+".")

    a = str
    a = a.replace(" / ", "/")
    a = a.replace("/ ", "/")
    a = a.replace(" /", "/")
    a = a.replace(" dot " , ".")
    a = a.replace("desktop", "Desktop")
    a = a.replace("my documents", "MyDocuments")
    a = a.replace("my document", "MyDocuments")

    return a
def fixName(str):
#    for i in range(0, len(str)):
#        print(str[i]+".")

    temp = str
    temp = temp.replace(" ", "")


    return temp

def show_ext():

    ext = [".txt", ".mp3", ".mp4", ".png", ".wav", ".sh", ".docx"]
    print(ext)
    ui.textBrowser.append(".txt .mp3 .mp4 .png .wav .sh .docx")
	
    #for i in range(0,len(ext)):

     #   print(i + ": " + ext[i])
        #ui.textBrowser.append(i + ": " + ext[i] )

    playsound("selectect.mp3")

    d=getInput()

    d=int(d)

    return ext[d]

def getInput():
    r = sr.Recognizer()
    while True:  # keep trying if expections occur, correctly chalne pr break hoga
        with sr.Microphone() as source:
            ui.textBrowser.append("Listening...")
            print("listening...")
            audio = r.listen(source)
            ui.textBrowser.append("Done Listening")
            print("done listening")


        # recognize speech using Google Speech Recognition

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            string = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + string)

            return string

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            playsound("error.mp3")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            playsound("error.mp3")


def wordSearch(str):
    command = "INVALID"
    print("searching for words...")
    if 'copy file' in str or 'copy' in str:
        print("found copy")

        print("Enter source path")
        playsound("sourcepath.mp3")
        source = getInput()
        source = fixString(source)

        print("Enter dest path")  # enterdest.mp3
        playsound("destpath.mp3")
        dest = getInput()
        dest = fixString(dest)

        command = "cp " + source + " " + dest

    elif 'date' in str:
        command = "date"
        #os.system("date") #commented out when testing on windows
    elif ('list' in str):
        command = "ls"
    elif "move" in str:
        print("Enter source path")  # sourcepath.mp3
        playsound("sourcepath.mp3")
        source = getInput()
        source = fixString(source)

        print("Enter dest path")  # enterdest.mp3
        playsound("destpath.mp3")
        dest = getInput()
        dest = fixString(dest)

        command = "mv " + source + " " + dest
    elif "change directory" in str:
        if "home" in str:
            command = "cd ~"
        else:
            ui.textBrowser.append("Enter directory")
            playsound("entrdir.mp3")

            dir = getInput()
            dir=fixString()
            command = "cd " + dir
    elif "copy folder" in str:
        playsound("sourcepath.mp3")
        s = getInput()
        s = fixString(s)

        playsound("destpath")
        d = getInput()
        d= fixString(d)
        command = "cp -r " + s + " " + d
    elif "kernel version" in str:
        command = "uname -r"
    elif "exit" in str:
        command = "quit()"
    elif "clear" in str:
        command = "clear"
#    elif "find all text files" in str:
#        os.system("find *.txt")
    elif "create file" in str:
        ui.textBrowser.append("Enter name")
        playsound("name.mp3")
        n = getInput()
        n=fixName(n)
        ui.textBrowser.append("Select extension")
        t = show_ext()

        command = "touch " + n + t
    elif "create directory" in str:
        ui.textBrowser.append("Enter name")
        playsound("name.mp3")
        n = getInput()
        n = fixName(n)
        command =  "mkdir " + n
    elif "delete file" in str:
        ui.textBrowser.append("Enter name")
        playsound("name.mp3")
        n = getInput()
        n = fixName(n)
        ui.textBrowser.append("Select extension")
        t = show_ext()

        c = n + "." + t
        command = "rm " + c
    elif "delete folder" in str:
        ui.textBrowser.append("Enter name")
        playsound("name.mp3")
        n = getInput()
        n = fixName(n)
        command = "rmdir " + n
    elif "shutdown" in str:
        command = "shutdown now"
    elif "restart" in str:
        command = "reboot"
    elif "current directory" in str:
        command = "pwd"
    elif "network status" in str:
        command = "ifconfig -a"
    elif "running processes" in str:
        command = "ps"
    elif "all processes" in str:
        command =  "ps -A"
    elif "disk usage" in str:
        command = "df"
    elif "file usage" in str:
        command = "du"
    elif "open browser" in str:
        command = "firefox&"
    elif "change access" in str:
        playsound("name.mp3")
        n = getInput()
        n = fixName(n)

        ui.textBrowser.append("Select extension")
        t = show_ext()
        t = fixString(t)
        n = n + "." + t
        playsound("perm.mp3")

        str = getInput()
        if "execute" in str:
            command = "chmod +x " + n
        elif "write" in str:
            command = "chmod +w " + n
        elif "read" in str:
            command = "chmod +r " + n
        else:
            command = "chmod +xwr " + n


    print("entering command: " + command)
    os.system(command)

def press():

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


