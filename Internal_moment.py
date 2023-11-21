import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from internal_shear import *

for i in moment:
    plt.plot(span, i, color = 'blue')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()

idx1 = maximum2.index(max(maximum2))
idx2 = maximum2.index(min(maximum2))

n_crit_max = n_values[idx1]
n_crit_min = n_values[idx2]

momentmax = moment[idx1]
momentmin = moment[idx2]

def moment_fit():
    
    a,b,c,d,e = np.polyfit(span, momentmax, 4)
    p,q,r,s,t = np.polyfit(span, momentmin, 4)


plt.plot(span, momentmax, color = 'red')
plt.plot(span, momentmin, color = 'red')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()