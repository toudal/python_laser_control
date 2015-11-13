import serial

import urllib2
import json
import time
import threading

#ser = serial.Serial('/dev/ttyUSB0',9600)
multiplier = 100.
deltat = 0.1
#mydata =  urllib2.urlopen("http://45.55.243.197/location").read()
'''
class MyThread(threading.Thread):
    def run(self):
        mydata =  json.load(urllib2.urlopen("http://45.55.243.197/location"))
        x =  int((mydata['x'] - .5) * 2 * multiplier)
        y =  int((mydata['y'] - .5) * 2 * multiplier)
        myLock.acquire()
        print "x:"+ str(x)
        print "y:" + str(y)
        #ser.write(str(x) + ','+ str(y) + '.')
        myLock.release()
'''
myLock = threading.Lock()

def myRequest():
    mydata =  json.load(urllib2.urlopen("http://45.55.243.197/location"))
    x =  (mydata['x'] - .5) * 2 * multiplier
    y =  (mydata['y'] - .5) * 2 * multiplier
    myLock.acquire()
    #print "x:"+ str(x)
    #print "y:" + str(y)
    ser.write(str(x) + ','+ str(y) + ';')
    myLock.release()





while True:
    #thread1 = MyThread()
    #thread1.start()
    threading.Thread(target=myRequest).start() # This is the simpler consutrction
    time.sleep(deltat)
