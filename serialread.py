import serial
from time import sleep

ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate
a = 0 #set a to 0
while True:
    received_data = ser.read()  # read serial port
    sleep(0.03)
    data_left = ser.inWaiting()  # check for remaining byte
    received_data += ser.read(data_left)
    a += 1
    print("{}".format(a), end='')
    print(received_data)
