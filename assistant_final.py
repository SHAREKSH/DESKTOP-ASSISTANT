from assistant_final_gui import  Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import os
import webbrowser as web
import sys
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import wolframalpha
import requests
from bs4 import BeautifulSoup




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am rio , i am your personal assistant , how may i help you")   
def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("sharekshkshetri999@gmail.com", 'sncjxxjksibcbsdq')
        server.sendmail('sharekshkshetri123@gmail.com', to, content)
        server.close()   
def wolfram(query):
    api="69AKJE-E7J2HG76WY"
    requester=wolframalpha.Client(api)
    request=requester.query(query)
    try:
        result=next(request.results).text
        speak(result)
    except:
        speak("sorry ")
def calculator(query):
    term=str(query)
    term=term.replace("hydra","")
    term=term.replace("plus","+")
    term=term.replace("minus","-")
    term=term.replace("multiply","*")
    term=term.replace("divide","/")
    term=term.replace("calculate","")
    wolfram(term)
    

def temprature():
          #search="temprature in jalandhar"
          #url=f"https://www.google.com/search?={search}"
          #r=requests.get(url)
          #data=BeautifulSoup(r.text,"html.parser")
          #temprature=data.find("div",class_="BNeawe").text
          #speak(f"the temprature  outside is {temprature} celsius")
          wolfram("temprature in jalandhar")
      

class mainthread(QThread):

    def __init__(self):
        super(mainthread,self).__init__()
    def run(self):
        self.logic()
        
  
    def takeCommand(self):

         #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("listening")
            print("Listening...")
            r.energy_threshold = 500  # minimum audio energy to consider for recording
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            speak("recognizing")
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

    def logic(self):
        speak("importing    os   , checking      internet    ,       importing      user    interface   ,      importing        modules  ")
        speak("systems are now fully operational")
        wishMe()
        while True:
    
         self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
         if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

         elif 'open youtube' in self.query:
            webbrowser.open("youtube.com")
        

         elif 'open google' in self.query:
                 webbrowser.open("google.com")

         elif 'open stackoverflow' in self.query:
                 webbrowser.open("stackoverflow.com")   
         elif "chrome" in self.query:
            web.open("https:/www.chrome.com/")

         elif 'play music' in self.query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

         elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

         elif 'open code' in self.query:
                 #codePath = "C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
                 #os.startfile(codePath) 
                 pass

         elif 'email' in self.query:
             try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "sharekshkshetri123@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
             except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")    
         elif "calculate" in self.query:
               calculator(self.query)
               
            
         elif "weather" in self.query:
            speak("checking")
            temprature()


         elif "wait"in self.query:
            import time
            speak("ok sir")
            time.sleep(13)          
         elif"stop" in self.query:
            speak("good by sir,have a   great  day   ahead")
            sys._exit()
startExe=mainthread()
class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        
        self.gui.setupUi(self)


        self.gui.pushButton_start.clicked.connect(self.start_task)
        self.gui.pushbutton_exit.clicked.connect(self.close)
        self.gui.pushButton_chrome.clicked.connect(self.chrome_app)
        self.gui.pushButton_yt.clicked.connect(self.yt_app)

    def chrome_app(self):
        os.startfile("https:/www.chrome.com/")
    def yt_app(self):
        web.open("https://www.youtube.com/")
    def start_task(self):
        

        self.gui.label=QtGui.QMovie("..//assistant_material//ExtraGui-20221017T140106Z-001/Earth.gif")
        self.gui.gif1.setMovie(self.gui.label)
        self.gui.label.start()

        self.gui.label2=QtGui.QMovie("..//assistant_material//VoiceReg-20221017T135923Z-001/VoiceReg/Siri.gif")
        self.gui.gif3.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3=QtGui.QMovie("..//assistant_material//ExtraGui-20221017T140106Z-001/initial.gif")
        self.gui.gif3_2.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4=QtGui.QMovie("..//assistant_material//gif2.gif")
        self.gui.gif4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5=QtGui.QMovie("..//assistant_material//gif3.gif")
        self.gui.gif5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6=QtGui.QMovie("..//assistant_material//gif4.gif")
        self.gui.gif6.setMovie(self.gui.label6)
        self.gui.label6.start()
        timer=QTimer(self)
        timer.timeout.connect(self.show_tandd)
        timer.start(1000)
        startExe.start()

    def show_tandd(self):
        a=QTime.currentTime()
        b=QDate.currentDate()
        A=a.toString()
        B=b.toString()
        lable_date=B
        lable_time=A
        self.gui.text_date.setText(lable_date)
        self.gui.text_time.setText(lable_time)



guiapp=QApplication(sys.argv)
assistant_gui=Gui_start()
assistant_gui.show()
exit(guiapp.exec())

