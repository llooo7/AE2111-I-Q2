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

print(n_crit_max,n_crit_min)

momentmax = moment[idx1]
momentmin = moment[idx2]



plt.plot(span, momentmax, color = 'blue')
plt.plot(span, momentmin, color = 'blue')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()