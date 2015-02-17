#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sqlite3 as mydb
import sys

#Returns the current time and temperature in C/F

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006972625/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	print "Current temperature is: %s C" % tempC
	tempF = tempC*9.0/5.0+32
	print "Current temperature is: %s F" % tempF
	return[currentTime, tempC, tempF]


con = mydb.connect("/home/pi/ELSpring2015/misc/tempsensor-db/temperature.db")

cursor = con.cursor()

temperature = readTemp()

cursor.execute("INSERT INTO TempData values( (?), (?), (?) )", (temperature) )

print "Temperature logged"

con.commit()

con.close()
