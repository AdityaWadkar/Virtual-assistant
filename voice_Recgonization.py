import subprocess
import shutil
import time
from tkinter import *
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
import smtplib
import psutil
import pyautogui
import keyboard
import cv2
try:
    import pywhatkit as p
except:
    # print("NO connection !!! Some functions may not work properly\n This program may terminate in few seconds")
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
cnt1, cnt1whatsapp = 0,0
GMAIL_ID = 'YOUR_EMAIL_ADDRESS'
GMAIL_PSD = 'YOUR_PASSWORD'
news_api_key = "YOUR API KEY"
weather_api_key = "YOUR API KEY"
order=""
df = pd.read_excel("birthday.xlsx")
attempts,sleepcount,taskcount, commandcount,splitcommand,speak_frequency=0,0,0,0,0,0
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
    global speak_frequency
    speak_frequency=1
    # print(speak_frequency)
    engine.say(audio)
    engine.runAndWait()
    speak_frequency = 0


def delete_file(filename):
    file = open(filename, "r+")
    file.truncate(0)
    file.close()
def confirmation(msg):
    f = open("confirm.txt", "w+")
    f.write("Your Message : "+msg)
    f.close()
    webbrowser.open("confirm.txt")

def pick_aatachment():
    speak("choose file that you want  to send")
    root = Tk()
    root.title("file attachment")
    root.geometry('300x300')
    file_select = filedialog.askopenfilenames()
    root.destroy()
    root.mainloop()
    return file_select

def invalid_login_email(to,sub,message,file_name):
    msg = MIMEMultipart()
    msg["From"] = "Aditya Wadkar"
    msg["To"] = to
    msg["subject"] = sub
    msg.attach(MIMEText(message, 'plain'))

    # filename = os.path.basename(file_name)  # file select
    attachment = open(file_name, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', f'attachment; filename ={file_name}')
    msg.attach(part)
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(GMAIL_ID, GMAIL_PSD)  # login with mail_id and password
    text = msg.as_string()
    session.sendmail(GMAIL_ID, to, text)
    session.quit()

def mail_with_attachment(to, sub, message, name, attach):
    file_select = attach
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
        if no==1:
            speak("you have written wrong username or password!!! so ! mail has not sent")
        else:
            if no == 1:
                speak("Email successfully sent ")
            speak(f"Email successfully sent!! ")
    s.quit()

def offline_mode(type=None):
    root = Tk()
    root.title("command")
    root.geometry("400x160")
    root.resizable(False, False)
    bg = PhotoImage(file="uicomponents//command.png")
    def disable_event1():
        pass
    def next_order():
        global order
        order = txtfield.get()
        txtfield.delete(0, END)
        root.destroy()

    if type=="task":
        command_label='write task'
        command_button='Add Task'
    elif type == 'search':
        command_label = 'Write File Name'
        command_button = 'Search File'
    elif type == 'time_limit  :':
        command_label = 'Time Limit'
        command_button = 'Set Time Limit'
    elif type == 'google_search':
        command_label = 'Search Title  :'
        command_button = 'Search'
    elif type == 'youtube_search':
        command_label = 'watch Title  :'
        command_button = 'Search File'
    elif type == 'location':
        command_label = 'Write Location :'
        command_button = 'Locate'
    elif type == 'terminate':
        command_label = 'Your Answer :'
        command_button = 'Perform Task'
    else:
        command_label = 'write command:'
        command_button = 'Perform Task'
    # Show image using label
    root.iconphoto(False, bg)
    label1 = Label(root, image=bg).pack()
    heading1 = Label(label1, text=command_label, font="verdena 13 bold")
    heading1.place(x=10, y=30)
    txtfield = Entry(label1, font="Helvitica 14")
    txtfield.place(x=150, y=30, width=240, height=25)
    button1 = Button(label1, text=command_button, command=next_order)

    button1.place(x=195, y=80)
    try:
        root.protocol("WM_DELETE_WINDOW", disable_event1)
        root.mainloop()
    except:
        pass
    return order

def face_authentication():
    global converted_image
    cam = cv2.VideoCapture(0)  # used to create video which is used to capture images

    cascadePath = "uicomponents//haarcascade_frontalface_default.xml"
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    speak(" !! performing face authentication!!please look at camera ")
    recognizer.read('uicomponents//trained_data.yml')  # loaded trained model
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes fonts size

    # id = 5  # number of persons your want to recognize
    # names = ['', 'Aditya']

    cam.set(3, 640)
    cam.set(4, 480)
    #
    # # define min window size to be recognize as a face
    minW = 0.1 * cam.get(3)
    maxW = 0.1 * cam.get(4)
    valid_face = 0
    invalid_face = 0
    while True:
            ret, img = cam.read()  # read the frames using above created objects

            # cv2.imshow('camera', img)
            try:
                converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converts image to black and white
            except:
                pass
            faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minW)),
            )
            cv2.imshow("camera", img)
            # time.sleep(1)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])
                # check if accuracy is less than 100 ==> "0" is perfect match
                # print(accuracy)
                if (accuracy >= 45 and accuracy<=60):
                    valid_face += 1
                    if valid_face >=10:
                            # print(f"valid face : {valid_face}")
                        # cv2.imshow('frame', converted_image)
                        # if cv2.waitKey(1) == ord('q'):
                        #     break
                            speak("face recognization successfull!!hello aditya!!!initializing System!!!!!")
                            cam.release()
                            cv2.destroyAllWindows()
                            pyautogui.press('esc')
                            return

                else:
                        invalid_face += 1
                        # print(f"invalid face : {invalid_face}")
                        if invalid_face >=100:
                            mal_user = "mal_user.png"
                            cv2.imwrite(mal_user, img)
                            shutil.move('mal_user.png', 'uicomponents/')
                            close_program("uicomponents/mal_user.png")
                            sys.exit()
                break
                # cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 0, 255), 2)
                # cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break
    cam.release()
    cv2.destroyAllWindows()

