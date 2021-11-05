# This is a volume script for volumio
# It use mpc instead of volumio to faster apply the actions
# make sure mpd support is enabled in volumio!

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
        subprocess.Popen(['mpc', 'volume', '-2'])
    else:
        subprocess.Popen(['mpc', 'volume', '+2'])

def togglePlay(e):
    subprocess.Popen(['mpc', 'toggle'])

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