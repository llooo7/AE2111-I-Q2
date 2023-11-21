import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from Moment_of_inertia import *
from Internal_moment import *


def momentmax(y):
    
    a,b,c,d,e,p,q,r,s,t = moment_fit()
    return (a*y**4+b*y**3+c*y**2+d*y+e)

def momentmin(y):
    
    a,b,c,d,e,p,q,r,s,t = moment_fit()
    return (p*y**4+q*y**3+r*y**2+s*y+t)


def f(y):
    return (momentmax(y)/(a*y**4 + b*y**3 + c*y**2 + d*y + e)/E)

def g(y):
    return (momentmin(y)/(a*y**4 + b*y**3 + c*y**2 + d*y + e)/E)

def deflection(span,function):
    
    v = []
    
    for i in span:
        result_1, error_1 = integrate.quad(function, 0, i)
        result_2, error_2 = integrate.quad(lambda x: result_1, 0, i)
        v.append(result_2)
    
    return v 

V_max = deflection(span,f)
V_min = deflection(span,g)

plt.plot(span, V_max)
plt.plot(span, V_min)
plt.xlabel('y')
plt.ylabel('I')
plt.title('Span-wise moment of Inertia')

plt.show()


  