#! /usr/bin/env python

import os
import time

#Returns the current time and temperature in Celcius and Fahrenheit

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006972625/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	return[currentTime, tempC, tempF]

print readTemp()
