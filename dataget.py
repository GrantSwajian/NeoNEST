import serial
from time import sleep
ser = serial.Serial('COM5')
ser.flushInput()
import numpy as np


def GetData(samples, sensors):
    total_samples = samples*sensors
    current_sample = 0
    message = True
    f = open("sensordata.txt", "w")
    while current_sample < total_samples:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            f.write("S."+str(int(current_sample/sensors))+"."+str(current_sample%sensors)+": ")
            f.write(str(decoded_bytes))
            f.write("\n")
            message = True
            print("got sample: ", current_sample)
            current_sample+=1
        except Exception as e: 
            #print(e)
            sleep(0.1)
    f.close()
    print("done")