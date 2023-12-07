import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from useful_functions import *

span2 = np.arange(0,0.4*12.815,0.001)
E = 69*10**9

critical_stress = 241*10**6

def compressive(t_spar, t_skin, n_str_top, n_str_bot, A_str):
    chords = chord_length(span2)
    stress1 = []
    stress2 = []
    stress3 = []
    stress4 = []


    for i in chords: 
        A1,A2,A3,A4,height,left,right,bottom = area_section(i, t_spar, t_skin, n_str_top, n_str_bot, A_str)
        N = 42300
            
        S1 = N/A1
        S2 = N/A2
        S3 = N/A3
        S4 = N/A4
    
        stress1.append(S1)
        stress2.append(S2)
        stress3.append(S3)
        stress4.append(S4)

        
    return stress1,stress2,stress3,stress4
        
def safety_margin(f,y):
    margin = []
    
    for i in f:
        m = y/i
        margin.append(m)
            
    return margin
    
safety1 = []
safety2 = []
safety3 = []
safety4 = []


for tspar,tskin,nstrtop,nstrbot,astr in zip(t_sparl, t_skinl, n_str_topl, n_str_botl, A_strl):
    
    s1,s2,s3,s4 = compressive(tspar, tskin, nstrtop, nstrbot, astr)
    

    m1 = safety_margin(s1,critical_stress)
    m2 = safety_margin(s2,critical_stress)
    m3 = safety_margin(s3,critical_stress)
    m4 = safety_margin(s4,critical_stress)

    
    safety1.append(m1)
    safety2.append(m2)
    safety3.append(m3)
    safety4.append(m4)


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
    
    plt.plot(span2, i, color = c,label=k)
    
    l+=1
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,0.4*12.815)
plt.xlabel('y [m]')
plt.ylabel('Shear Force [N]')
plt.legend(loc='upper right')
plt.title('Internal Shear Force for n = -1 and n = 2.5')

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
   
    plt.plot(span2, j, color = p,label=q)
    t+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,0.4*12.815)
plt.xlabel('y [m]')
plt.ylabel('Shear Force [N]')
plt.legend(loc='upper right')
plt.title('Internal Shear Force for n = -1 and n = 2.5')

plt.grid(True)

plt.show()


l1 = 0    
for dababy in safety3:

    if l1 == 0:
        c1 = 'red'
        k1 = 'Design option 1'
    elif l1 == 1:
        c1 = 'blue'
        k1 = 'Design option 2'
    elif l1 == 2:
        c1 = 'green'
        k1 = 'Design option 3'
    
    plt.plot(span2, dababy, color = c1,label=k1)
    
    l1+=1
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,0.4*12.815)
plt.xlabel('y [m]')
plt.ylabel('Shear Force [N]')
plt.legend(loc='upper right')
plt.title('Internal Shear Force for n = -1 and n = 2.5')

plt.grid(True)
plt.show()

t1 = 0
for joo in safety4:

    if t1 == 0:
        p1 = 'red'
        q1 = 'Design option 1'
    elif t1 == 1:
        p1 = 'blue'
        q1 = 'Design option 2'
    elif t1 == 2:
        p1 = 'green'
        q1 = 'Design option 3'
   
    plt.plot(span2, joo, color = p1,label=q1)
    t1+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.xlim(0,0.4*12.815)
plt.xlabel('y [m]')
plt.ylabel('Shear Force [N]')
plt.legend(loc='upper right')
plt.title('Internal Shear Force for n = -1 and n = 2.5')

plt.grid(True)

plt.show()
    


        
    
    
    
    

