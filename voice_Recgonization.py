import subprocess
import time
from tkinter import *
import re
import random
from tkinter import filedialog
from openpyxl import Workbook
import docx
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import random
import os
import getpass
import smtplib
import psutil
import pyautogui

try:
    import pywhatkit as p
except:
    print("NO connection !!! Some functions may not work properly\n This program may terminate in few seconds")
    time.sleep(3)
import pandas as pd
import math
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import LoadUiType
from alexaUI import Ui_alexaUI

# from Tools.scripts import google
hour = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
"""
open new tab = ctrl + t
close tab = ctrl + w
switch another tab on chrome = ctrl + tab
youtube theater mode = t
youtube Full screen mode = f
"""
engine.setProperty('voice', voices[1].id)
cnt1,cnt1whatsapp = 0,0
GMAIL_ID = 'wadkaraditya824@gmail.com'
GMAIL_PSD = '8625994933'
news_api_key = "fcebce30abff45c4bc252594a06b1cb7"
weather_api_key = "710e105ff069d401d319b833c155511f"

df = pd.read_excel("birthday.xlsx")
taskcount, commandcount = 0,0
timer = ""


def target():
    if (not os.path.exists("Task.txt")):
        f = open("Task.txt", "w+")
        f.close()
        speak("No task are assigned sir!!")
        return
    with open("Task.txt", "r") as f:
        task = f.read()
        if os.stat("Task.txt").st_size == 0:
            speak("No task are assigned sir!!")
        else:
            speak("Todays tasks are as follows !!!")
            speak(task)
            speak("these were task assigned !!")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def delete_file(filename):
    file = open(filename, "r+")
    file.truncate(0)
    file.close()
def confirmation(msg):
    f = open("confirm.txt", "w+")
    f.write("Your Message : "+msg)
    f.close()
    webbrowser.open("confirm.txt")
