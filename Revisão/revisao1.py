import pyttsx3

robo = pyttsx3.init()
robo.setProperty('rate', 150)
robo.setProperty('volume', 1.0)
robo.say("Good morning, my friend. Let's go!")
robo.runAndWait()