import os

import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound

microfone = sr.Microphone()
reconhecedor = sr.Recognizer()
with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    audio = gTTS("Deseja ouvir uma música?", lang = "pt")
    audio.save('msg2.mp3')
    playsound('msg2.mp3')
    print("Deseja ouvir uma música?")
    audio = reconhecedor.listen(mic)
    print("Reconhecendo...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print(texto)
    lista = ['OK', 'PODE SER', 'SIM', 'TUDO BEM', 'QUERO']
    if texto.upper() in lista:
        audio = gTTS("Ok, abrindo música", lang='pt')
        audio.save('msg3.mp3')
        playsound('msg3.mp3')
        print("Ok, abrindo a música...")
        os.system('musica.mp3')
    else:
        audio = gTTS("Tudo bem, até logo!", lang='pt')
        audio.save('msg4.mp3')
        playsound('msg4.mp3')
        print("Tudo bem, até logo!")


