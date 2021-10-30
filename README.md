# Simple-Speak-Dictionary-Using-Python
We can make our system say out the meaning of the word given as input. which speak the meaning when we want to have the meaning of the particular word.

# Libraries required to be installed using pip command:
1. PyDictionary
2. pyttsx3
3. speech_recognition 

# For Male voice :
  USE : 0
 engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# For Female voice :
  USE : 1
 engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
