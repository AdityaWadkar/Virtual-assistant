import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import random
import getpass
import smtplib
import pyautogui
import pywhatkit as p
import pandas as pd
import math
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter.filedialog import *
from tkinter import ttk
import pathlib


hour = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)

GMAIL_ID = 'Your Email Address'
GMAIL_PSD = 'Your Password'
news_api_key="Your API Key"
weather_api_key ="Your API key"

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
        speak(" I coudn't hear that !!!! please type what you want to say!!!")
        # querry = takecommand().lower()
    return querry

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def mail_with_attachment(to, sub ,message,name):
    root = Tk()
    root.title("file attachment")
    root.geometry('300x300')
    file_select = askopenfilename()
    aditya = Label(text="Please close this window Manually", font=("verdena", 12))
    aditya.pack(side=TOP, fill=X, padx=0)
    pyautogui.hotkey('alt','f4')
    pyautogui.hotkey('win','down')
    root.mainloop()
    # file_select = input("Write path here : ")
    speak(f"Sending email to {name} within few moments !!")
    msg = MIMEMultipart()
    msg["From"] = GMAIL_ID
    msg["To"] = to
    msg["subject"] = sub
    msg.attach(MIMEText(message, 'plain'))
    filename = os.path.basename(file_select)
    attachment = open(file_select, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', 'attachment; filename = %s' % filename)
    msg.attach(part)
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(GMAIL_ID, GMAIL_PSD)  # login with mail_id and password
    text = msg.as_string()
    speak("Uploading Attachment and then sending mail")
    session.sendmail(GMAIL_ID, to, text)
    session.quit()
    speak('Mail Sent successfully')

def sendmail(to, sub, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(GMAIL_ID, GMAIL_PSD)
        s.sendmail(GMAIL_ID, to, f"subject: {sub} \n\n {msg}")
    except Exception as e:
        speak("you have written wrong username or password!!! so ! mail has not sent  ")
    # speak("If you're sending this mail for first time !! then a "
    #       "security alert will come on your mail and!! mail would not be sent !! To avoid that !"
    #       "allow less secure app to acces your mail using this link")
    # print("https://myaccount.google.com/lesssecureapps")
    s.quit()
    speak("Email successfully sent ")


def validation():
    speak("hello User ")
    wishMe()
    speak("To confirm !you are valid user !write password below")
    password = getpass.getpass("Password :")
    if password == "Your_password":
        speak("hello Aditya")
        speak("My name is lisa .! How can i help you")
    else:
        speak("Password is incorrect please retype it. !This is last chance!!")
        password1 = getpass.getpass("Password :")
        if password1 == "Your_password":
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
    try:
        speak("To whom your want to send message : ")
        querry = takecommand().lower()
        n = querry
    except Exception as e:
        n = input("enter name : ")
    cnt = 0
    def message(no):
        try:
            hrs = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute) + 1
            p.sendwhatmsg('+' + no, msg, hrs, min)
        except:
            min = min + 2
            p.sendwhatmsg('+' + no, msg, hrs, min)

    for index, item in df.iterrows():
        if item["name"] == n:
            cnt = 1
            try:
                querry = takecommand().lower()
                msg = querry
            except Exception as e:
                msg = input("enter msg : ")
            speak(f"Sending a whatsapp message to {n} within a minute !! Please be Patient")
            ab = str(math.trunc(item["no"]))
            message(ab)
            speak("Please close whatsapp window manually!! And ensure to logout if your are on different system")
    if cnt != 1:
        speak(f"Sorry!! The name {n} is not present in database!! Please Update it")

def mail():
    cnt1 = 0
    try:
     speak("To whom you want to send mail : ")
     querry = takecommand().lower()
     to = querry
     for index, item in df.iterrows():
         if item["name"] == to:
             cnt1 = 1
             speak("what subject you want to give")
             querry = takecommand().lower()
             sub = querry
             speak("What message you want to convey  : ")
             querry = takecommand().lower()
             message = querry
             mail_id = item['Email']
             speak("Do you wish to send attachment along with this mail")
             querry = takecommand().lower()
             if "yes" in querry:
                  mail_with_attachment(mail_id, sub, message,to)
             else:
                 speak(f"Sending email to {to} within few moments !!")
                 sendmail(mail_id, sub, message)
     if cnt1 != 1:
         speak(f"Sorry!! The name {to} is not present in database")

    except Exception as e:
        speak("Please fill following details to send mail")
        to = input("Write receiver's name : ")
        name = to
        for index, item in df.iterrows():
            if item["name"] == to:
                cnt1 = 1
                sub = input("Write subject of mail : ")
                message = input("Write message you wish to convey : ")
                mail_id = item['Email']
                a=input("Do you wish to send attachment along with this mail[y/n] : ")
                if "y" in a:
                    mail_with_attachment(mail_id, sub, message,name)
                else:
                    speak(f"Sending email to {to} within few moments !!")
                    sendmail(mail_id, sub, message)
        if cnt1 != 1:
            speak(f"Sorry!! The name {to} is not present in database!!Please update it")

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
def news():
    url=f"http://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}"
    main_page =requests.get(url).json()
    article=main_page["articles"]
    head=[]
    for ar in article:
        head.append(ar["description"])
    for i in range(6):
        print(head[i])
        speak(head[i])
        time.sleep(1)

def weather():
    url="http://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=710e105ff069d401d319b833c155511f"
    main_page=requests.get(url).json()
    temp=main_page["main"]['temp']
    weather=main_page["weather"][0]['main']
    speak(f"Today's temperature is {temp} degree celsius and the weather will be {weather}")




if __name__ == '__main__':
    df = pd.read_excel("C:\\Users\\Admin\\PycharmProjects\\Mini_Assistant\\birthday.xlsx")
    # validation()
    wishMe()
    weather()
    num = 0
    hault = 0
    while hault is 0:
        while hault is 0:
            if num >= 1:
                speak("At your service sir ")
            try:
                querry = takecommand().lower()
                num += 1
            except Exception as e:
                querry = input("what can i do for you:")
                num += 1
            # logic for executing tasks
            # music
            if "music" in querry:
               try:
                    speak("playing songs from your music directory")
                    musicdir = 'C:\\Users\\Admin\\Music'
                    songs = os.listdir(musicdir)
                    os.startfile(os.path.join(musicdir, songs[random.randint(1, 64)]))
               except Exception as e:
                    # song = querry.replace('music', '')
                    song = 'dhavni bhanushali'
                    speak("playing your Favorite song from youtube")
                    p.playonyt(song)
            elif 'change' in querry:
                speak("playing next song from your music directory")
                musicdir = 'C:\\Users\\Admin\\Music'
                songs = os.listdir(musicdir)
                os.startfile(os.path.join(musicdir, songs[random.randint(1, 64)]))

            elif 'send' and 'email' in querry:
                mail()
            elif 'send' and 'message' in querry:
                whatsappmsg()
            elif 'mail' in querry:
                speak("opening mail")
                webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

            elif 'photos' in querry:
                speak("opening google photos")
                webbrowser.open("https://photos.google.com/?tab=mq&pageId=none")

            # time

            elif 'time' in querry:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strtime}")
            #news update
            elif 'news' and 'update' in querry:
                speak("Todays news updates are!!")
                news()
             #weather update
            elif 'weather' and "details" in querry:
                weather()
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



            # chrome

            elif 'google' in querry:
                speak("what do you want to search")
                try:
                    querry = takecommand().lower()
                except Exception as e:
                    querry = input("what do you want to search:")
                webbrowser.open("https://www.google.com/search?q=" + querry)
                speak("These are the results from Google")

            # youtube

            elif 'youtube' in querry:
                speak("what do you want to watch")
                try:
                    querry = takecommand().lower()
                except Exception as e:
                    querry = input("what do you want to watch :")
                webbrowser.open('https://www.youtube.com/results?search_query=' + querry)
                speak("These are the results from youtube")


            # System close

            elif 'close' in querry:
                speak("Thanks for using me.")
                speak(" Would you also like to close or restart your system for better performance ??")
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
                querry = querry.replace("video", "")
                p.playonyt(querry)
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
                querry = querry.replace("who is","")
                try:
                    results = wikipedia.summary(querry,sentences=3)
                    speak("according to wikipedia..")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Page not found. please try another page  ")
            elif "screenshot" in querry:
                pyautogui.hotkey('win', 'printscreen')
                speak("screenshot taken")
            elif "switch tab" or "switch window" in querry:
                pyautogui.hotkey('alt','tab')

            elif "none" in querry:
                time.sleep(5)
                querry = takecommand().lower()

            elif len(querry) > 5:
                webbrowser.open("https://www.google.com/search?q=" + querry)
                speak(f"sorrry  I didn't understand !! but These are the Results from Google")
            hault=1

        try:
            while True:
                speak("speak jarvis to activate me!!")
                querry = takecommand().lower()
                if 'jarvis' in querry:
                    break
        except Exception as e:
            querry = input("Type jarvis for next command : ")
        if 'jarvis' in querry:
            hault =0
