import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from Moment_of_inertia import *
from Internal_moment import momentmax,momentmin


h,i,j,k,l,m = np.polyfit(span, momentmax, 5)
p,q,r,s,t,u = np.polyfit(span, momentmin, 5)


def moment_maxfunction(y):
    return (h*y**5 + i*y**4 + j*y**3 +k*y**2 + l*y + m)

def moment_minfunction(y):
    return (p*y**5 + q*y**4 + r*y**3 + s*y**2 + t*y + u)

def f(y):
    return (-moment_maxfunction(y)/(a*y**4 + b*y**3 + c*y**2 + d*y + e)/E)

def g(y):
    return (-moment_minfunction(y)/(a*y**4 + b*y**3 + c*y**2 + d*y + e)/E)


def deflection(span,function):
    
    v = []
    
    for i in span:
        result_1, error_1 = integrate.quad(function, 0, i)

        result_2, error_2 = integrate.quad(lambda x: result_1, 0, i)
        
        v.append(result_2)
   
    return v 



V_max = deflection(span,f)
V_min = deflection(span,g)

plt.plot(span,V_max,color = 'r')
plt.plot(span,V_min, color = 'b')
plt.plot(span,[0,3.844],color = 'o')
plt.plot(span,[0,-3.844], color = 'o')
plt.xlabel('y [m]')
plt.ylabel('Deflection [m]')
plt.title('Deflection in [m] for n = -1 and n = 2.5')
plt.ylim(-3,3)
plt.xlim(0,14)
plt.grid(True)

plt.show()


  