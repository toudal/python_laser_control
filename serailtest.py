import serial
ser = serial.Serial('/dev/ttyUSB1',baudrate=57600,timeout=5)

ser.write("30,30;")
ser.close()
