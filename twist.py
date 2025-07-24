import serial
import time

# Replace with your Arduino port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux/Mac)
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

# Send the command to trigger servo twist
arduino.write(b't')

arduino.close()