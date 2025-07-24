import serial
import time

arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(1)  

arduino.write(b't')

arduino.close()
