import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate
import isa
import wing

data = [open("MainWing_a=0.00_v=10.00ms.txt"), open("MainWing_a=10.00_v=10.00ms.txt")]
aoas = [0,10]

ypos = [[],[]]
force = [[],[]]

i = 0
for datapoint in data:
    ypos.append([])
    force.append([])
    for line in datapoint.readlines():
        items = line.split(' ')
        if float(items[0]) > 0:
            ypos[i].append(float(items[0]))
            force[i].append(float(items[3]))
    datapoint.close()
    i += 1

f0 = sp.interpolate.interp1d(ypos[0],force[0],kind='quadratic',fill_value="extrapolate")
f10 = sp.interpolate.interp1d(ypos[1],force[1],kind='quadratic',fill_value="extrapolate")

def q(h,v,S,CL):
    return 0.5 * float(isa.getDensity(h)) * v * v * S * CL

def aeroForce(x,v = 10,a = 0,h = 0): #x = point on the wing, v = velocity, a = angle of attack, given PER UNIT SPAN 
    return q(h,v,wing.chord(x),f0(x)) + 1/10 * q(h,v,wing.chord(x),f10(x))

###Graph for debugging purposes
xVal = []
yVal = []
for i in range(int(10 * wing.span /2)):
    xVal.append(i/10)
    yVal.append(aeroForce(i/10))
plt.plot(xVal,yVal)
plt.show()