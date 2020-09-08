import numpy as np 
import matplotlib.pyplot as plt

t = np.arange(-10,100,0.1)
v = np.arange(-10,100,0.1)

for i in range(len(t)):
    v[i] = (50/1000)*np.exp(25*(1 - np.exp(-0.1*t[i])))


plt.plot(t,v)
plt.xlabel("Time (in days)")
plt.ylabel("Volume of Tumor (in x10^9 mm^3)")
plt.show()