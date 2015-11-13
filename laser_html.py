import serial

import urllib2
import json
import time

ser = serial.Serial('/dev/ttyUSB0',9600)
multiplier = 100.
#mydata =  urllib2.urlopen("http://45.55.243.197/location").read()

while True:

    mydata =  json.load(urllib2.urlopen("http://45.55.243.197/location"))
    x =  int((mydata['x'] - .5) * 2 * multiplier)
    y =  int((mydata['y'] - .5) * 2 * multiplier)
    #print "x:"+ str(x)
    #print "y:" + str(y)
    #time.sleep(0.1)
    ser.write(str(x) + ','+ str(y) + '.')
