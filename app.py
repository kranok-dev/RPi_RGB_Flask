from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import threading
import time

red   = 14    #(RPi 3B+ GPIO14)
green = 15    #(RPi 3B+ GPIO15)
blue  = 18    #(RPi 3B+ GPIO18)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red,  GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red,  GPIO.LOW)
GPIO.output(green,GPIO.LOW)
GPIO.output(blue, GPIO.LOW)
time.sleep(2)

#-----------------------------------------------------------------------
def redColor():
    while(True):
        global red,pulseWidth,redPWM
        GPIO.output(red,GPIO.HIGH)
        time.sleep(pulseWidth*redPWM/255)
        GPIO.output(red,GPIO.LOW)
        time.sleep(pulseWidth*(1-redPWM/255))

#-----------------------------------------------------------------------
def greenColor():
    while(True):
        global green,pulseWidth,greenPWM
        GPIO.output(green,GPIO.HIGH)
        time.sleep(pulseWidth*greenPWM/255)
        GPIO.output(green,GPIO.LOW)
        time.sleep(pulseWidth*(1-greenPWM/255))
        
#-----------------------------------------------------------------------
def blueColor():
    while(True):
        global blue,pulseWidth,bluePWM
        GPIO.output(blue,GPIO.HIGH)
        time.sleep(pulseWidth*bluePWM/255)
        GPIO.output(blue,GPIO.LOW)
        time.sleep(pulseWidth*(1-bluePWM/255))
        
#-----------------------------------------------------------------------

pulseWidth = 0.01
redPWM = 255
greenPWM = 255
bluePWM = 255

thread_red   = threading.Thread(target=redColor)
thread_green = threading.Thread(target=greenColor)
thread_blue  = threading.Thread(target=blueColor)

thread_red.start()
thread_green.start()
thread_blue.start()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/result/<color>/<value>')
def result(color,value):
    global redPWM,greenPWM,bluePWM
    if(color == "red"):
        redPWM = int(value)
    elif(color == "green"):
        greenPWM = int(value)
    elif(color == "blue"):
        bluePWM = int(value)
        
    return "Ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