def mail_with_attachment(to, sub, message, name):
    speak("choose file that you want  to send")
    root = Tk()
    root.title("file attachment")
    root.geometry('300x300')
    file_select = filedialog.askopenfilenames()
    aditya = Label(text="Please close this window Manually", font=("verdena", 12))
    aditya.pack(side=TOP, fill=X, padx=0)
    pyautogui.hotkey('alt', 'f4')
    root.mainloop()
    # file_select = input("Write path here : ")
    speak(f"Sending email to {name} within few moments !!")
    msg = MIMEMultipart()
    msg["From"] = "Aditya Wadkar"
    msg["To"] = ",".join(to)
    msg["subject"] = sub
    msg.attach(MIMEText(message, 'plain'))
    speak("Finding and validating attachment !!")
    for filecount in file_select:
        filename = os.path.basename(filecount)  # file select
        attachment = open(filecount, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('content-Disposition', 'attachment; filename = %s' % filename)
        msg.attach(part)
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(GMAIL_ID, GMAIL_PSD)  # login with mail_id and password
        text = msg.as_string()
    speak("attatchment validated Successfully!!Now Uploading attachment and sending email!!This may take few minutes depending upon file size")
    try:
        session.sendmail(GMAIL_ID, to, text)
        speak(f"Email successfully sent!! ")
    except:
        speak("You cannot send application file or exe file through mail!! so mail not sent")
    session.quit()


def sendmail(to, sub, msg, no):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(GMAIL_ID, GMAIL_PSD)
        s.sendmail("Aditya Wadkar", to, f"subject: {sub} \n\n {msg}")
    except Exception as e:
        speak("you have written wrong username or password!!! so ! mail has not sent")
    if to == 'kanikakinger824@gmail.com':
        speak(f"Email sent to your Favorite sister !!")
    else:
        if no == 1:
            speak("Email successfully sent ")

    s.quit()


def validation():
    speak("hello User ")
    speak("To confirm !! you are valid user !write password below")
    password = getpass.getpass("Password :")
    if password == "KaniWal":
        speak("hello Aditya!!!")
        speak("initializing System!!!!!")
        time.sleep(1)
    else:
        speak("Password is incorrect !!please retype it. !This is last chance!!")
        password1 = getpass.getpass("Password :")
        speak("Validating Password .....")
        if password1 == "KaniWal":
            speak("hello Aditya")
        else:
            sendmail("wadkaraditya923@gmail.com", "Alexa Security alert!!!!",
                     "Some malicious person tried to access me.\nPlease Take a look in this matter\nIf it was done by you mistakenly. Ignore This mail\n\nYou received this mail to ensure Security of Application ",
                     0)
            speak("You are not a valid user . closing this application")
            exit()


def find(name):
    cnt = 0
    speak("Searching file in your system!!!This may take few minutes!!")
    speak("Searching in C directory")
    for root, dirs, files in os.walk('C:\\'):
        if name in files:
            cnt = 1
            speak("File found in C Directory!!here's the path of that file!!")
            print(root)
            speak("Searching duplicate copy of file")
    if cnt == 1:
        file_not_found = True
    else:
        file_not_found = False
    if file_not_found == False:
        speak("File not present in C directory Searching in D directory")
        for root, dirs, files in os.walk('D:\\'):
            if name in files:
                cnt = 1
                speak("File found in d Directory!!here's the path of that file")
                print(root)
                speak("Searching duplicate copy of file")
    if cnt == 1:
        file_not_found = True
    else:
        file_not_found = False

    if file_not_found == False:
        speak("File not present in D directory Searching in E directory")
        for root, dirs, files in os.walk('E:\\'):
            if name in files:
                cnt = 1
                speak("File found in E Directory!!here's the path of that file")
                print(root)
                speak("Searching duplicate copy of file")
    if cnt == 0:
        speak("file not present in your system")


def whatsappmsg(self):
    global cnt1whatsapp
    try:
        speak("To whom your want to send message : ")
        self.querry = self.takecommand1().lower()
        n = self.querry
    except Exception as e:
        n = input("enter name : ")
    def message(no):
        try:
            hrs = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute) + 1
            p.sendwhatmsg('+' + no, msg, hrs, min)
        except Exception as e:
            print(e)
            try:
                min = min + 2
                p.sendwhatmsg('+' + no, msg, hrs, min)
            except:
                speak("Cannot send whatsapp message at this moment!!sorry for inconvience!!please try again later" )
                return
    for index, item in df.iterrows():
        if item["name"] == n:
            cnt1whatsapp =1
            ab = str(math.trunc(item["no"]))
    if cnt1whatsapp != 1:
         speak(f"Sorry!! The name {n} is not present in database!! Please Update it")
    try:
        speak(f"what message you would like to give to {n}")
        whatmsg = self.takecommand1()
        confirmation(self.querry)
        time.sleep(1)
        while True:
            speak("have I listen the message correctly ??")
            check = self.takecommand1()
            if "yes" in check or "correctly" in check or "right" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                break
            elif "no" in check or "incorrect" in check or "wrong" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sorry for that!! Please say that once again!!")
                whatmsg = self.takecommand1()
                confirmation(self.querry)
            elif "cancel" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sending mail program Cancelled Successfully!!")
                return
        msg = whatmsg
    except Exception as e:
        msg = input("Enter message : ")
    speak(f"Sending a whatsapp message to {n} within a minute !! Please be Patient")

    try:
        message(ab)
        speak("Please close whatsapp window manually!! And ensure to logout if your are on different system")
    except:
        speak("unable to send message due to no internet connection")



