import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from useful_functions import *
from Internal_moment import *
from test import *


ks_top = 16
ks_bottom = 16
v = 0.3333333333333333
E = 68.94757*10**9
b_top = 1.7969480351999998
b_bottom = 1.797201170322717
l_str = 0.105
t_str = 0.02
critical_stress1 = 241*10**6
    
def critical_stress(ks,E,b,v,t_skin,ntop,nbot,lstr,h,l,r,bot):
    
    b_t = (b - (ntop)*lstr)/(ntop-1)
    b_b =  (b - (nbot)*lstr)/(nbot-1)

    return (np.pi**2*ks*E)/(1-v**2)/12*(t_skin/b_t)**2,(np.pi**2*ks*E)/(1-v**2)/12*(t_skin/b_b)**2

def skin_buckling(t_spar, t_skin, n_str_top, n_str_bot, A_str,t_sparc,t_skinc,n_str_topc,n_str_botc):
    chords = chord_length(span1)
    stress1 = []
    stress2 = []
    stress3 = []
    stress4= []
    stress5 = []
    stress6 = []
 
    p = 0
   

    
    for i in chords:
        A1,A2,A3,A4,height,left,right,bottom = area_section(i, t_spar, t_skin, n_str_top, n_str_bot, A_str)
        M_max = momentmax[p]
        M_min = abs(momentmin[p])
        
        stress_top = M_min*cx[p]/I_lst[check][p]
        
        stress_bottom = M_max*(left - cx[p])/I_lst[check][p]
        stress_top1 = M_max*cx[p]/I_lst[check][p]
        stress_bottom1 = M_min*(left-cx[p])/I_lst[check][p]
        S_str_top = M_max*cx[p]/I_lst[check][p]
        S_str_bot = M_min*(left - cx[p])/I_lst[check][p]
        
        
        stress1.append(stress_top)
        stress2.append(stress_bottom)
        stress3.append(stress_top1)
        stress4.append(stress_bottom1)  
        stress5.append(S_str_top)
        stress6.append(S_str_bot)
        p+=1

    return stress1,stress2,stress3,stress4,stress5,stress6,height,left,right,bottom
        
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
safety5 = []
safety6 = []
check = 0
for tspar,tskin,nstrtop,nstrbot,astr,lstr,tsparc,tskinc,nstrtopc,nstrbotc in zip(t_sparl, t_skinl, n_str_topl, n_str_botl, A_strl,l_strl,t_sparcl,t_skincl,n_str_topcl,n_str_botcl):
    
    stress1,stress2,stress3,stress4,stress5,stress6,h,l,r,b = skin_buckling(tspar, tskin, nstrtop, nstrbot, astr, tsparc, tskinc, nstrtopc, nstrbotc)
    stress_cr1,stress_cr2 = critical_stress(ks_top, E, b_top, v, t_skin,nstrtop,nstrbot,lstr,h,l,r,b)


    m1 = safety_margin(stress1, stress_cr1)
    m2 = safety_margin(stress2, stress_cr2)
    m3 = safety_margin(stress3, critical_stress1)
    m4 = safety_margin(stress4, critical_stress1)
    m5 = safety_margin(stress5, critical_stress1)
    m6 = safety_margin(stress6, critical_stress1)
    safety1.append(m1)
    safety2.append(m2)
    safety3.append(m3)
    safety4.append(m4)
    safety5.append(m5)
    safety6.append(m6)
    
    check += 1

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
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Skin Buckling of the top skin panel (n=2.5)')
plt.ylim(0,15)
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
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin [N]')
plt.legend(loc='upper left')
plt.title('Skin Buckling of the bottom skin panel (n=-1)')
plt.ylim(0,15)
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
    
    plt.plot(span1, dababy, color = c1,label=k1)
    
    l1+=1
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')

plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Tension Failure of the top skin panel (n=-1)')

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
   
    plt.plot(span1, joo, color = p1,label=q1)
    t1+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Tension Failure of the bottom skin panel (n=2.5)')

plt.grid(True)

plt.show()  
    
t2 = 0
for jooo in safety5:

    if t2 == 0:
        p2 = 'red'
        q2 = 'Design option 1'
    elif t2 == 1:
        p2 = 'blue'
        q2 = 'Design option 2'
    elif t2 == 2:
        p2 = 'green'
        q2 = 'Design option 3'
   
    plt.plot(span1, jooo, color = p2,label=q2)
    t2+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Tension failure of the top stringers (n=-1)')

plt.grid(True)

plt.show()
        
    
 
t3= 0
for joooo in safety6:

    if t3 == 0:
        p3 = 'red'
        q3 = 'Design option 1'
    elif t3 == 1:
        p3 = 'blue'
        q3 = 'Design option 2'
    elif t3 == 2:
        p3 = 'green'
        q3 = 'Design option 3'
   
    plt.plot(span1, joooo, color = p3,label=q3)
    t3+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Tension Failure of the bottom stringers (n=2.5)')

plt.grid(True)

plt.show()
              

plt.plot(span1,stress4)
plt.show()
    
    