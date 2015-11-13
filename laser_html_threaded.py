import serial

import urllib2
import json
import time
import threading

ser = serial.Serial('/dev/ttyUSB0',19200)

#ser.open()
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()
print ser.isOpen()

multiplier = 50.
deltat = 0.05

myLock = threading.Lock()

def myRequest():
    mydata =  json.load(urllib2.urlopen("http://45.55.243.197/location"))
    x =  (mydata['x'] - .5) * 2 * multiplier
    y =  (mydata['y'] - .5) * 2 * multiplier
    myLock.acquire()
    print str(x) + ','+ str(y) + ';'
    ser.write(str(x) + ','+ str(y) + ';')
    myLock.release()

while True:
    threading.Thread(target=myRequest).start() # This is the simpler consutrction
    time.sleep(deltat)
