import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from useful_functions import *
from test import *
from Internal_moment import *
from Stringer_moi import *

span2 = np.arange(0,12.001,0.001)
E = 68.94757*10**9
K=1/4
critical_stress = 241*10**6


def critical_stress1(I,L,A_str):
    s_crit = []
    p=0
    for i in span2:
        s = np.pi**2*K*E*I[p]/L**2/A_str
        s_crit.append(s)
        p+=1
    return s_crit


def compressive(t_spar, t_skin, n_str_top, n_str_bot, A_str):
    chords = chord_length(span2)
    stress1 = []
    stress2 = []
    stress3 = []
    stress4 = []
    stress5 = []
    stress6 = []
    p = 0
    for i in chords: 
        A1,A2,A3,A4,height,left,right,bottom = area_section(i, t_spar, t_skin, n_str_top, n_str_bot, A_str)
        M_max = momentmax[p]
        M_min = abs(momentmin[p])
        if span2[p]<=0.4*12.815:
            N = 42300
        else:
            N = 0
        A_tot = (A1+A2+A3+A4+(n_str_top+n_str_bot)*A_str)
        S1 = N/A_tot+ M_min*cx[p]/I_lst[check][p]
        S2 = N/A_tot 
        S3 = N/A_tot
        S4 = N/A_tot + M_max*(left - cx[p])/I_lst[check][p]
        S_str_top = N/(A_str*(n_str_top+n_str_bot)) + M_min*cx[p]/I_lst[check][p]
        S_str_bot = N/(A_str*(n_str_top+n_str_bot)) + M_max*(left - cx[p])/I_lst[check][p]
        stress1.append(S1)
        stress2.append(S2)
        stress3.append(S3)
        stress4.append(S4)
        stress5.append(S_str_top)
        stress6.append(S_str_bot)
        
    
        p+=1
    return stress1,stress2,stress3,stress4,stress5,stress6
        
def safety_margin(f,y):
    margin = []
    
    for i in f:
        if i>0:
            m = y/i
        elif i == 0:
            m = margin[-1]
        
        margin.append(m)
            
    return margin
    
safety1 = []
safety2 = []
safety3 = []
safety4 = []
safety5 = []
safety6 = []
safety7 = []
safety8 = []

check = 0
for tspar,tskin,nstrtop,nstrbot,astr,lstr in zip(t_sparl, t_skinl, n_str_topl, n_str_botl, A_strl,l_strl):
    
    s1,s2,s3,s4,s5,s6 = compressive(tspar, tskin, nstrtop, nstrbot, astr)
    s_crit = critical_stress1(I_lst[check], 12.815, (nstrtop+nstrbot-2)*A_str)

    m1 = safety_margin(s1,critical_stress)
    m2 = safety_margin(s2,critical_stress)
    m3 = safety_margin(s3,critical_stress)
    m4 = safety_margin(s4,critical_stress)
    m5 = safety_margin(s5,critical_stress)
    m6 = safety_margin(s6,critical_stress)
    
    loop = 0
    margin = []
    for i1 in s5:
        
        m7 = s_crit[loop]/i1
        margin.append(m7)
        
        loop+=1
        
  
    loop2 = 0
    margin1 = []
    for j1 in s6:
        
        m8 = s_crit[loop2]/j1
        margin1.append(m8)
        
        loop2+=1
        
    safety1.append(m1)
    safety2.append(m2)
    safety3.append(m3)
    safety4.append(m4)
    safety5.append(m5)
    safety6.append(m6)
    safety7.append(margin)
    safety8.append(margin1)
    
    
    check+=1
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
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,8)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Top skin panel Compressive Strength')

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
   
    plt.plot(span2[:5126], j[:5126], color = p,label=q)
    t+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)

plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper right')
plt.title('Front Spar Compressive Strength')

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
    
    plt.plot(span2[:5126], dababy[:5126], color = c1,label=k1)
    
    l1+=1
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)

plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper right')
plt.title('Rear Spar Compressive Strength')

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
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Bottom skin panel Compressive Strength')

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
   
    plt.plot(span2, jooo, color = p2,label=q2)
    t2+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Top stringers Compressive Strength')

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
   
    plt.plot(span2, joooo, color = p3,label=q3)
    t3+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Bottom stringers Compressive Strength')

plt.grid(True)

plt.show()
           
t4 = 0
for ok in safety7:

    if t4 == 0:
        p4 = 'red'
        q4 = 'Design option 1'
    elif t4 == 1:
        p4 = 'blue'
        q4 = 'Design option 2'
    elif t4 == 2:
        p4 = 'green'
        q4 = 'Design option 3'
   
    plt.plot(span2, ok, color = p4,label=q4)
    t4+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Top stringers Column Buckling')

plt.grid(True)

plt.show()
        
    
 
t5= 0
for ok2 in safety8:

    if t5 == 0:
        p5 = 'red'
        q5 = 'Design option 1'
    elif t5 == 1:
        p5 = 'blue'
        q5 = 'Design option 2'
    elif t5 == 2:
        p5 = 'green'
        q5 = 'Design option 3'
   
    plt.plot(span2, ok2, color = p5,label=q5)
    t5+=1
    
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.axhline(1,0,12.8125,color='orange',label='Requirement',linestyle='dotted')
plt.xlim(0,12.815)
plt.ylim(0,10.5)
plt.xlabel('y [m]')
plt.ylabel('Safety Margin')
plt.legend(loc='upper left')
plt.title('Bottom stringers Column Buckling')

plt.grid(True)

plt.show() 
    