def close_program(mal):
    invalid_login_email("wadkaraditya923@gmail.com", "Aditi Security alert!!!!",
             f"An Unauthorized person tried to access me at {datetime.datetime.now().strftime('%H:%M:%S')}\nThe pic of that user is attached below.\nPlease Take a look in this matter\nIf it was done by you mistakenly. please Ignore This mail !!\n\nYou received this mail to ensure Security of Application ",
             mal)
    os.remove("uicomponents/mal_user.png")
    speak("You are not a valid user . closing this application")

def validation():
    global click_event
    root = Tk()
    root.geometry("540x360")
    root.resizable(False,False)
    bg = PhotoImage(file="uicomponents//login.png")
    speak("!! To confirm !! you are valid user !write secret key Here")

    def disable_event():
        button2.place(x=395, y=300)
    def close_win():
        root.destroy()
        sys.exit()

    def authenticate():
        global  attempts
        password = txtfield.get()
        txtfield.delete(0,END)
        if password == "KaniWal":
            speak("hello Aditya!!!")
            speak("initializing System!!!!!")
            root.destroy()
            # pyautogui.hotkey('alt','F4')
        else:
            if attempts < 1:
                speak("Password is incorrect !!please retype it. !This is last chance!!")
            attempts =attempts +1
            if attempts ==2:
                cam = cv2.VideoCapture(0)
                while True:
                    ret, img = cam.read()  # read the frames using above created objects
                    mal_user = "mal_user.png"
                    cv2.imwrite(mal_user, img)
                    shutil.move('mal_user.png', 'uicomponents/')
                    close_program("uicomponents/mal_user.png")
                    break
                cam.release()
                cv2.destroyAllWindows()
                sys.exit()


    # Show image using label
    root.title("Authentication System")
    p1 = PhotoImage(file='uicomponents\\login.png')
    root.iconphoto(False,p1)
    label1 = Label(root, image=bg).pack()
    heading = Label(label1, text="Smart Login System", font="verdena 17 bold")
    heading.place(x=270, y=30)
    heading1 = Label(label1, text="Password:", font="verdena 13 bold")
    heading1.place(x=270, y=170)
    txtfield = Entry(label1, show="*")
    txtfield.place(x=370, y=170)
    label2=Label(root, image=bg).pack()
    button1 = Button(label1, text="Activate", command=authenticate)
    button1.place(x=395, y=200)

    button2 = Button(label2, text="close program", command=close_win)
    button2.pack_forget()
    try:
        root.protocol("WM_DELETE_WINDOW", disable_event)

        root.mainloop()

    except Exception as e:
        # print(e)
        pass

