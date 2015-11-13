import serial
import time
ser = serial.Serial('/dev/ttyUSB0',19200)
ser.flush()
if ser.isOpen():
    ser.close()
ser.open()


time.sleep(2)
print ("yo")
#print ser.read()
ser.write(b'30.0,30.0;')
ser.close()
