import sys
from adcstuff import GetData
from adcstuff import Average
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

print("Hello World")
a,b,c,d = GetData(10, 4)
mq135average = Average(a)
mq2average = Average(b)
mq3average = Average(c)
mq4average = Average(d)
sleep(1)

xpoints = np.array ([0,12])
ypoints = np.array([0,200])
plt.plot(a,marker = '*', color = "blue")
plt.plot(b,marker = '*', color = "green")
plt.plot(c,marker = '*', color = "red")
plt.plot(d,marker = '*', color = "brown")
plt.show()
sleep(10)
 
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
