import speech_recognition as sr
import playsound
from gtts import gTTS
import os
from selenium import webdriver
import wolframalpha


num = 1


def assistant_speaks(output):
    global num
    num += 1
    print ("PerSon : ", output)

    toSpeak = gTTS (text=output, lang='en', slow=False
    file = (str (num) + ".mp3")
    toSpeak.save (file)
    playsound.playsound (file, True)
    os.remove (file)


def get_audio():
    rObject = sr.Recognizer ()
    audio = ''

    with sr.Microphone () as source:
        with sr.Microphone () as source:
            print ("Speak...")
            audio = rObject.listen (source, phrase_time_limit=5)
        print ("Stop.")

        try:

            text = rObject.recognize_google (audio, language='en-US')
            print ("You : ", text)
            return text

        except:

            assistant_speaks ("Could not understand your audio, PLease try again !")
            return 0
if __name__ == "__main__":
    assistant_speaks ("What's your name, Human?")
    name = 'Human'
    name = get_audio ()
    assistant_speaks ("Hello, " + name + '.')

    while (1):

        assistant_speaks ("What can i do for you?")
        text = get_audio ().lower ()

        if text == 0:
            continue

        if "exit" in str (text) or "bye" in str (text) or "sleep" in str (text):
            assistant_speaks ("Ok bye, " + name + '.')
            break
            process_text (text)
def open_application(input):
    if "chrome" in input:
        assistant_speaks ("Google Chrome")
        os.startfile ('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks ("Opening Mozilla Firefox")
        os.startfile ('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        assistant_speaks ("Opening Microsoft Word")
        os.startfile ('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        assistant_speaks ("Opening Microsoft Excel")
        os.startfile ('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
    else:
        assistant_speaks ("Application not available")
        return

