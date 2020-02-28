import RPi.GPIO as GPIO
import time
import cv2
import numpy as np
from difflib import SequenceMatcher
import sys

# set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Button Pin Setup
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED Pins Setup
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    ledClock = .1
    game = True
    i = 18

    while (game == True):
        GPIO.output(i, GPIO.HIGH)
        time.sleep(ledClock)
        GPIO.output(i, GPIO.LOW)
        time.sleep(ledClock)
        i = i+1
        if i == 25:
            i = 18
        
        if GPIO.input(4) == 1 and i == 21:
            GPIO.output(i, GPIO.HIGH)
            game = False
    print("You win")
    time.sleep(3)
    GPIO.output(21, GPIO.LOW)

    GPIO.cleanup()