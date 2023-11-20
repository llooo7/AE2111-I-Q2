import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from wing import *
from aeroforces import *
from isa import *
from bending_moment import *


n = [1,2,3,4]
mass = [2,3,4,5]
v = [3,4,5,6] 
h = [4,5,6,7]


for n,mass,v,h in zip(n,mass,v,h):
    
    Weight = mass*9.81
    v = v*np.sqrt(1.225/h)
    q = 1/2*getDensity(h)*v**2
    CLd = n*Weight/(0.5*h*v**2*surface)
    CL0 = 0.383907
    CL10 = 1.2045817
    factor = (CLd-CL0)/(CL10-CL0)
    alpha = np.arcsin(factor*np.sin(10/57.3))*57.3
    
    a,b,c,d = plot(n,mass,v,h,alpha)

print(a)
    
    
    
    