import serial
from time import sleep
ser = serial.Serial('COM5')
import numpy as np
from statistics import mean

def Average(lst):
    return mean(lst)

def GetData(samples, sensors):
    ser.flushInput()
    total_samples = (samples-1)*(sensors-1)
    current_sample = 0
    sample_iteration = 0
    mq135 = []
    mq2 = []
    mq3 = []
    mq4 = []
    mq5 = []
    mq6 = []
    mq7 = []
    mq8 = []
    mq9 = []
    tga = []
    tgb = []
    tbc = []
    message = True
    f = open("sensordata.txt", "w")
    x = current_sample * sample_iteration
    while x < total_samples:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            f.write("S."+str(int(sample_iteration))+"."+str(current_sample%sensors)+": ")
            f.write(str(decoded_bytes))
            f.write("\n")
            message = True
            print("got sample: ", current_sample)
            x = current_sample * sample_iteration
            if (current_sample == 0):
                mq135.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 1):
                mq2.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 2):
                mq3.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 3):
                mq4.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 4):
                mq5.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 5):
                mq6.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 6):
                mq7.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 7):
                mq8.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 8):
                mq9.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 9):
                tga.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 10):
                tgb.append(int(decoded_bytes))
                current_sample+=1
            elif (current_sample == 11):
                tgc.append(int(decoded_bytes))
                current_sample = 0
                sample_iteration+=1
        except Exception as e: 
            #print(e)
            sleep(0.1)
    f.close()
    return mq135, mq2, mq3, mq4, mq5, mq6, mq7, mq8, mq9, tga, tgb, tgc
    