def find(name):
    f = open("filepath.txt", "a")
    f.truncate(0)
    cnt = 0
    speak("Searching file in your system!!!This may take few minutes!!")
    speak("Till that time you enjoy some youtube videos")
    p.playonyt("https://www.youtube.com/watch?v=VU07jbfe9dU&list=WL&index=2&t=182s")
    for root, dirs, files in os.walk('C:\\'):
        if name in files:
            cnt = 1
            f.write(root+"\n")
    if cnt == 1:
        file_not_found = True
    else:
        file_not_found = False
    if file_not_found == False:
        for root, dirs, files in os.walk('D:\\'):
            if name in files:
                cnt = 1
                f.write(root + "\n")
    if cnt == 1:
        file_not_found = True
    else:
        file_not_found = False
    if file_not_found == False:
        speak("File not present in D directory Searching in E directory")
        for root, dirs, files in os.walk('E:\\'):
            if name in files:
                cnt = 1
                f.write(root + "\n")
    f.close()
    if cnt == 0:
        speak("sorry !! file is not present in your system")
    else:
        speak("File found in system !!here's the path of that file")
        webbrowser.open("filepath.txt")

def database_fetch(n):
    global cnt1whatsapp,order
    for index, item in df.iterrows():
        if item["name"] == n:
            cnt1whatsapp = 1
            order="Name present in database"
    if cnt1whatsapp != 1:
         order="Name not present in database!! Please Update it"
    cnt1whatsapp =0
    return order


def message(no,msg,n):
    import pywhatkit as p
    speak(f"sending whatsapp message to {n} within a minute !!! Please be patient ")
    try:
        hrs = int(datetime.datetime.now().hour)
        min = int(datetime.datetime.now().minute) + 1
        p.sendwhatmsg('+' + no, msg, hrs, min)
    except Exception as e:
        # print(e)
        try:
            min = min + 2
            p.sendwhatmsg('+' + no, msg, hrs, min)
        except:
            speak("Cannot send whatsapp message at this moment!!sorry for inconvience!!please try again later")
            return

def whatsappmsg(self):
    global cnt1whatsapp
    ab=0
    try:
        speak("To whom your want to send message : ")
        querry = self.takecommand1().lower()
        n = querry
        for index, item in df.iterrows():
            if item["name"] == n:
                cnt1whatsapp =1
                ab = str(math.trunc(item["no"]))
        if cnt1whatsapp != 1:
             speak(f"Sorry!! The name {n} is not present in database!! Please Update it")
             return
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
                    speak("Sending whatsapp message program Cancelled Successfully!!")
                    return
        msg = whatmsg
        message(ab,msg,n)
    except Exception as e:
        # print(e)
        root = Tk()
        root.title("Whatsapp Messenger")
        root.geometry("400x160")
        root.resizable(False, False)
        bg = PhotoImage(file="uicomponents//whatsapp.png")

        def collect_data_whatsapp():
            n=txtfield_whatsapp.get()
            msg=txtfield1_whatsapp.get()
            for index, item in df.iterrows():
                if item["name"] == n:
                    cnt1whatsapp = 1
                    ab = str(math.trunc(item["no"]))
            if cnt1whatsapp != 1:
                speak(f"Sorry!! The name {n} is not present in database!! Please Update it")
            root.destroy()
            message(ab,msg,n)
        def name_verify():
            global order
            order = txtfield_whatsapp.get()
            name_verification = database_fetch(order)
            name_result.config(text=name_verification)

        # Show image using label
        root.iconphoto(False, bg)
        label1 = Label(root, image=bg).pack()

        name_result = Label(label1, font="verdena 10 bold")
        name_result.place(x=70, y=9)

        heading1 = Label(label1, text="Receiver's Name:", font="verdena 13 bold")
        heading1.place(x=10, y=40)
        txtfield_whatsapp = Entry(label1, font="Helvitica 10")
        txtfield_whatsapp.place(x=155, y=40, width=140, height=22)
        verify = Button(label1, text="Verify Name", command=name_verify)
        verify.place(x=315, y=40)

        heading2 = Label(label1, text="Message :", font="verdena 13 bold")
        heading2.place(x=30, y=80)
        txtfield1_whatsapp = Entry(label1, font="Helvitica 10")
        txtfield1_whatsapp.place(x=155, y=80, width=230, height=22)

        button1 = Button(label1, text="Send Message", command=collect_data_whatsapp)
        button1.place(x=145, y=120)

        try:
            # root.protocol("WM_DELETE_WINDOW", disable_event)
            root.mainloop()
        except:
            pass