b = 0
def mail(self):
    try:
        mail_id = []
        name = []
        def receipient1():
            global cnt1,b
            speak("To whom you want to send mail : ")
            self.querry = self.takecommand1().lower()
            to = self.querry
            print(to)
            name.append(to)
            for index, item in df.iterrows():
                if item["name"] == to:
                    cnt1 = 1
                    mail_id.append(item['Email'])
            if cnt1 != 1:
                speak(f"Sorry!! The name {name[-1]} is not present in database!!Please update it")
                name.pop()
            cnt1 = 0
            speak("do you wish to add another recipient ? ")
            option = self.takecommand1().lower()
            if "yes" in option or "add" in option:
                receipient1()
            elif "no" in option or "do not" in option:
                return
        receipient1()
        print(name)
        if len(name)==0:
            speak("You have not added any receipent!!please add atleast 1")
            receipient1()

        speak("what subject you want to give")
        self.querry = self.takecommand1().lower()
        subject = self.querry
        confirmation(subject)
        time.sleep(1)
        while True:
            speak("!have I listen the subject correctly ??")
            check = self.takecommand1().lower()
            if "yes" in check or "correctly" in check or "right" in check:
                pyautogui.hotkey("alt","F4")
                delete_file("confirm.txt")
                break
            elif "no" in check or "incorrect" in check or "wrong" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sorry for that!! Please say that once again!!")
                subject = self.takecommand1().lower()
                confirmation(subject)
            elif "cancel" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sending mail program Cancelled Successfully!!")
                return
        sub = subject
        speak("What message you want to convey  : ")
        self.querry = self.takecommand1()
        email_message=self.querry
        confirmation(email_message)
        time.sleep(3)
        while True:
            speak("have I listen the message correctly ??")
            check = self.takecommand1()
            if "yes" in check or "correctly" in check or "right" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                break
            elif "no" in check or "incorrect" in check or "wrong" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sorry for that!! Please say that once again!!")
                email_message = self.takecommand1()
                confirmation(email_message)
            elif "cancel" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sending mail program Cancelled Successfully!!")
                return

        message = email_message
        message = message + "\n\n\n\n---\nThanks And Regards,\nMr. Aditya Anand Wadkar\nMOB NO : 8275693296\nEmail: wadkaraditya824@gmail.com"
        if "attachment" in message:
            mail_with_attachment(mail_id, sub, message, name)
        else:
            speak("Do you wish to send attachment along with this mail")
            self.querry = self.takecommand1().lower()
            if "don not" in self.querry or "no" in self.querry:
                speak(f"Sending email to {name} within few moments !!")
                sendmail(mail_id, sub, message, 1)
            elif "yes" in self.querry or "send attachment" in self.querry or "attachment" in self.querry:
                mail_with_attachment(mail_id, sub, message, name)

    except Exception as e:
        print(e)
        speak("Sorry !! Mic is not accessible!! Please Type all details in command prompt")
        mail_id = []
        name = []

        def receipient():
            global cnt1

            to = input("Write receiver's name : ")
            name.append(to)
            for index, item in df.iterrows():
                if item["name"] == to:
                    cnt1 = 1
                    mail_id.append(item['Email'])
            if cnt1 != 1:
                speak(f"Sorry!! The name {name[-1]} is not present in database!!Please update it")
                name.pop()
            cnt1=0
            option = input("do you wish to add another recipient ?[y/n] : ")
            if "y" in option or "Y" in option:
                receipient()
            elif "n" in option or "N" in option:
                return
        receipient()


        sub = input("Write subject of mail : ")
        message = input("Write message you wish to convey : ")
        message = message + "\n\n\n\n---\nThanks And Regards,\nMr. Aditya Anand Wadkar\nMOB NO : 8275693296\nEmail: wadkaraditya824@gmail.com"
        a = input("Do you wish to send attachment along with this mail[y/n] : ")
        if "y" in a:
            mail_with_attachment(mail_id, sub, message, name)
        else:
            speak(f"Sending email to {name} within few moments !!")
            sendmail(mail_id, sub, message, 1)


def wishMe():
    '''
    Greetings to user
    :return:
    '''
    if hour < 12:
        speak("good Morning")
    elif hour >= 12 and hour < 16:
        speak("good Afternoon")
    elif hour >= 16 and hour < 22:
        speak("good Evening ")
    else:
        speak("Its late night")
    speak(f"Current temperature is {temperature}  and the weather is {weather1}")


def news():
    url = f"http://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}"
    main_page = requests.get(url).json()
    article = main_page["articles"]
    head = []
    for ar in article:
        head.append(ar["description"])
    for i in range(6):
        # a = time.sleep(2)
        print(f"{i + 1} {head[i]} ")
        speak(f"{i + 1} {head[i]} ")
        time.sleep(2)


temperature = ""
weather1 = ""


def weather():
    global temperature, weather1
    url = "http://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=710e105ff069d401d319b833c155511f"
    main_page = requests.get(url).json()
    temp = main_page["main"]['temp']
    weather1 = main_page["weather"][0]['main']
    temperature = str(temp) + " \N{DEGREE SIGN}C"


def terminate(self):
    speak("Thanks for using me.")
    speak(" Would you also like to close or restart your system for better performance ??")
    try:
        self.querry = self.takecommand1().lower()
    except Exception as e:
        self.querry = input("your answer : ")
    if 'no' in self.querry:
        speak("closing Application within few moments")
        startmain.kill()
        exit()
        sys.exit()

    elif 'shutdown' in self.querry or "yes" in self.querry:
        os.system("shutdown /s ")
        speak("Your system will shutdown within a minute ")
        startmain.kill()
        exit()
        sys.exit()

    elif 'restart' in self.querry:
        os.system("shutdown /r ")
        speak("Your system will restart within a minute ")
        startmain.kill()
        exit()
        sys.exit()


