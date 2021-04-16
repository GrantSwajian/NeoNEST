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
plt.plot(a,marker = '*', color = "blue")
plt.plot(b,marker = '*', color = "green")
plt.plot(c,marker = '*', color = "red")
plt.plot(d,marker = '*', color = "brown")
plt.plot(e,marker = '*')
plt.plot(f,marker = '*')
plt.plot(g,marker = '*')
plt.plot(h,marker = '*')
plt.plot(i,marker = '*')
plt.plot(j,marker = '*')
plt.plot(k,marker = '*')
plt.plot(l,marker = '*')
plt.show()
sleep(10)
 
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
