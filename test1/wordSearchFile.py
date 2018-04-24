from playsound import playsound
import speech_recognition as sr
import os
import sys
#obj=sys.path.insert(0,"../interface.py")



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

def show_ext():

    ext = ["txt", "mp3", "mp4", "png", "wav", "sh", "docx"]

    for i in range(0,len(ext)):

        print("%d:"+ext[i]+"\n",i)

    playsound("select extension")

    d=getInput()

    d=int(d)

    return ext[d]

def getInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Say something!")
        audio = r.listen(source)
        print("done listening")

    # recognize speech using Google Speech Recognition
    while True: #keep trying if expections occur, correctly chalne pr break hoga
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
            playsound("error.mp3")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            playsound("error.mp3")

from interface import Ui_Dialog
from interface import getUI
# import interface as obj
#
#
uz=Ui_Dialog
uz=getUI()
def wordSearch(str):
    command = "INVALID"
    print("searching for words...")
    if 'copy' in str or 'Copy' in str:
        print("found copy")

        print("Enter source path") #sourcepath.mp3
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
    elif "list all files" in str:
        os.system("ls -a")
    elif "move file" in str:
        playsound("sourcepath.mp3")
        s = getInput()
        playsound("tell the type of file")
        t = show_ext()
        t.replace(" ", "")
        s = s + "." + t
        playsound("tell destination")
        d = getInput()
        d=fixString()
        os.system("mv " + s + " " + d)
    elif "change directory" in str:
        if "to home" in str:
            os.system("cd ..")
        else:
            playsound("tell me the name of the directory")
            dir = getInput()
            dir=fixString()
            os.system("cd " + dir)
    elif "copy file" in str:
        playsound("tell source")
        s = getInput()
        playsound("tell the type of file")
        t = show_ext()
        t=fixString()
        s = s + "." + t
        playsound("tell destination")
        d = getInput()
        os.system("cp " + s + " " + d)
    elif "copy folder" in str:
        playsound("tell source")
        s = getInput()
        playsound("tell the type of file")
        t = getInput()
        t=fixString()
        s = s + t
        playsound("tell destination")
        d = getInput()
        os.system("cp -r " + s + " " + d)
    elif "what is the kernel version" in str:
        os.system("uname -r")
    elif "exit" in str:
        os.system("quit()")
    elif "clear" in str:
        os.system("clear")
    elif "find all text files" in str:
        os.system("find *.txt")
    elif "create text file" in str:
        playsound("tell the name of file")
        t = getInput()
        t = t + ".txt"
        os.system("touch " + t)
    elif "create directory" in str:
        playsound("tell the name of the directory")
        t = getInput()
        os.system("mkdir " + t)
    elif "delete file" in str:
        playsound("tell the name of file")
        n = getInput()
        n=fixString()
        playsound("tell the type of file")
        t = show_ext()
        c = n + "." + t
        os.system("rm " + c)
    elif "delete folder" in str:
        playsound("enter the name of the folder")
        n = getInput()
        n=fixString()
        os.system("rmdir " + n)
    elif "shutdown" in str:
        os.system("shutdown now")
    elif "restart" in str:
        os.system("shutdown -f now")
    elif "head" in str:
        playsound("tell the name of file")
        n = getInput()
        n=fixString()
        playsound("tell the type of file")
        t = show_ext()
        t=fixString()
        c = n + "." + t
        os.system("head " + c)
    elif "tail" in str:
        playsound("tell the name of file")
        n = getInput()
        n=fixString()
        playsound("tell the type of file")
        t = show_ext()
        t=fixString()
        c = n + "." + t
        os.system("tail " + c)
    elif "current directory" in str:
        os.system("pwd")
    elif "network status" in str:
        os.system("ifconfig -a")
    elif "running processes" in str:
        os.system("ps")
    elif "all processes" in str:
        os.system("ps -A")
    elif "disk usage" in str:
        os.system("df")
    elif "file usage" in str:
        os.system("du")
    elif "login as root user" in str:
        os.system("sudo -i")
    elif "open browser" in str:
        os.system("firefox&")
    elif "give access to file" in str:
        playsound("Tell the name of file")
        n = getInput()
        n=fixString(n)
        playsound("Tell the type of file")
        ty = show_ext()
        ty=fixString()
        n = n + "." + ty
        playsound("Tell the type of access")
        t = getInput()
        if "execute" in str:
            os.system("chmod +x " + n)
        elif "write" in str:
            os.system("chmod +w " + n)
        elif "read" in str:
            os.system("chmod +r " + n)
        else:
            os.system("chmod +xwr " + n)


    print("entering command: " + command)
