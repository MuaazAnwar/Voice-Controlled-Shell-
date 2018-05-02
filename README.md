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
