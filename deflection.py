import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from Moment_of_inertia import *
from Internal_moment import momentmax,momentmin


h,i,j,k,l = np.polyfit(span, momentmax, 4)
p,q,r,s,t = np.polyfit(span, momentmin, 4)


def moment_maxfunction(y):
    return (h*y**4 + i*y**3 + j*y**2 +k*y + l)

def moment_minfunction(y):
    return ((p*y**4 + q*y**3 + r*y**2 + s*y**2 + t))

def f(y):
    return (moment_maxfunction(y)/(a*y**4 + b*y**3 + c*y**2 + d*y + e)/E)

def g(y):
    return(moment_minfunction(y)/(a*y**4 + b*y**3 + c*y**2 + d*y + e)/E)


def deflection(span,function):
    
    v = []
    
    for i in span:
        result_1, error_1 = integrate.quad(function, 0, i)
        result_2, error_2 = integrate.quad(lambda x: result_1, 0, i)
        v.append(result_2)
    
    return v 

V_max = deflection(span,f)
V_min = deflection(span,g)

plt.plot(span, V_max, color = 'r')
plt.plot(span,V_min, color = 'b')
plt.xlabel('y')
plt.ylabel('I')
plt.ylim(0,5)
plt.title('Span-wise moment of Inertia')

plt.show()


  