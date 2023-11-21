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
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()

n_crit_max = n_values[idx1]
n_crit_min = n_values[idx2]

plt.plot(span, torsion[idx1], color = 'green')
plt.plot(span, torsion[idx2], color = 'green')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()