def mail(self):
    try:
        mail_id = []
        name = []
        def receipient1():
            global cnt1
            speak("To whom you want to send mail : ")
            self.querry = self.takecommand1().lower()
            to = self.querry
            # print(to)
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
            if "no" in option or "do not" in option:
                return
            elif "yes" in option or "add" in option:
                receipient1()

        receipient1()
        # print(name)
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
            elif "cancel" in check or "stop" in check:
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
            elif "cancel" in check or "stop" in check:
                pyautogui.hotkey("alt", "F4")
                delete_file("confirm.txt")
                speak("Sending mail program Cancelled Successfully!!")
                return

        message = email_message
        message = message + "\n\n\n\n---\nThanks And Regards,\nMr. Aditya Anand Wadkar\nMOB NO : 8275693296\nEmail: wadkaraditya824@gmail.com"
        if "attachment" in message:
            attach = pick_aatachment()
            mail_with_attachment(mail_id, sub, message, name, attach)
        else:
            speak("Do you wish to send attachment along with this mail")
            self.querry = self.takecommand1().lower()
            if "don not" in self.querry or "no" in self.querry:
                speak(f"Sending email to {name} within few moments !!")
                sendmail(mail_id, sub, message, 1)
            elif "yes" in self.querry or "send attachment" in self.querry or "attachment" in self.querry:
                attach = pick_aatachment()
                mail_with_attachment(mail_id, sub, message, name, attach)

    except Exception as e:
        root = Tk()
        root.title("Email")
        root.geometry("400x250")
        root.resizable(False, False)
        bg = PhotoImage(file="uicomponents//email.png")

        def collect_data(option):
            global cnt1
            mail_id = []
            name = []
            to = txtfield.get()
            sub = txtfield1.get()
            message = txtfield2.get()
            name.append(to)
            for index, item in df.iterrows():
                if item["name"] == to:
                    cnt1 = 1
                    mail_id.append(item['Email'])
            if cnt1 != 1:
                speak(f"Sorry!! The name {name[-1]} is not present in database!!Please update it")
                name.pop()
            cnt1 = 0
            message = message + "\n\n\n\n---\nThanks And Regards,\nMr. Aditya Anand Wadkar\nMOB NO : 8275693296\nEmail: wadkaraditya824@gmail.com"
            root.destroy()
            if option == "mail":
                speak(f"Sending email to {name} within few moments !!")
                sendmail(mail_id, sub, message, 1)
            else:
                attach = pick_aatachment()
                mail_with_attachment(mail_id, sub, message, name, attach)

        def name_verify():
            global order
            order = txtfield.get()
            name_verification = database_fetch(order)
            name_result.config(text=name_verification)

        root.iconphoto(False, bg)
        label1 = Label(root, image=bg).pack()

        name_result = Label(label1, font="verdena 10 bold")
        name_result.place(x=70, y=9)

        heading1 = Label(label1, text="Receiver's name:", font="verdena 13 bold")
        heading1.place(x=10, y=40)
        txtfield = Entry(label1, font="Helvitica 10")
        txtfield.place(x=155, y=40, width=140, height=22)
        verify = Button(label1, text="Verify Name", command=name_verify)
        verify.place(x=315, y=40)

        heading2 = Label(label1, text="Subject :", font="verdena 13 bold")
        heading2.place(x=35, y=80)
        txtfield1 = Entry(label1, font="Helvitica 10")
        txtfield1.place(x=155, y=80, width=230, height=22)

        heading3 = Label(label1, text="Message :", font="verdena 13 bold")
        heading3.place(x=32, y=120)
        txtfield2 = Entry(label1, font="Helvitica 10")
        txtfield2.place(x=155, y=120, width=230, height=22)

        heading4 = Label(label1, text="Attachment (if any) ", font="verdena 13 bold")
        heading4.place(x=10, y=160)
        attach = Button(label1, text="Attach File", command=lambda: collect_data("attachment"))
        attach.place(x=195, y=160)

        button1 = Button(label1, text="Send Email", command=lambda: collect_data("mail"))
        button1.place(x=145, y=210)

        try:
            root.mainloop()
        except:
            pass


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
        # print(f"{i + 1} {head[i]} ")
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
        self.querry = offline_mode('terminate')
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


