import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate

data = open("MainWing_a=0.00_v=10.00ms.txt")
ypos = []
force = []
count = 0
M = 0.77
a = 343 
v = M*a
rho = 1.225

for line in data.readlines():
    count += 1
    items = line.split(' ')
    #print(items)
    if float(items[0]) > 0:
        ypos.append(float(items[0]))
        force.append(float(items[3]))

data.close()
f = sp.interpolate.interp1d(ypos,force,kind='quadratic',fill_value="extrapolate")

#def dynpress(c_l,vel):
#interpolates as linear between known datapoints
def force(x): 
    return f(abs(x))

print(force(12))