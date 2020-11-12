import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import getpass
import smtplib
import pywhatkit as p
import pandas as pd
import math
# from Tools.scripts import google
hour = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendmail(to, sub, msg):
    print(F"sending email to {to} ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(GMAIL_ID, GMAIL_PSD)
        s.sendmail(GMAIL_ID, to, f"subject: {sub} \n\n {msg}")
    except Exception as e:
        speak("you have written wrong username or password!!! so ! mail has not sent  ")
    speak("If you're sending this mail for first time , then a "
          "security alert will come on your mail and mail would not sent . To avoid that "
          "allow less secure app to acces your mail using this link")
    print("https://myaccount.google.com/lesssecureapps")
    s.quit()


def validation():
    speak("hello User ")
    wishMe()
    speak("To confirm !you are valid user !write password below")
    password = getpass.getpass("Password :")
    if password == "KaniWal":
        speak("hello Aditya")
        speak("My name is lisa .! How can i help you")
    else:
        speak("Password is incorrect please retype it. !This is last chance!!")
        password1 = getpass.getpass("Password :")
        if password1 == "KaniWal":
            speak("hello Aditya")
        else:
            speak("You are not a valid user . closing this application")
            exit()

def find(name):
    cnt = 0
    speak("Searching file in your system!!!This may take few minutes!! Please have Paitence")
    speak("Searching in C directory")
    for root, dirs, files in os.walk('C:\\'):
        if name in files:
            print(root)
            cnt = 1
            speak("File found in C Directory")
    if cnt == 1:
        file_not_found = True
    else:
        file_not_found = False
        # os.startfile(root)STE Micro project TEST Cases
    if file_not_found == False:
        speak("File not present in C directory Searching in D directory")
        for root, dirs, files in os.walk('D:\\'):
            if name in files:
                print(root)
                cnt = 1
                speak("File found in d Directory")

    if cnt == 1:
        file_not_found = True
    else:
        file_not_found = False

    if file_not_found == False:
        speak("File not present in D directory Searching in E directory")
        for root, dirs, files in os.walk('E:\\'):
            if name in files:
                print(root)
                cnt = 1
                speak("File found in E Directory")
    if cnt == 0:
        speak("file not present in your system")

def whatsappmsg():
    speak("Enter name of person to whom you want to send message")
    n = input("Enter name : ")
    msg = input("Enter msg : ")
    hrs = int(datetime.datetime.now().hour)
    min =int(datetime.datetime.now().minute)
    min = min + 1
    cnt = 0
    df = pd.read_excel("C:\\Users\\Admin\\PycharmProjects\\Mini_Assistant\\birthday.xlsx")

    def message(no, hrs, min):
        try:
            p.sendwhatmsg('+' + no, msg, hrs, min)
        except:
            min = min + 1
            p.sendwhatmsg('+' + no, msg, hrs, min)

    for index, item in df.iterrows():
        if item["name"] == n:
            cnt = 1
            speak(f"Sending a whatsapp message to {n}")
            ab = str(math.trunc(item["no"]))
            message(ab, hrs, min)
            speak("Please close whatsapp window manually!!")
    if cnt != 1:
        speak("Sorry!! The name is not present in database")


def wishMe():
    '''
    Greetings to user
    :return:
    '''
    if hour <= 12:
        speak("good Morning")
    elif hour > 12 and hour <= 16:
        speak("good Afternoon")
    elif hour >= 16 and hour <= 21:
        speak("good Evening ")
    else:
        speak("Its late night")


def takecommand():
    '''
    take user commands(microphone inputs and returns string output)
    :return:
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        querry = r.recognize_google(audio, language='en-in')
        print(f"user said :{querry}\n")

    except Exception as e:
        print(e)
        print(" say that Again please")
        return "none"
    return querry


if __name__ == '__main__':
    # validation()
    wishMe()
    num = 0

    while True:
        if num >= 1:
            speak("what's my next task ")
        try:
            querry = takecommand().lower()
            num += 1
        except Exception as e:
            querry = input("what can i do for you:")
            num += 1
        # logic for executing tasks
        # music
        if "music" in querry:
            speak("playing songs from your music directory")
            musicdir = 'C:\\Users\\Admin\\Music'
            songs = os.listdir(musicdir)
            os.startfile(os.path.join(musicdir, songs[random.randint(1, 64)]))
        elif 'change' in querry:
            speak("playing next song from your music directory")
            musicdir = 'C:\\Users\\Admin\\Music'
            songs = os.listdir(musicdir)
            os.startfile(os.path.join(musicdir, songs[random.randint(1, 64)]))

        elif 'send'and 'email' in querry:
            speak("Please fill following details to send mail")
            GMAIL_ID = input("Enter your gmail_id: ")
            GMAIL_PSD = getpass.getpass("Password :")
            to = input("To whom you want to send mail : ")
            sub = input("subject : ")
            msg = input("What message you want to convey  : ")
            sendmail(to, sub, msg)
        elif 'send' and 'message' in querry:
            whatsappmsg()

        elif 'open mail' in querry:
            speak("opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'photos' in querry:
            speak("opening google photos")
            webbrowser.open("https://photos.google.com/?tab=mq&pageId=none")

        # time

        elif 'time' in querry:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")

        # Search file option
        elif 'search' in querry:
            speak("Please type the file name that you want to search along with extension!!")
            s = input("name: ")
            find(s)

        # whatsapp

        elif 'whatsapp' in querry:
            speak("opening whatsapp")
            os.startfile("C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")


        # instagram

        elif 'instagram' in querry:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")

        # linux

        elif 'linux' in querry:
            speak("opening second operating system ")
            os.startfile("D:\\Virtual Box\\VirtualBox.exe")


        # chrome

        elif 'google' in querry:
            speak("opening the best search engine of world")
            os.startfile("www.google.com")

        # youtube

        elif 'youtube' in querry:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")


        # System close

        elif 'close' in querry:
            speak("Thanks for using me.")
            speak(" Would you also like to close your system ??")
            try:
                querry = takecommand().lower()
            except Exception as e:
                querry = input("your answer : ")
            if 'no' in querry:
                speak("closing Application")
                exit()
                os.system("TASKKILL /F /IM pycharm64.exe")
            elif 'shutdown' or "yes" in querry:
                os.system("shutdown /s ")
                speak("Your system will shutdown within a minute ")
                exit()
            elif 'restart' in querry:
                os.system("shutdown /r ")
                speak("Your system will restart within a minute ")
                exit()

        # Accessing chrome using information
        elif 'video' in querry:
            webbrowser.open('https://www.youtube.com/results?search_query=' + querry)
            speak("These are the results from youtube")
        # wikipedia

        elif 'wikipedia'   in querry:
            speak("searching in wikipedia....")
            querry = querry.replace("wikipedia", "")
            try:
                results = wikipedia.summary(querry, sentences=3)
                speak("according to wikipedia..")
                print(results)
                speak(results)
            except Exception as e:
                speak("Page not found. please try another page  ")

        elif 'who' in querry :
            speak("searching in wikipedia....")
            querry = querry.replace("wikipedia","")
            try:
                results = wikipedia.summary(querry,sentences=3)
                speak("according to wikipedia..")
                print(results)
                speak(results)
            except Exception as e:
                speak("Page not found. please try another page  ")

        elif "none" in querry:
            querry = takecommand().lower()

        elif len(querry) >= 5:
            webbrowser.open("https://www.google.com/search?q=" + querry)
            speak(f"These are the Results from Google")
        else:
            speak("The task name should be atleast 5 character")
