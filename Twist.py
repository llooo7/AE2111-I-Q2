import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from Moment_of_inertia import *
from Internal_torsion import torquemax,torquemin


G =26*10**9


h,i,j,k,l,m,n,o = np.polyfit(span,torquemax,7)
p,q,r,s,t,u,v1,w1 = np.polyfit(span, torquemin, 7)


def torsion_max(y):
    return (h*y**7 + i*y**6 + j*y**5 +k*y**4 + l*y**3 + m*y**2 + n*y + o)

def torsion_min(y):
    return (p*y**7 + q*y**6 + r*y**5 + s*y**4 + t*y**3 + u*y**2 + v1*y + w1)

def torsional_constant(n_str_top,n_str_bottom,A_str,t_spar,t_skin):
    
    chords = chord_length(span)
    J = []
    for i in chords:
        
        A1,A2,A3,A4,height,left,right,bottom = area(i,t_spar,t_skin)
        
        A = 0.5*(left+right)*height+A_str*(n_str_top+n_str_bottom)
        
        l = (left + right)/t_spar + (height + bottom)/t_skin
        
        j = 4*A**2/l
        
        J.append(j)
        
    return J
        
        
J = torsional_constant(n_str_top,n_str_bottom,A_str,t_spar, t_skin)


v,w,x,y1,z = np.polyfit(span,J,4)


def f(y):
    return (torsion_max(y)/(v*y**4 + w*y**3 + x*y**2 + y1*y + z)/G)

def g(y):
    return (torsion_min(y)/(v*y**4 + w*y**3 + x*y**2 + y1*y + z)/G)

def twist(span,function):
    
    theta = []
    for i in span:
        result_1, error_1 = integrate.quad(function, 0, i)
        theta.append(result_1)
        
    return theta


Theta_max = np.array(twist(span,f))*180/np.pi
Theta_min = np.array(twist(span,g))*180/np.pi


plt.plot(span, Theta_max,color = 'r',label='n = 2.5')
plt.plot(span, Theta_min, color = 'b',label='n = -1')
print(J[0])
plt.xlabel('y [m]')
plt.ylabel('Twist [deg]')
plt.title('Span-wise Wing Twist for n = -1 and n = 2.5')
plt.grid(True)
plt.ylim(-11,11)
plt.axhline(10,0,12.8125,color='orange',label='Requirement')
plt.axhline(-10,0,12.8125,color='orange')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.legend(loc='lower left')

plt.show()