city, country = "", ""


def location():
    global city, country
    add = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + add + ".json"
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    city = geo_data['city']
    country = geo_data['country']


def stop_listening(value):
    string1 = value
    try:
        a = int(re.search(r'\d+', string1).group())
    except:
        speak("I cannot do this right now!! sorry for inconvience")
        return
    if "second" in string1:
        speak(f"I will not listen anything for {a} seconds")
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(a)
        speak(f"{a} seconds are completed !!")
    elif "minute" in string1:
        speak(f"I will not listen anything for {a} minutes")
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(60 * a)
        speak(f"{a} minutes are completed !!")
    else:
        speak("sorry!!I cannot stop listening for more than 60 minutes")
    speak("Now I am activated")


def main2(self):
    while True:
    #     try:
    #         self.querry = self.takecommand1()
    #     except:
    #         self.querry = input("Type activate :")
    #     if "wake up" in self.querry or "activate" in self.querry:
    #         speak("I am activated")
    #         self.main()
    #     elif "close" in self.querry or "terminate" in self.querry:
    #         terminate(self)
        import keyboard
        if keyboard.is_pressed('F5') == True:
            speak("I am activated")
            self.main()
        if keyboard.is_pressed('Esc') == True:
            terminate(self)



def basic_commands(self, querry):
    if "how are you" in self.querry:
        speak("I am fine sir!! What about you ??")

    elif "good" in self.querry or "fine" in self.querry:
        speak("Nice to listen that")

    elif "thankyou" in self.querry or "thanks" in self.querry:
        speak("Its my pleasure sir!! I am always available for you !!!!")

    elif "name" in self.querry:
        speak("My name is alexa and I am virtual assistant")

    elif "yourself" in self.querry or "functions" in self.querry or "what can you do" in self.querry:
        speak(" My name is alexa!!! My maker has assemble a great deal of capacities "
              "in me!!I can send emails,!whatsapp messages !! can give climate subtleties,"
              " news refreshes!!,play tunes, can take you to visit through web surfing !! "
              "fetch information about anyone and lots more!! But I am in developing stage!!!"
              "my developers are updating me daily!!!!!")

    elif "born" in self.querry or "birthday" in self.querry or "created" in self.querry:
        speak("I was born on 11 september 2020 as a captone project by my developers")

    elif "i love you" in self.querry:
        speak("Sorry I cannot Love you!!Because I am a just few lines of code! and  not a human being!!!Infact "
              "I suggest you to create your account on any matrimonial Site! so that your can find your life partner!!!")

    else:
        speak("sorrry  I didn't understand that!! ")
    self.main()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        weather()
        location()
        wishMe()
        self.main()

    def takecommand1(self):
        '''
        take user commands(microphone inputs and returns string output)
        :return:
        '''
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Listening...... ")
            speak("Listening......")
            r.pause_threshold = 0.7
            audio = r.listen(source)
        try:

            print("Recognizing....")
            speak("Recognizing....")
            self.querry = r.recognize_google(audio, language='en-in')
            self.querry = self.querry.lower()
            # else:
            #     self.querry = self.takecommand1().lower()
            print(f"user said :{self.querry}\n")
        except Exception as e:
            print(e)
            speak(" I coud not hear that !!!! please type what you want to say!!!")
        return self.querry

    def main(self):
        global taskcount,commandcount
        while True:
            if taskcount == 0:
                try:

                    speak("Sir!!! do you wish to know your Todays task ??")
                    self.querry = self.takecommand1().lower()
                    if "do not" in self.querry:
                        pass
                    elif "yes" in self.querry or "task" in self.querry:
                        target()

                except Exception as e:
                    self.querry = input("do you wish to know your Todays task ?? [y/n]:")
                    if "y" in self.querry:
                        target()
                taskcount = 1
            ####################### Taking User command #########################
            if (commandcount % 2 == 0):
                speak("I am ready for next command")
            else:
                speak("what's my next task ")
            commandcount = commandcount + 1
            try:
                self.querry = self.takecommand1().lower()

            except Exception as e:
                self.querry = input("what can i do for you:")

                ####################### Closing tab #########################

            if "close" in self.querry:
                try:
                    pyautogui.hotkey("alt", "F4")
                except:
                    speak("sorry !! unable to access your keyboard!!!Please close it manually for this time!!")

            ####################### Music #########################
            elif "music" in self.querry or "song" in self.querry:
                try:

                    musicdir = 'C:\\Users\\Admin\\Music'
                    songs = os.listdir(musicdir)
                    speak("playing songs from your music directory")
                    os.startfile(os.path.join(musicdir, songs[random.randint(1, 64)]))

                except Exception as e:
                    speak("which song would you like to listen")
                    try:
                        self.querry = self.takecommand1().lower()
                    except Exception as e:
                        self.querry = input("Enter song name : ")
                    p.playonyt(self.querry)


            ####################### Sending Email #########################

            elif ('send' in self.querry and ('email' in self.querry or 'mail' in self.querry)) or\
                    (('email' in self.querry or 'mail' in self.querry) and'send' in self.querry ):
                try:
                    mail(self)
                except:
                    speak("sorry !!Unable to send Email because of no internet connection")
                # speak("what's my next task ")

            ####################### Sending Whatsapp message #########################

            elif ('send' in self.querry and 'message' in self.querry) or\
                ('message' in self.querry and 'send' in self.querry):
                try:
                    whatsappmsg(self)
                except:
                    speak("sorry !!Unable send message because of no internet connection")
                # speak("I am ready for next command")

            ####################### OPening mail #########################

            elif 'mail' in self.querry or 'mail' in self.querry:
                speak("opening mail")
                webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
                # speak("what's my next task ")

            ####################### OPening Google Photos #########################

            elif 'photos' in self.querry:
                speak("opening google photos")
                webbrowser.open("https://photos.google.com/?tab=mq&pageId=none")
                # speak("I am ready for next command")

            ####################### For Task #########################

            elif ('add' in self.querry and 'task' in self.querry) or\
                    ('add' in self.querry and 'task' in self.querry):
                try:
                    speak("What do you want to add? :")
                    self.querry = self.takecommand1().lower()
                    if (not os.path.exists("Task.txt")):
                        speak("No task are assigned sir!!")
                        with open("Task.txt", "a")as f:
                            f.write(str("\n" + self.querry))
                    else:
                        with open("Task.txt", "a") as f:
                            f.write(str("\n" + self.querry))
                except:
                    task = input("What do you want to add :")
                    if (not os.path.exists("Task.txt")):
                        speak("No task are assigned sir!!")
                        with open("Task.txt", "a")as f:
                            f.write(str("\n" + task))
                    else:
                        with open("Task.txt", "a") as f:
                            f.write(str("\n" + task))
                speak("Task addedd successfully")

            elif "clear" in self.querry and ("schedule" in self.querry or "task" in self.querry):
                delete_file("Task.txt")
                speak("All schedules are cleared ")

            elif 'schedule' in self.querry or 'task' in self.querry:
                target()


            ####################### For Time #########################

            elif 'time' in self.querry:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strtime}")
                # speak("what's my next task ")

            ####################### Getting News update #########################

            elif ('news' in self.querry and 'update' in self.querry)or\
                    ('update' in self.querry and 'news' in self.querry)or\
                    'todays news' in self.querry:
                speak("fetching News!!")
                try:
                    news()
                    speak("These were latest news!!")
                except:
                    speak("sorry !!Unable to fetch news because of no internet connection")
            ####################### Geting Weather Details #######################

            elif 'weather' and "details" in self.querry:
                try:
                    weather()
                except:
                    speak("sorry !!Unable to fetch weather details due to lack internet connection")
                # speak("what's my next task ")

            ####################### Searching A file in system #########################

            elif ('search' in self.querry and 'file' in self.querry) or\
                    ('file' in self.querry and 'search' in self.querry):
                speak("Please type the file name that you want to search along with extension!!")
                try:
                    f=open("search.txt","w+")
                    f.truncate(0)
                    f.close()
                    webbrowser.open("search.txt")
                    s=""
                    def file():
                        global s
                        time.sleep(10)
                        speak("Have you written file name completely!!!")
                        filename_search = self.takecommand1().lower()
                        if "yes" in filename_search or "written" in filename_search or "completely" in filename_search:
                            pyautogui.hotkey("ctrl","s")
                            time.sleep(1)
                            pyautogui.hotkey("alt","F4")
                            f=open("search.txt","r")
                            s=f.read()
                            f.close()
                        else:
                            speak("ok no problem !!! I will ask again after 10 seconds")
                            file()
                    file()
                except Exception as e:
                    print(e)
                    s = input("name: ")
                find(s)

                # speak("I am ready for next command")

            ####################### Opening whatsapp  #########################
            elif 'whatsapp' in self.querry:
                speak("opening whatsapp")
                try:
                    os.startfile("C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
                except:
                    speak("you may need to scan QR code if you have not login before")
                    webbrowser.open("https://web.whatsapp.com/")
                # speak("what's my next task ")
            ####################### OPening Instagram #########################

            elif 'instagram' in self.querry:
                speak("For How much time do you want to use instagram ")
                try:
                    time_limit = self.takecommand1().lower()
                except:
                    time_limit =input("Enter time in minutes or seconds : ")

                webbrowser.open("https://www.instagram.com/")
                speak("opening instagram and ")
                stop_listening(time_limit)
                # speak("I am ready for next command")
            ####################### Searching on web  #########################

            elif 'google' in self.querry or ("search" in self.querry and "google" in self.querry ):
                speak("what do you want to search")
                try:
                    self.querry = self.takecommand1().lower()
                except Exception as e:
                    self.querry = input("what do you want to search:")
                webbrowser.open("https://www.google.com/search?q=" + self.querry)
                speak("These are the results from Google")
                # speak("what's my next task ")
            ####################### Searching videos On Youtube #########################

            elif 'youtube' in self.querry:
                speak("what do you want to watch")
                try:
                    self.querry = self.takecommand1().lower()
                except Exception as e:
                    self.querry = input("what do you want to watch :")
                # webbrowser.open('https://www.youtube.com/results?search_query=' + self.querry)
                p.playonyt(self.querry)
                speak("These are the results from youtube")
                # speak("I am ready for next command")

            #######################  Playing youtube  #########################

            elif 'video' in self.querry:
                self.querry = self.querry.replace("video", "")

                try:
                    p.playonyt(self.querry)
                    speak("These are the results from youtube")
                except:
                    speak("sorry !!Unable to access youtube because of no internet connection")
                # speak("what's my next task ")

            ####################### Opening NotePad #########################

            elif ("open" in self.querry and "notepad" in self.querry) or\
                    ("notepad" in self.querry and "open" in self.querry):
                speak("Opening Notepad")
                try:
                    subprocess.Popen("notepad.exe")
                except:
                    speak("Sorry !! unable to open notepad")
                # speak("I am ready for next command")
            ####################### OPening Calculator #########################

            elif ("open" in self.querry and "calculator" in self.querry) or\
                    ("calculator" in self.querry and "open" in self.querry):
                speak("Opening Calculator")
                try:
                    subprocess.Popen("calc.exe")
                except:
                    speak("Sorry !! unable to open Calculator")
                # speak("what's my next task ")

            ####################### OPENING CMD #########################

            elif "command prompt" in self.querry or "cmd" in self.querry:
                speak("Opening Command Prompt")
                try:
                    os.popen("Start cmd")
                except:
                    speak("Sorry !! unable to open Command prompt")


            ####################### OPening Word #########################

            elif ("open" in self.querry and "word" in self.querry) or\
                    ("word" in self.querry and "open" in self.querry):
                doc = docx.Document()
                speak("what name would you like to give to word document.")
                try:
                    self.querry = self.takecommand1()
                except Exception as e:
                    self.querry = input("enter file name : ")
                doc.save(self.querry + ".docx")
                speak("Opening word document titled as ".format(self.querry))
                os.system("start " + self.querry + ".docx")


            ####################### OPening Excel #########################

            elif ("open" in self.querry and "excel" in self.querry) or\
                    ("excel" in self.querry and "open" in self.querry):
                speak("what name would you like to give to excel document.")
                try:
                    self.querry = self.takecommand1()

                except Exception as e:
                    self.querry = input("enter file name : ")

                x1 = Workbook()
                speak("Opening excel document titled as ".format(self.querry))
                x1.save(self.querry + ".xlsx")
                os.system("start " + self.querry + ".xlsx")



            ####################### Searching in wikipedia #########################

            elif 'wikipedia' in self.querry:
                speak("searching in wikipedia....")
                self.querry = self.querry.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(self.querry, sentences=4)
                    speak("according to wikipedia..")
                    print(results)
                    speak(results)
                    speak("I am ready for next command")
                except Exception as e:
                    speak(
                        f"Page not found because of no internet connection or lack of information about {self.querry}. please try another page  ")


            ####################### Getting information About person #########################

            elif 'who is' in self.querry:
                speak("searching in wikipedia....")
                self.querry = self.querry.replace("who is", "")
                self.querry = self.querry.replace("alexa", "")
                try:
                    results = wikipedia.summary(self.querry, sentences=3)
                    speak("according to wikipedia..")
                    print(results)
                    speak(results)

                except Exception as e:
                    speak(
                        f"Page not found because of no internet connection or lack of information about {self.querry}. please try another page  ")

            ####################### Taking a screenshot #########################

            elif "screenshot" in self.querry:
                try:
                    pyautogui.hotkey('win', 'printscreen')
                except:
                    speak("sorry !! unable to access your keyboard")
                speak("screenshot taken")


            ####################### Switching tab  #########################

            elif "switch screen" in self.querry or "switch" in self.querry:
                try:
                    pyautogui.hotkey("alt", "tab")
                except:
                    speak("sorry !! unable to access your keyboard")

            ####################### Scrolling down #########################

            elif "down" in self.querry:
                try:
                    pyautogui.press("space")
                except:
                    speak("sorry !! unable to access your keyboard")


            ####################### Scrolling Up #########################

            elif "up" in self.querry:
                try:
                    pyautogui.press("up")
                except:
                    speak("sorry !! unable to access your keyboard")



            ####################### find location #########################
            elif ("find" in self.querry and "location" in self.querry) or\
                    ("location" in self.querry and "find" in self.querry):
                speak("what do you want to locate")
                try:
                    self.querry = self.takecommand1().lower()
                except Exception as e:
                    self.querry = input("what do you want to locate :")
                webbrowser.get().open('https://google.nl/maps/place/' + self.querry + "/@amp;")
                time.sleep(2)
                speak(f"here is the location of {self.querry}")

            ####################### sleeping Program #########################

            elif "sleep" in self.querry or "sleeping" in self.querry:
                speak("sleeping mode activated !! You can activate me any time")
                main2(self)

            elif("shut" in self.querry and "mouth" in self.querry):
                speak("husshhhh !! I think  you are having a bad day today?? But you should not "
                      "talk rudely with me !! i am going to sleep now !! Make your mind "
                      "fresh!! and then talk with me ")
                main2(self)

            elif "stop" in self.querry and "application" in self.querry or\
                    "terminate" in self.querry :
                try:
                    terminate(self)
                except:
                    exit()
            ####################### Stop Listening #########################

            elif "stop listening" in self.querry or "do not listen" in self.querry:
                stop_listening(self.querry)


            ####################### If querry doesn't matches any of above conditions #########################

            else:
                basic_commands(self, self.querry)


startmain = MainThread()
thougths = ["Strive for progress, not perfection.",
            "Failure cannot cope with persistence.",
            "Be yourself; everyone else is already taken.",
            "Powerful dreams inspire powerful action",
            "Another sunrise, another new beginning.",
            "Imagination is greater than detail."]


class MainUI(QMainWindow):
    validation()
    def __init__(self):

        super().__init__()
        self.ui = Ui_alexaUI()
        # weather()
        self.ui.setupUi(self)

        self.ui.movie = QtGui.QMovie("uicomponents\\initiating image.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("uicomponents\\Circle2.gif")
        self.ui.mainlabel.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("uicomponents\\tenor.gif")
        self.ui.tenor.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("uicomponents\\hi.gif")
        self.ui.hi.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.textBrowser_4.setText(random.choice(thougths))

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
    startmain.start()  # to start mainthread class

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.TextDate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_1.setText("Time :" + label_time)
        self.ui.textBrowser_2.setText("Temp : " + temperature)
        self.ui.textBrowser_3.setText(str(psutil.virtual_memory().percent) + "% Memory Used")
        self.ui.textBrowser_5.setText("Country : " + country + "\n  City    : " + city)


App = QApplication(sys.argv)
alexa = MainUI()
alexa.show()
sys.exit(App.exec_())
