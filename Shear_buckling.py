import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from useful_functions import *
from internal_shear import *
from Internal_torsion import *

kv = 1.5
ks_front = 15
ks_back = 15
v = 0.3333333333333333
E = 68.94757*10**9

def torsion_stress(c,t_spar,t_skin,n_str_top,n_str_bot,A_str,T):
     A,left,right,height,bottom = area_enclosed(c, t_spar, t_skin, n_str_top, n_str_bot, A_str)
     return T/(2*A*t_spar)
    
def critical_stress(ks,E,b,v,t_spar):
    return (np.pi**2*ks*E)/(1-v**2)/12*(t_spar/b)**2

def shear_buckling(t_spar, t_skin, n_str_top, n_str_bot, A_str,t_sparc,t_skinc,n_str_topc,n_str_botc):
    chords = chord_length(span1)
    stress = []
    stress2 = []
    change = chords[9500]
    p = 0

    for i in chords:
        if i <= change:
            t_spar = t_sparc
            t_skin = t_skinc
            n_str_top = n_str_topc
            n_str_bot = n_str_botc
        
        A1,A2,A3,A4,height,left,right,bottom = area_section(i, t_spar, t_skin, n_str_top, n_str_bot, A_str)
        V = shearmax[p]
        T = torquemax[p]

        stress_avg = V/(left*t_spar+right*t_spar)
        torsion = torsion_stress(i, t_spar, t_skin, n_str_top, n_str_bot, A_str, T)
        stress_max1 = stress_avg*kv + torsion
        stress_max2 = stress_avg*kv - torsion

        
        stress.append(stress_max1)
        stress2.append(stress_max2)
        p+=1

    return stress,stress2
        
def safety_margin(f,y):
    margin = []
    
    for i in f:
        m = y/i
        margin.append(m)
            
    return margin
    
safety1 = []
safety2 = []

for tspar,tskin,nstrtop,nstrbot,astr,tsparc,tskinc,nstrtopc,nstrbotc in zip(t_sparl, t_skinl, n_str_topl, n_str_botl, A_strl,t_sparcl,t_skincl,n_str_topcl,n_str_botcl):
    
    stress,stress2 = shear_buckling(tspar, tskin, nstrtop, nstrbot, astr, tsparc, tskinc, nstrtopc, nstrbotc)
    stress_cr1 = critical_stress(ks_front, E, b_front, v, tspar)
    stress_cr2 = critical_stress(ks_back, E, b_back, v, tspar)
    
    m1 = safety_margin(stress, stress_cr1)
    m2 = safety_margin(stress2, stress_cr2)
    
    safety1.append(m1)
    safety2.append(m2)


l = 0    
for i in safety1:

    if l == 0:
        c = 'red'
        k = 'Design option 1'
    elif l == 1:
        c = 'blue'
        k = 'Design option 2'
    elif l == 2:
        c = 'green'
        k = 'Design option 3'
    
    plt.plot(span1, i, color = c,label=k)
    
    l+=1
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1.5,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Shear Buckling for the Front spar')

plt.grid(True)
plt.show()

t = 0
for j in safety2:

    if t == 0:
        p = 'red'
        q = 'Design option 1'
    elif t == 1:
        p = 'blue'
        q = 'Design option 2'
    elif t == 2:
        p = 'green'
        q = 'Design option 3'
   
    plt.plot(span1, j, color = p,label=q)
    t+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1.5,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Shear Buckling for the Rear spar')

plt.grid(True)

plt.show()


    
    
    
    
    
    
    