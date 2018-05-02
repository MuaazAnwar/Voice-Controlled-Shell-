# Voice Controlled Shell

It is a Python script. 

## Implementation

Voice Controlled Shell is implemented using python script with following
libraries:
* speech_recognition
* PyQt5
* os
* playsound
* sys 

Voice is recognized through Google API and different mp3 files are played to ask user for further details of commands (if required). UI part of Voice Controlled Shell is designed with QT designer and converted to python using pyuic5.  

## How to use

### Ubuntu (tested working)

0. Set up git
* sudo apt install git
* git config --global user.name "user_name"
* git config --global user.email "email_id"

1. Clone repository
* git clone https://github.com/MuaazAnwar/Voice-Controlled-Shell-.git

2. Install Packages:
* sudo apt install python3-pip
* pip3 install SpeechRecognition
* sudo apt-get install python3-pyqt5
* pip3 install playsound
* **pyaudio**:
* sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
* sudo apt-get install ffmpeg libav-tools
* pip3 install pyaudio

3. Run:
* python3 /test1/interface.py

## Examples

-1. Create test file on desktop: touch file.txt. 
0. Create test destination on desktop: mkdir folder

1. Click the micorphone button

2. Say: "Copy File"

3. Say: "Desktop slash file

4. Say corresponding number for .txt extension

5. Say: Desktop slash folder

## Limitations

### Acceptable Commands
* Copy
* Move
* List
* Change directory
* Copy folder
* Kernel version
* Exit
* Clear
* Create file
* Create directory
* Delete file
* Delete folder
* Shutdown
* Restart
* Current directory
* Network status
* Running Processes
* All processes
* Disk usage
* File usage
* Open browser
* Change access

### Other
* Keywords are searched for in spoken text rather than processing natural language.
* Commands with parameters (ex: cp source destination) are accepted in pieces.
* Program must be triggered by clicking on the micorphone button (for every command)
* Number of extensions is limited and can be selected seperately by voice.
