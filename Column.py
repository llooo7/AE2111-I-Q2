import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from useful_functions import *
from Stringer_moi import *

span2 = np.arange(0,0.4*12.815,0.001)
E = 69*10**9
K=1/4

def critical_stress(I,L,A_str):
    return np.pi**2*K*E*I/L**2/A_str

def column(A_str,n_str_top,n_str_bot):
    chords = chord_length(span2)
    stress = []
    p = 0

    for i in chords: 
        
        N = 42300
            
        S = N/(A_str*(n_str_top+n_str_bot))
        stress.append(S)
        L = span2[p]
        p+=1

    return stress,L
        
def safety_margin(f,y):
    margin = []
    
    for i in f:
        m = y/i
        margin.append(m)
            
    return margin
    
safety1 = []


for tspar,tskin,nstrtop,nstrbot,astr,lstr in zip(t_sparl, t_skinl, n_str_topl, n_str_botl, A_strl,l_strl):
    
    s,L = column(astr,nstrtop,nstrbot)
    
    t_str = astr/2/lstr
    I = (nstrtop+nstrbot)*str_moment_inertia(lstr, t_str)
    s_crit = critical_stress(I, L, astr)
    print(s_crit)
    m1 = safety_margin(s,s_crit)
    

    
    safety1.append(m1)



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
