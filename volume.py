#!/usr/bin/python
# This is a volume script for volumio

import subprocess
import time
import RPi.GPIO as GPIO
from encoder import Encoder

# set up pins
volumePinClk = 17
volumePinDt = 27
togglePin = 22


# callback functions
def valueChanged(value, direction):
    if direction == "L":
        subprocess.Popen(['volumio', 'volume', 'minus'])
    else:
        subprocess.Popen(['volumio', 'volume', 'plus'])

def togglePlay(e):
    subprocess.Popen(['volumio', 'toggle'])

# use bcm pin numbering
GPIO.setmode(GPIO.BCM)

# setup volume +/-
e1 = Encoder(volumePinDt, volumePinClk, valueChanged)

# setup toggle play/pause
GPIO.setup(togglePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(togglePin, GPIO.BOTH, callback=togglePlay, bouncetime=300)  

try:
    while True:
        time.sleep(60)
        #print("Value is {}".format(e1.getValue()))
except Exception:
    pass

GPIO.cleanup()