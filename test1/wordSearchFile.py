from playsound import playsound
import speech_recognition as sr
import os

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


    print("entering command: " + command)
