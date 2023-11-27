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

n_crit_max = n_values1[idx1]
n_crit_min = n_values1[idx2]

print(n_crit_max,n_crit_min)

momentmax = moment[idx1]
momentmin = moment[idx2]





plt.plot(span, momentmax, color = 'blue',label='n = 2.5')

plt.plot(span, momentmin, color = 'red', label = 'n = -1')
plt.title('Internal Bending Moment in [Nm] for n = -1 and n = 2.5')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Internal Bending Moment [Nm]')
plt.legend()
plt.grid(True)

plt.show()