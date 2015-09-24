#!/usr/bin/python

import subprocess, time, Image, socket
from Adafruit_Thermal import *


import time
from subprocess import call

call(["rm","snap.jpg"])
time.sleep(1)

call(["uvccapture","-S40","-C100", "-G80", "-B70", "-x320", "-y240", "-v", "-m"])
time.sleep(3)



printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)


printer.printImage(Image.open('snap.jpg'), False)
printer.feed(3)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
