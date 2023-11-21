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

n_values = [1.21,-2.23,3.23,-1]
mass_values = [15000,15000,31000,31000]
v_values = [50,46,70,69] 
h_values = [0,0,11000,11000]
shear = []
moment = []
torsion = []
maximum = []
maximum2 = []
maximum3 = []



for n,mass,v,h in zip(n_values,mass_values,v_values,h_values):

    Weight = mass*9.81
    rho = getDensity(h)
    v = v*np.sqrt(1.225/rho)
    q = 1/2*rho*v**2
    CLd = n*Weight/(q*surface)
    CL0 = 0.383907
    CL10 = 1.2045817
    factor = (CLd-CL0)/(CL10-CL0)
    alpha = np.arcsin(factor*np.sin(10/57.3))*57.3
    
    a,b,c,d = plot(n,mass,v,h,alpha)
    shear.append(b)
    moment.append(c)
    torsion.append(d)
    maximum.append(b[0])
    maximum2.append(c[0])
    maximum3.append(d[0])
    
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

n_crit_max = n_values[idx1]
n_crit_min = n_values[idx2]

shearmax = shear[idx1]
shearmin = shear[idx2]


plt.plot(span, shearmax, color = 'red')
plt.plot(span, shearmin, color = 'red')
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,12.815)
plt.xlabel('y')
plt.ylabel('I')
plt.grid(True)

plt.show()






