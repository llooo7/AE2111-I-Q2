import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from wing import *
from aeroforces import *
from isa import *


n = [1]
mass = [2]
v = [3] 
h = [4]


for n,mass,v,h in zip(n,mass,v,h):
    
    Weight = mass *9.81
    v = v*np.sqrt(1.225/h)
    q = 1/2*getDensity(h)*v**2
    CLd = n*Weight/(0.5*h*v**2*surface)
    CL0 = 0.108651
    CL10 = 0.372901
    factor = (CLd-CL0)/(CL10-CL0)
    alpha = np.arcsin(factor*np.sin(10/57.3))
    
    def lift_dist():
        return curveFit(v,alpha,h,normalAeroForce)

    
    
 
print(lift_dist())

    
    
    