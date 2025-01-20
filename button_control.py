from tkinter import *
import os
import sys
import time
import datetime
import RPi.GPIO as GPIO
import face_detect
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

t = Thread(target = face_detect.TrackImages)
t.start()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def safe_exit(signum, frame):
    exit(1)
    
lcd = LCD()

Motor1A = 20
Motor1B = 26
Motor2A = 19
Motor2B = 16
Water_pump = 12

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Water_pump,GPIO.OUT)

GPIO.output(Water_pump,GPIO.LOW)
r=Tk()
r.geometry('600x400')
r.title('Fire Fighting')

def back():
    print("Backward")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    
def forw():
    print("FORWARD")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    
def right():
    print("RIGHT")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    
def left():
    print("LEFT")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    
def stop():
    print("Stop")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    
def On():
    print("PUMP ON")
    GPIO.output(Water_pump,GPIO.HIGH)
    time.sleep(1)
    
def Off():
    print("PUMP OFF")
    GPIO.output(Water_pump,GPIO.LOW)
    
def text():
    txt = input("Enter Message")
    lcd.text("FIRE RESCUE",1)
    lcd.text(txt,2)
    
l1=Label(r,text='Fire Fight',fg='navy', font=('bold',20)).pack()
b1=Button(r,text='Forward',fg='Blue', font=('bold',20),activebackground = "Pink",command=forw)
b1.place(x=233,y=75)
b2=Button(r,text='Backward',fg='Blue', font=('bold',20),activebackground = "Pink",command=back)
b2.place(x=222,y=225)
b3=Button(r,text='Right',fg='Blue', font=('bold',20),activebackground = "Pink",command=right)
b3.place(x=150,y=150)
b4=Button(r,text='Left',fg='Blue', font=('bold',20),activebackground = "Pink",command=left)
b4.place(x=350,y=150)
b5=Button(r,text='Stop',fg='red', font=('bold',20),activebackground = "Pink",command=stop)
b5.place(x=250,y=150)
b6=Button(r,text='ON',fg='Blue', font=('bold',20),activebackground = "Pink",command=On)
b6.place(x=20,y=20)
b7=Button(r,text='OFF',fg='Blue', font=('bold',20),activebackground = "Pink",command=Off)
b7.place(x=500,y=20)
b8=Button(r,text='TEXT',fg='Blue', font=('bold',20),activebackground = "Pink",command=text)
b8.place(x=20,y=80)

r.mainloop()
