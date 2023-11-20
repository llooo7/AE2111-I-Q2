import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from moment_of_inertia import *



G =26*10**9

def torsion(y):
    return (500*y**2 + 300*y + 500)


def torsional_constant(n_str,A_str,t_spar,t_skin):
    
    chords = chord_length(span)
    J = []
    for i in chords:
        
        A1,A2,A3,A4,height,left,right,bottom = area(i,t_spar,t_skin)
        
        A = 0.5*(left+right)*height+A_str*n_str
        
        l = (left + right)/t_spar + (height + bottom)/t_skin
        
        j = 4*A**2/l
        
        J.append(j)
        
    return J
        
        
J = torsional_constant(n_str,A_str,t_spar, t_skin)


p,q,r,s,t = np.polyfit(span,J,4)


def f(y):
    return (torsion(y)/(p*y**4 + q*y**3 + r*y**2 + s*y + t)/G)

def twist(span):
    
    theta = []
    for i in span:
        result_1, error_1 = integrate.quad(f, 0, i)
        theta.append(result_1)
        
    return theta


Theta = twist(span)

a,b,c,d,e,f,g,h = np.polyfit(span,Theta,7)

Theta_2 = a*span**7+ b*span**6 + c*span**5 + d*span**4 + e*span**3 + f*span**2 + g*span + h






plt.plot(span, Theta)
plt.plot(span, Theta_2)
plt.xlabel('y')
plt.ylabel('I')
plt.title('Span-wise Wing Twist')

plt.show()