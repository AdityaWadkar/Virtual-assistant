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
try:
    import pyautogui
except:
    print("NO connection !!! Some functions may not work properly")
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
    speak("choose file that you want  to send")
    root = Tk()
    root.title("file attachment")
    root.geometry('300x300')
    file_select = filedialog.askopenfilenames()
    aditya = Label(text="Please close this window Manually", font=("verdena", 12))
    aditya.pack(side=TOP, fill=X, padx=0)
    pyautogui.hotkey('alt','f4')
    root.mainloop()
    # file_select = input("Write path here : ")
    speak(f"Sending email to {name} within few moments !!")
    msg = MIMEMultipart()
    msg["From"] = GMAIL_ID
    msg["To"] = ",".join(to)
    msg["subject"] = sub
    msg.attach(MIMEText(message, 'plain'))
    speak("Uploading Attachment!!")
    for filecount in file_select:
        filename = os.path.basename(filecount)#file select
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
    speak("Attachment Uploaded Successfully !!! sending email")
    try:
        session.sendmail(GMAIL_ID, to, text)
        speak(f"Email successfully sent!! ")
    except:
        speak("You cannot send application file or exe file through mail!! so mail not sent")
    session.quit()


def sendmail(to, sub, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(GMAIL_ID, GMAIL_PSD)
        s.sendmail(GMAIL_ID, to, f"subject: {sub} \n\n {msg}")
    except Exception as e:
        speak("you have written wrong username or password!!! so ! mail has not sent")
    if to =='kanikakinger824@gmail.com':
        speak(f"Email sent to your Favorite sister !!")
    else:
        speak("Email successfully sent ")
    s.quit()

def validation():
    speak("hello User ")
    wishMe()
    speak("To confirm !! you are valid user !write password below")
    password = getpass.getpass("Password :")
    if password == "KaniWal":
        speak("hello Aditya!!!")
        speak("initializing System!!!!!")
        time.sleep(1)
    else:
        speak("Password is incorrect !!please retype it. !This is last chance!!")
        password1 = getpass.getpass("Password :")
        if password1 == "KaniWal":
            speak("hello Aditya")
        else:
            speak("You are not a valid user . closing this application")
            exit()

def find(name):
    cnt = 0
    speak("Searching file in your system!!!This may take few minutes!!")
    speak("Searching in C directory")
    for root, dirs, files in os.walk('C:\\'):
        if name in files:
            print(root)
            cnt = 1
            speak("File found in C Directory!!here's the path of that file!!")
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
                speak("File found in d Directory!!here's the path of that file")

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
    if cnt == 0:
        speak("file not present in your system")

def whatsappmsg():
    try:
        speak("To whom your want to send message : ")
        querry = takecommand1().lower()
        while True:
            speak("!have I listen the name correctly ??")
            check = takecommand1()
            if "yes" in check or "correct" in check or "right" in check:
                break
            elif "no" in check or "incorrect" in check or "wrong" in check:
                speak("Sorry for that!! Please say that once again!!")
                querry = takecommand1()
            elif "restart" in check:
                speak("restarting application")
                pyautogui.hotkey("ctrl", "F5")
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
                speak(f"what message you would like to give to {n}")
                querry = takecommand1()
                while True:
                    speak("have I listen the message correctly ??")
                    check = takecommand1()
                    if "yes" in check or "correct" in check or "right" in check:
                        break
                    elif "no" in check or "incorrect" in check or "wrong" in check:
                        speak("Sorry for that!! Please say that once again!!")
                        querry = takecommand1()
                    elif "restart" in check:
                        speak("restarting application")
                        pyautogui.hotkey("ctrl", "F5")
                msg = querry
            except Exception as e:
                msg = input("Enter message : ")
            speak(f"Sending a whatsapp message to {n} within a minute !! Please be Patient")
            ab = str(math.trunc(item["no"]))
            try:
                message(ab)
                speak("Please close whatsapp window manually!! And ensure to logout if your are on different system")
            except:
                speak("unable to send message due to no internet connection")

    if cnt != 1:
        speak(f"Sorry!! The name {n} is not present in database!! Please Update it")


def mail():
    global cnt1
    try:
     mail_id = []
     name = []
     def receipient1():
         global cnt1
         speak("To whom you want to send mail : ")
         querry = takecommand1().lower()
         to = querry
         name.append(to)
         b = 0
         for a in name:
             for index, item in df.iterrows():
                 if item["name"] == name[b]:
                     cnt1 = 1
                     mail_id.append(item['Email'])
             if cnt1 != 1:
                 speak(f"Sorry!! The name {name} is not present in database!!Please update it")
                 name.pop()
             b = b + 1
     receipient1()
     while True:
         speak("do you wish to add another recipient ? ")
         option =takecommand1()
         if "yes" in option or "add" in option:
             receipient1()
         elif "no" in option or "do not" in option:
             break

     speak("what subject you want to give")
     querry = takecommand1().lower()
     while True:
         speak("!have I listen the subject correctly ??")
         check = takecommand1()
         if "yes" in check or "correct" in check or "right" in check:
             break
         elif "no" in check or "incorrect" in check or "wrong" in check:
             speak("Sorry for that!! Please say that once again!!")
             querry = takecommand1()
         elif "restart" in check:
             speak("restarting application")
             pyautogui.hotkey("ctrl", "F5")
     sub = querry
     speak("What message you want to convey  : ")
     querry = takecommand1()
     while True:
         speak("!have I listen the message correctly ??")
         check = takecommand1()
         if "yes" in check or "correct" in check or "right" in check:
             break
         elif "no" in check or "incorrect" in check or "wrong" in check:
             speak("Sorry for that!! Please say that once again!!")
             querry = takecommand1()
         elif "restart" in check:
             speak("restarting application")
             pyautogui.hotkey("ctrl", "F5")

     message = querry
     message = message + "\n\n\n\n---\nThanks And Regards,\nMr. Aditya Anand Wadkar\nMOB NO : 8275693296\nEmail: wadkaraditya824@gmail.com"
     if "attachment" in message:
         mail_with_attachment(mail_id, sub, message, name)
     else:
         speak("Do you wish to send attachment along with this mail")
         querry = takecommand1().lower()
         if "yes" in querry or "send attachment" in querry:
             mail_with_attachment(mail_id, sub, message, name)
         else:
             speak(f"Sending email to {name} within few moments !!")
             sendmail(mail_id, sub, message)

    except Exception as e:
        mail_id = []
        name = []
        def receipient():
            global cnt1
            b = 0
            to = input("Write receiver's name : ")
            name.append(to)
            for a in name:
                for index, item in df.iterrows():
                    if item["name"] == name[b]:
                        cnt1 = 1
                        mail_id.append(item['Email'])
                if cnt1 != 1:
                    speak(f"Sorry!! The name {name} is not present in database!!Please update it")
                    name.pop()
                b = b + 1
        receipient()
        while True:
            option=input("do you wish to add another recipient ?[y/n] : ")
            if "y" in option or "Y" in option :
                receipient()
            elif "n" in option or "N" in option:
                break
        sub = input("Write subject of mail : ")
        message = input("Write message you wish to convey : ")
        message = message + "\n\n\n\n---\nThanks And Regards,\nMr. Aditya Anand Wadkar\nMOB NO : 8275693296\nEmail: wadkaraditya824@gmail.com"
        a = input("Do you wish to send attachment along with this mail[y/n] : ")
        if "y" in a:
            mail_with_attachment(mail_id, sub, message, name)
        else:
            speak(f"Sending email to {name} within few moments !!")
            sendmail(mail_id, sub, message)


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
def news():
    url=f"http://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}"
    main_page =requests.get(url).json()
    article=main_page["articles"]
    head=[]
    for ar in article:
        head.append(ar["description"])
    for i in range(6):
        # a = time.sleep(2)
        print(f"{i+1} {head[i]} ")
        speak(f"{i+1} {head[i]} ")
        time.sleep(2)

def weather():
    url="http://api.openweathermap.org/data/2.5/weather?q=Pune&units=metric&appid=710e105ff069d401d319b833c155511f"
    main_page=requests.get(url).json()
    temp=main_page["main"]['temp']
    weather=main_page["weather"][0]['main']
    speak(f"Current temperature is {temp} degree celsius and the weather is {weather}")
def exit1():
    exit()
def terminate():
    speak("Thanks for using me.")
    speak(" Would you also like to close or restart your system for better performance ??")
    try:
        querry = takecommand1().lower()
    except Exception as e:
        querry = input("your answer : ")
    if 'no' in querry:
        speak("closing Application")
        exit1()
        os.system("TASKKILL /F /IM pycharm64.exe")
    elif 'shutdown' in querry or "yes" in querry:
        os.system("shutdown /s ")
        speak("Your system will shutdown within a minute ")
        exit1()
    elif 'restart' in querry:
        os.system("shutdown /r ")
        speak("Your system will restart within a minute ")
        exit1()

def stop_listening(value):
    string1 = value
    try:
        a=int(re.search(r'\d+', string1).group())
    except:
        speak("I cannot do this right now!! sorry for inconvience")
    if "second" in string1:
        speak(f"I will not listen anything for {a} seconds")
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(a)
    elif "minute" in string1:
        speak(f"I will not listen anything for {a} minutes")
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(60 * a)
    speak("I am activated")

def main():

    while True:

    ####################### Taking User command #########################

        try:
            querry = takecommand1().lower()

        except Exception as e:
            querry = input("what can i do for you:")


    ####################### Music #########################
        if "music" in querry or "songs" in querry:
            try:

                musicdir = 'C:\\Users\\Admin\\Music'
                songs = os.listdir(musicdir)
                speak("playing songs from your music directory")
                os.startfile(os.path.join(musicdir, songs[random.randint(1, 64)]))
                speak("I am ready for next command")
            except Exception as e:
                speak("which song would you like to listen")
                try:
                    querry=takecommand1().lower()
                except Exception as e:
                    querry = input("Enter song name : ")
                p.playonyt(querry)
                speak("I am ready for next command")

        ####################### Sending Email #########################

        elif 'send' in querry and ('email' in querry or 'mail' in querry):
                try:
                    mail()
                except:
                    speak("sorry !!Unable to send Email because of no internet connection")
                speak("what's my next task ")

        ####################### Sending Whatsapp message #########################

        elif 'send' in querry and 'message' in querry:
                try:
                    whatsappmsg()
                except:
                    speak("sorry !!Unable send message because of no internet connection")
                speak("I am ready for next command")

        ####################### OPening mail #########################

        elif 'mail' in querry:
                speak("opening mail")
                webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
                speak("what's my next task ")

        ####################### OPening Google Photos #########################

        elif 'photos' in querry:
                speak("opening google photos")
                webbrowser.open("https://photos.google.com/?tab=mq&pageId=none")
                speak("I am ready for next command")


        ####################### For Time #########################

        elif 'time' in querry:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strtime}")
                speak("what's my next task ")

        ####################### Getting News update #########################

        elif 'news' in querry and 'update' in querry:
                speak("fetching News!!")
                try:
                    news()
                    speak("These were latest news!!I am ready for next command")
                except:
                    speak("sorry !!Unable to fetch news because of no internet connection")
        ####################### Geting Weather Details #######################

        elif 'weather' and "details" in querry:
                try:
                    weather()
                except:
                    speak("sorry !!Unable to fetch weather details due to lack internet connection")
                speak("what's my next task ")

        ####################### Searching A file in system #########################

        elif 'search' in querry and 'file' in querry:
                speak("Please type the file name that you want to search along with extension!!")
                s = input("name: ")
                find(s)
                speak("I am ready for next command")

        ####################### Opening whatsapp  #########################
        elif 'whatsapp' in querry:
                speak("opening whatsapp")
                try:
                    os.startfile("C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
                except:
                    speak("you may need to scan QR code if you have not login before")
                    webbrowser.open("https://web.whatsapp.com/")
                speak("what's my next task ")
        ####################### OPening Instagram #########################

        elif 'instagram' in querry:
                speak("opening instagram")
                webbrowser.open("https://www.instagram.com/")
                speak("I am ready for next command")
        ####################### Searching on web  #########################

        elif 'google' in querry:
                speak("what do you want to search")
                try:
                    querry = takecommand1().lower()
                except Exception as e:
                    querry = input("what do you want to search:")
                webbrowser.open("https://www.google.com/search?q=" + querry)
                speak("These are the results from Google")
                speak("what's my next task ")
        ####################### Searching videos On Youtube #########################

        elif 'youtube' in querry:
                speak("what do you want to watch")
                try:
                    querry = takecommand1().lower()
                except Exception as e:
                    querry = input("what do you want to watch :")
                webbrowser.open('https://www.youtube.com/results?search_query=' + querry)
                speak("These are the results from youtube")
                speak("I am ready for next command")

        #######################  Playing youtube  #########################

        elif 'video' in querry:
                querry = querry.replace("video", "")

                try:
                    p.playonyt(querry)
                    speak("These are the results from youtube")
                except:
                    speak("sorry !!Unable to access youtube because of no internet connection")
                speak("what's my next task ")

        ####################### Opening NotePad #########################

        elif "open notepad" in querry:
            try:
                subprocess.Popen("notepad.exe")
            except:
                speak("Sorry !! unable to open notepad")
            speak("I am ready for next command")
        ####################### OPening Calculator #########################

        elif "open calculator" in querry:
            try:
                subprocess.Popen("calc.exe")
            except:
                speak("Sorry !! unable to open Calculator")
            speak("what's my next task ")

        ####################### OPENING CMD #########################

        elif "open command prompt"  in querry or "cmd" in querry:
            try:
                os.popen("Start cmd")
            except:
                speak("Sorry !! unable to open Command prompt")
            speak("what's my next task ")

        ####################### OPening Word #########################

        elif "open word" in querry:
            doc = docx.Document()
            speak("what name would you like to give to word document.")
            try:
                querry =takecommand1()
            except Exception as e:
                querry = input("enter file name : ")
            doc.save(querry+".docx")
            speak("Opening word document")
            os.system("start "+querry+".docx")
            speak("I am ready for next command")

        ####################### OPening Excel #########################

        elif "open excel" in querry:
            speak("what name would you like to give to excel document.")
            try:
                querry = takecommand1()

            except Exception as e:
                querry = input("enter file name : ")

            x1=Workbook()
            speak("Opening excel document")
            x1.save(querry+".xlsx")
            os.system("start " +querry+".xlsx")
            speak("what's my next task ")


        ####################### Searching in wikipedia #########################

        elif 'wikipedia'   in querry:
                speak("searching in wikipedia....")
                querry = querry.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(querry, sentences=3)
                    speak("according to wikipedia..")
                    print(results)
                    speak(results)
                    speak("I am ready for next command")
                except Exception as e:
                    speak(f"Page not found because of no internet connection or lack of information about {querry}. please try another page  ")
                    speak("what is my next command")

        ####################### Getting information About person #########################

        elif 'who is' in querry :
                speak("searching in wikipedia....")
                querry = querry.replace("who is","")
                try:
                    results = wikipedia.summary(querry,sentences=3)
                    speak("according to wikipedia..")
                    print(results)
                    speak(results)
                    speak("what is my next command")
                except Exception as e:
                    speak(f"Page not found because of no internet connection or lack of information about {querry}. please try another page  ")
                    speak("I am ready for next command")
        ####################### Taking a screenshot #########################

        elif "screenshot" in querry:
            try:
                pyautogui.hotkey('win', 'printscreen')
            except:
                speak("sorry !! unable to access your keyboard")
            speak("screenshot taken")
            speak("I am ready for next command")

        ####################### Switching tab  #########################

        elif "switch screen" in querry or "switch" in querry :
            try:
                pyautogui.hotkey("alt", "tab")
            except:
                speak("sorry !! unable to access your keyboard")
            speak("what's my next task ")
        ####################### Scrolling down #########################

        elif "down" in querry:
            try:
                pyautogui.press("space")
            except:
                speak("sorry !! unable to access your keyboard")
            speak("I am ready for next command")

        ####################### Scrolling Up #########################

        elif "up" in querry:
            try:
                pyautogui.press("up")
            except:
                speak("sorry !! unable to access your keyboard")
            speak("what's my next task ")
        ####################### Closing tab #########################

        elif "close" in querry:
            try:
                pyautogui.hotkey("alt", "F4")
            except:
                speak("sorry !! unable to access your keyboard")
            speak("I am ready for next command")

        ####################### find location #########################
        elif "find" in querry and "location":
            speak("what do you want to locate")
            try:
                querry = takecommand1().lower()
            except Exception as e:
                querry = input("what do you want to locate :")
            webbrowser.get().open('https://google.nl/maps/place/'+querry+"/@amp;")
            time.sleep(2)
            speak(f"here is the location of {querry}")

        ####################### sleeping Program #########################

        elif "sleep" in querry:
            speak("sleeping mode activated !! You can activate me any time")
            main2()


        elif "stop application" in querry or "terminate" in querry or "stop this application" in querry:
            try:
                terminate()
            except:
                exit()
        ####################### Stop Listening #########################

        elif "stop listening" in querry:
            stop_listening(querry)

        ####################### If querry doesn't matches any of above conditions #########################

        else:
           basic_commands(querry)


def main2():
    while True:
        try:
            querry = takecommand1()
        except:
            querry = input("Type activate :")
        if "wake up" in querry or "activate" in querry:
            speak("I am activated")
            main()
        elif "close" in querry or "terminate" in querry:
           terminate()

def basic_commands(querry):

    if "how are you" in querry:
        speak("I am fine sir!! What about you ??")

    elif "good" in querry or "fine" in querry:
        speak("Nice to listen that")

    elif "thankyou" in querry or "thanks" in querry:
        speak("Its my pleasure sir!! I am always available for you !!!!")

    elif "name" in querry:
        speak("My name is alexa and I am virtual assistant")

    elif "yourself" in querry or "functions" in querry or "what can you do" in querry:
        speak(" My name is alexa!!! My maker has assemble a great deal of capacities "
              "in me!!I can send emails,!whatsapp messages !! can give climate subtleties,"
              " news refreshes!!,play tunes, can take you to visit through web surfing !! "
              "fetch information about anyone and lots more!! But I am in developing stage!!!"
              "my developers are updating me daily!!!!!")

    elif "born" in querry or "birthday" in querry or "created" in querry:
        speak("I was born on 11 september 2020 as a captone project by my developers")

    elif "i love you" in querry:
        speak("I love you to ")

    else:
        speak("sorrry  I didn't understand that!! ")
    main()

if __name__ == '__main__':
    # validation()
    df = pd.read_excel("birthday.xlsx")
    wishMe()
    try:
        weather()
    except:
        speak("Incapable to get climate News because of absence of internet connection!! and also some function may not work")
    main()