def stop_listening(value,target):
    string1 = value
    try:
        a = int(re.search(r'\d+', string1).group())
    except:
        speak("I cannot do this right now!! sorry for inconvience")
        return
    if "second" in string1:
        if target =="stop":
            speak(f"I will not listen anything for {a} seconds")
        else:
            speak("setting timer for {a} seconds")

        time.sleep(a)
        speak(f"{a} seconds are completed !!")
    elif "minute" in string1:
        if target == "stop":
            speak(f"I will not listen anything for {a} minutes")
        else:
            speak("setting timer for {a} minutes")

        time.sleep(60 * a)
        if a == 1:
            speak(f"{a} minute is completed !!")
        else:
            speak(f"{a} minutes are completed !!")
    else:
        speak("sorry!!I cannot stop listening for more than 60 minutes")
    speak("Now I am activated as your time is up !!!")


def main2(self):
    global sleepcount
    sleepcount=1
    while True:
        if keyboard.is_pressed('pause') == True:
            sleepcount = 0
            speak("I am activated")
            self.main()
        if keyboard.is_pressed('Esc') == True:
            terminate(self)

def wikipedia_result(str,no):
    main_word,last = str.split("is",1)
    try:
        speak("searching on internet...")
        results = wikipedia.summary(last, sentences=no)
        speak("according to information on internet...")
        # print(results)
        speak(results)

    except Exception as e:
        speak(f"sorry !! I am unable to access information about {last}!due to shortage of information or lack of internet connection!! please try again later  ")


