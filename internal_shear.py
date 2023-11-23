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

n_values = [-1,-1,2.6567,2.6567,2.5,2.5,-1,-1,2.5,2.5,-1,-1,2.6567,2.6567,-1,-1,2.5,2.5,-1,-1,2.5,2.5,-1,-1]
mass_values = [15017.1,15017.1,15017.1,15017.1,26748.6,26748.6,26748.6,26748.6,31139.2,31139.2,31139.2,31139.2,15017.1,15017.1,15017.1,15017.1,26748.6,26748.6,26748.6,26748.6,31139.2,31139.2,31139.2,31139.2]
v_values = [30,127,68.5,159,88.5,159,57,127,95.5,159,61,127,68.5,133.5,42,127,88.5,133.5,56,127,95.5,133.5,60.5,127] 
h_values = [0,0,0,0,0,0,0,0,0,0,0,0,10668,10668,10668,10668,10668,10668,10668,10668,10668,10668,10668,10668]

n_values1 = [2.5,-1]
mass_values1 = [31139.2,31139.2]
v_values1 = [133.5, 127] 
h_values1 = [10668,10668]

shear = []
moment = []
torsion = []
maximum = []
maximum2 = []
maximum3 = []



for n,mass,v,h in zip(n_values1,mass_values1,v_values1,h_values1):

    Weight = mass*9.81
    rho = getDensity(h)
    v = v*np.sqrt(1.225/rho)
    q = 1/2*rho*v**2
    CLd = n*Weight/(q*surface)
    CL0 = 0.383907
    CL10 = 1.2045817
    factor = (CLd-CL0)/(CL10-CL0)
    alpha = np.arcsin(factor*np.sin(10/57.3))*57.3
    
    a,b,c,d,e = plot(n,mass,v,h,alpha,CLd)
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
m_crit_max = mass_values[idx1]
m_crit_min = mass_values[idx2]
v_crit_max = v_values[idx1]
v_crit_min = v_values[idx2]
h_crit_max = h_values[idx1]
h_crit_min = h_values[idx2]

print(n_crit_max,n_crit_min)
print(m_crit_max,m_crit_min)
print(v_crit_max,v_crit_min)
print(h_crit_max,h_crit_min)




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






