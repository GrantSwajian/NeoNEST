import sys
from adcstuff import GetData
from adcstuff import Average
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

print("Hello World")
a,b,c,d,e,f,g,h,i,j,k,l = GetData(10, 12)
sleep(1)

xpoints = np.array ([0,12])
ypoints = np.array([0,200])
plt.plot(a,marker = '*', color = "black")
plt.plot(b,marker = '*', color = "red")
plt.plot(c,marker = '*', color = "yellow")
plt.plot(d,marker = '*', color = "green")
plt.plot(e,marker = '*', color = "blue")
plt.plot(f,marker = '*', color = "magenta")
plt.plot(g,marker = '*', linestyle='dashed', color = "black")
plt.plot(h,marker = '*', linestyle='dashed', color = "red")
plt.plot(i,marker = '*', linestyle='dashed', color = "yellow")
plt.plot(j,marker = '*', linestyle='dashed', color = "green")
plt.plot(k,marker = '*', linestyle='dashed', color = "blue")
plt.plot(l,marker = '*', linestyle='dashed', color = "magenta")
plt.show()
sleep(10)
 
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
