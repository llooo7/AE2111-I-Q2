import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from internal_shear import *

for i in torsion:
    plt.plot(span, i, color = 'green')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Internal Torque [Nm]')
plt.title('Internal Torque in [Nm] for all loading cases')

plt.grid(True)

plt.show()

plt.show()

n_crit_max = n_values[idx1]
n_crit_min = n_values[idx2]

torquemax = torsion[idx1]
torquemin = torsion[idx2]




plt.plot(span, torsion[idx1], color = 'green',label = 'n = 2.5')
plt.plot(span, torsion[idx2], color = 'orange',label = 'n = -1')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Internal Torque [Nm]')
plt.title('Internal Torque in [Nm] for n = -1 and n = 2.5')
plt.legend(loc='lower right')
plt.grid(True)

plt.show()