import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from Moment_of_inertia import *
from Internal_torsion import torquemax,torquemin


G =26*10**9


h,i,j,k,l = np.polyfit(span,torquemax,4)
m,n,o,p,u = np.polyfit(span, torquemin, 4)


def torsion_max(y):
    return (h*y**4 + i*y**3 + j*y**2 +k*y + l)

def torsion_min(y):
    return (m*y**4 + n*y**3 + o*y**2 + p*y**2 + u)


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


p,q,r,s,t = np.polyfit(span,J,4)


def f(y):
    return (torsion_max(y)/(p*y**4 + q*y**3 + r*y**2 + s*y + t)/G)

def g(y):
    return (torsion_min(y)/(p*y**4 + q*y**3 + r*y**2 + s*y + t)/G)

def twist(span,function):
    
    theta = []
    for i in span:
        result_1, error_1 = integrate.quad(function, 0, i)
        theta.append(result_1)
        
    return theta


Theta_max = np.array(twist(span,f))*180/np.pi
Theta_min = np.array(twist(span,g))*180/np.pi

plt.plot(span, Theta_max)
plt.plot(span, Theta_min)
plt.xlabel('y')
plt.ylabel('I')
plt.title('Span-wise Wing Twist')
plt.grid(True)
plt.ylim(-2,10)

plt.show()