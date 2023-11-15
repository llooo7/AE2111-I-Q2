import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate
import isa
import wing

data = [open("MainWing_a=0.00_v=10.00ms.txt"), open("MainWing_a=10.00_v=10.00ms.txt")]
aoas = [0,10]

ypos = [[],[]]  #spanwise position from center
lcoe = [[],[]]  #lift coefficient
#dcoe = [[],[]]  #drag coefficient, probably not relevant

i = 0
for datapoint in data:
    ypos.append([])
    lcoe.append([])
    #dcoe.append([])
    for line in datapoint.readlines():
        items = line.split(' ')
        if float(items[0]) > 0:
            ypos[i].append(float(items[0]))
            lcoe[i].append(float(items[3]))
            #dcoe[i].append(float(items[3]))
    datapoint.close()
    i += 1

l0 = sp.interpolate.interp1d(ypos[0],lcoe[0],kind='quadratic',fill_value="extrapolate")
l10 = sp.interpolate.interp1d(ypos[1],lcoe[1],kind='quadratic',fill_value="extrapolate")

def pgApprox(h,v):
    return np.sqrt()    

def q(h,v,S,CL):
    return 0.5 * float(isa.getDensity(h)) * v * v * S * CL

def normalAeroForce(x,v = 10,a = 1.75,h = 0): #x = point on the wing, v = velocity, a = angle of attack, given PER UNIT SPAN 
    return (q(h,v,wing.chord(x),l0(x)) + 1/10 * q(h,v,wing.chord(x),l10(x))) / np.cos(a / 57.2958)
    #return (q(h,v,wing.chord(x),l0(x)) + 1/10 * q(h,v,wing.chord(x),l10(x)))

def curveFit(v = 10,a = 1.75,h = 0):
    xVal = []
    yVal = []
    for i in range(int(10 * wing.span /2)):
        xVal.append(i/10)
        yVal.append(normalAeroForce(i/10))
    
    return np.polyfit(xVal,yVal,3)
  #  print(np.polyfit(xVal,yVal,3))
  #  plt.plot(xVal,yVal)
  #  plt.show()