def basic_commands(self, querry):
    global commandcount
    if "how are you" in self.querry:
        speak("I am fine sir!! What about you ??")

    elif "good" in self.querry or "fine" in self.querry:
        speak("Nice to listen that")

    elif "thankyou" in self.querry or "thanks" in self.querry:
        speak("Its my pleasure sir!! I am always available for you !!!!")

    elif "name" in self.querry:
        speak("My name is aditi and I am virtual assistant")

    elif "yourself" in self.querry or "functions" in self.querry or "what can you do" in self.querry:
        speak(" My name is aditi!!! My maker has assemble a great deal of capacities "
              "in me!!I can send emails,!whatsapp messages !! can give climate subtleties,"
              " news refreshes!!,play tunes, can take you to visit through web surfing !! "
              "fetch information about anyone and lots more!! But I am in developing stage!!!"
              "my developers are updating me daily!!!!!")

    elif "born" in self.querry or "birthday" in self.querry :
        speak("I was born on 11 september 2020 as a captone project by my developers")

    elif "i love you" in self.querry:
        speak("I love you to !!!!!!! but as a friend !!")
    elif "marry me" in self.querry:
        if (commandcount % 2 == 0):
            speak("Sorry I cannot marry you!!Because I am a just few lines of code! and  not a girl!!!Infact "
                  "I suggest you to create your account on any matrimonial Site! so that your can find your life partner!!")
            webbrowser.open("https://www.shaadi.com/")
            time.sleep(3)
        else:
            speak("sorry !! I am already in relationship with electricity")
        speak("here's a sample matrimonial site for you !!!but to be very honest!!I don't think that any girl "
              "would marry you after viewing your profile as no one will like your face")

    elif "my" in self.querry and "girlfriend" in self.querry:
        speak("sorry !! I can't be your girfriend as I am already engaged with your machine !!")
    else:
        speak("sorrry  I didn't understand that!! ")
    self.main()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def kill(self):
        pass
    def run(self):
        # weather()
        location()
        # wishMe()
        self.main()

    def takecommand1(self):
        '''
        take user commands(microphone inputs and returns string output)
        :return:
        '''
        r = sr.Recognizer()
        with sr.Microphone() as source:

            # print("Listening...... ")
            speak("Listening......")
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try:

            # print("Recognizing....")
            speak("Recognizing....")
            self.querry = r.recognize_google(audio, language='en-in')
            self.querry = self.querry.lower()
            # else:
            #     self.querry = self.takecommand1().lower()
            # print(f"user said :{self.querry}\n")
        except Exception as e:
            # print(e)
            speak(" I coud not hear that !!!! please say that once again !!")
        return self.querry

    def main(self):
        global taskcount,commandcount,splitcommand

        while True:
            if taskcount == 0:
                wishMe()
                try:
                    speak("Sir!!! do you wish to know your Todays task ??")
                    self.querry = self.takecommand1().lower()
                    if "do not" in self.querry or 'no' in self.querry:
                        pass
                    elif "yes" in self.querry or "task" in self.querry:
                        target()

                except Exception as e:
                    self.querry = offline_mode()
                    if "yes" in self.querry:
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
                self.querry = offline_mode()

            if "and" in self.querry:
                splitcommand=1
                s1, s2 = self.querry.split("and", 1)
                self.querry=s1
            if splitcommand==1:
                self.querry=s2
                splitcommand=0
            mood=random.randint(0,10)


                ####################### Closing tab #########################

            if "close" in self.querry:
                if mood == 6:
                    speak("sir !!! You are becoming too lazy now a days !! just because of me !!"
                          "so close this window on your own !! give me some other task ")
                    time.sleep(2)
                else:
                    try:
                        pyautogui.hotkey("alt", "F4")
                    except:
                        speak("sorry !! unable to access your keyboard!!!Please close it manually for this time!!")

            ####################### Music #########################
            elif "play" in self.querry and  ("music" in self.querry or "song" in self.querry or "songs" in self.querry):
                if mood == 6:
                    speak("sir !!! it will be better if you play song on your own!! give me some other task !! ")
                    time.sleep(1)
                else:
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
                if mood==6:
                    speak("sir !!! i  have no interest to send email to anyone write now !!! do it on your own !!!! give me some other task !! ")
                    time.sleep(1)
                else:
                    try:
                        mail(self)
                    except:
                        speak("sorry !!Unable to send Email because of no internet connection")
                # speak("what's my next task ")

              ####################### Sending Whatsapp message #########################

            elif ('send' in self.querry and 'message' in self.querry) or\
                ('message' in self.querry and 'send' in self.querry):
                if mood ==6:
                    speak("Sir !! do it on your own !!! I have no interest in viewing your personal chats !!! Give some other task to me ")
                    time.sleep(2)
                else:
                    try:
                        whatsappmsg(self)
                    except:
                        speak("sorry !!Unable send message because of no internet connection")
                # speak("I am ready for next command")

            ####################### OPening mail #########################

            elif 'mail' in self.querry or 'email' in self.querry:
                if mood==6:
                    speak("Sorry !! I am off duty right now !! do it on your own ! or Try again later !!! ")
                    time.sleep(3)
                else:
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
                    ('add' in self.querry and 'schedule' in self.querry):
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
                    task = offline_mode('task')
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

            ####################### setting timer #########################

            elif "set" and "timer" in self.querry:
                stop_listening(self.querry, "timer")

            ####################### For Time #########################

            elif ('time' in self.querry and 'what' in self.querry)or\
                 ('what' in self.querry and 'time' in self.querry):
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

            elif ('weather' and "details" in self.querry) or \
                    ('news' in self.querry and 'update' in self.querry):
                try:
                    weather()
                    speak(f"Current temperature is {temperature}  and the weather is {weather1}")
                except:
                    speak("sorry !!Unable to fetch weather details due to lack internet connection")
                # speak("what's my next task ")


            ####################### Searching A file in system #########################

            elif ('search' in self.querry and 'file' in self.querry) or\
                    ('file' in self.querry and 'search' in self.querry):
                speak("Please type the file name that you want to search along with extension!!")
                s = offline_mode('search')
                find(s)



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
                    time_limit =offline_mode('time_limit')

                webbrowser.open("https://www.instagram.com/")
                speak("opening instagram ")
                stop_listening(time_limit,"stop")
                # speak("I am ready for next command")
            ####################### Searching on web  #########################

            elif 'google' in self.querry or ("search" in self.querry and "google" in self.querry ):
                speak("what do you want to search")
                try:
                    self.querry = self.takecommand1().lower()
                except Exception as e:
                    self.querry = offline_mode('google_search')
                webbrowser.open("https://www.google.com/search?q=" + self.querry)
                speak("These are the results from Google")
                # speak("what's my next task ")
            ####################### Searching videos On Youtube #########################

            elif 'youtube' in self.querry:
                speak("what do you want to watch")
                try:
                    self.querry = self.takecommand1().lower()
                except Exception as e:
                    self.querry = offline_mode('youtube_search')
                # webbrowser.open('https://www.youtube.com/results?search_query=' + self.querry)
                p.playonyt(self.querry)
                speak("These are the results from youtube")
                # speak("I am ready for next command")

                ####################### Scrolling down #########################

            elif "down" in self.querry or ("pause" in self.querry and "video" in self.querry):
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

            elif ("open" in self.querry and "command prompt" in self.querry) or\
                    ("open" in self.querry and "cmd" in self.querry):
                speak("opening Command Prompt")
                try:
                    os.system('start cmd')
                except:
                    speak("Sorry !! unable to open Command prompt")


            ####################### OPening Word #########################

            elif ("open" in self.querry and "word" in self.querry) or\
                    ("word" in self.querry and "open" in self.querry):
                doc = docx.Document()
                # speak("what name would you like to give to word document.")
                # try:
                #     self.querry = self.takecommand1()
                # except Exception as e:
                #     self.querry = input("enter file name : ")
                doc.save("Untitled.docx")
                speak("Opening word document")
                os.system("start Untitled.docx")


            ####################### OPening Excel #########################

            elif ("open" in self.querry and "excel" in self.querry) or\
                    ("excel" in self.querry and "open" in self.querry):
                # speak("what name would you like to give to excel document.")
                # try:
                #     self.querry = self.takecommand1()
                #
                # except Exception as e:
                #     self.querry = input("enter file name : ")
                x1 = Workbook()
                speak("Opening excel document ")
                x1.save("Untitled.xlsx")
                os.system("start Untitled.xlsx")


            ####################### Getting information About person #########################

            elif 'who is' in self.querry:
                wikipedia_result(self.querry,3)
            elif 'what is' in self.querry:
                wikipedia_result(self.querry,1)

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


            ####################### find location #########################
            elif ("find" in self.querry and "location" in self.querry) or\
                    ("location" in self.querry and "find" in self.querry):
                speak("what do you want to locate")
                try:
                    self.querry = self.takecommand1().lower()
                except Exception as e:
                    self.querry = offline_mode('location')
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
                except Exception as e:
                    # print(e)
                    exit()
            ####################### Stop Listening #########################

            elif "stop listening" in self.querry or "do not listen" in self.querry:
                stop_listening(self.querry,"stop")

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
    try:
        speak("Hello User")
        face_authentication()
    except Exception as e:
        print(e)
        speak("Sorry !! unable to perform face recognization due to some technical fault!!!!so")
        validation()
    global sleepcount,speak_frequency
    def __init__(self):
        super().__init__()
        self.ui = Ui_alexaUI()

        weather()
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

        self.ui.audio = QtGui.QMovie("uicomponents\\audio.gif")
        self.ui.frequency.setMovie(self.ui.audio)
        self.ui.audio.start()


        self.ui.textBrowser_4.setText(random.choice(thougths))
        self.lblHidden = False
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
        self.ui.textBrowser_5.setText("Country : " + country + "\nCity : " + city)
        if sleepcount == 1:
            self.ui.textBrowser_6.setText("Sleeping Mode is Activated")
        else:
            self.ui.textBrowser_6.setText("")
        if speak_frequency == 1:
            self.ui.frequency.setVisible(True)
        else:
            self.ui.frequency.setVisible(False)

App = QApplication(sys.argv)
alexa = MainUI()
alexa.show()
sys.exit(App.exec_())


