import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from wing import *
from aeroforces import *
from isa import *
from bending_moment import *

fig, ax = plt.subplots()
span = np.arange(0,12.815,0.001)

n_values = [1.21,-2.23,3.23,-1.1]
mass_values = [2,3,4,5]
v_values = [3,4,5,6] 
h_values = [4,5,6,7]
shear = []
moment = []
torsion = []
maximum = []
checkmax = []
checkmin = []


for n,mass,v,h in zip(n_values,mass_values,v_values,h_values):

    Weight = mass*9.81
    v = v*np.sqrt(1.225/h)
    q = 1/2*getDensity(h)*v**2
    CLd = n*Weight/(0.5*h*v**2*surface)
    CL0 = 0.383907
    CL10 = 1.2045817
    factor = (CLd-CL0)/(CL10-CL0)
    alpha = np.arcsin(factor*np.sin(10/57.3))*57.3
    
    a,b,c,d = plot(n,mass,v,h,alpha)
    shear.append(b)
    maximum.append(b[0])
    
for i in shear:  
    
    plt.plot(span, i, color = 'red')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()



idx1 = maximum.index(max(maximum))
idx2 = maximum.index(min(maximum))

print(n_values[idx1])
    
 
    