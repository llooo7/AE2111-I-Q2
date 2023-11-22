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
c4m = [[],[]]  #drag coefficient, probably not relevant
dcoe = [[],[]]

i = 0
for datapoint in data:
    ypos.append([])
    lcoe.append([])
    c4m.append([])
    for line in datapoint.readlines():
        items = line.split(' ')
        if float(items[0]) > 0:
            ypos[i].append(float(items[0]))
            lcoe[i].append(float(items[3]))
            c4m[i].append(float(items[7]))
            dcoe[i].append(float(items[5]))
    datapoint.close()
    i += 1

l0 = sp.interpolate.interp1d(ypos[0],lcoe[0],kind='quadratic',fill_value="extrapolate")
l10 = sp.interpolate.interp1d(ypos[1],lcoe[1],kind='quadratic',fill_value="extrapolate")

c40 = sp.interpolate.interp1d(ypos[0],c4m[0],kind='quadratic',fill_value="extrapolate")
c410 = sp.interpolate.interp1d(ypos[1],c4m[1],kind='quadratic',fill_value="extrapolate")

d0 = sp.interpolate.interp1d(ypos[0],dcoe[0],kind='quadratic',fill_value="extrapolate")
d10 = sp.interpolate.interp1d(ypos[1],dcoe[1],kind='quadratic',fill_value="extrapolate")   

def q(h,v,S,CL):
    a = np.sqrt(1.4 * 287 * isa.getTemp(h))
    pg = 1/np.sqrt(1 - pow(v/a,2))
    return 0.5 * float(isa.getDensity(h)) * v * v * S * CL * pg

def specialAbs(l,d, angle):
    return np.cos(angle / 57.2958) * l + np.sin(angle / 57.2958) * d
    #return np.sqrt(pow(l,2) + pow(d,2))

cl0 = 0.3839
cl10 = 1.2046

def aoaNormalize(val0,val1,angle,cld):
    return val0 + ((cld - cl0)/(cl10 - cl0)*(val1 - val0))
    #return ( val0 + angle * 0.1 * val1 ) / np.cos(a / 57.2958)

def normalAeroForce(x,v = 10,a = 1.75,h = 0,cld = 0.328): #x = point on the wing, v = velocity, a = angle of attack, given PER UNIT SPAN 
    normalLift = aoaNormalize(q(h,v,wing.chord(x),l0(x)), q(h,v,wing.chord(x),l10(x)),a,cld)
    normalDrag = aoaNormalize(q(h,v,wing.chord(x),d0(x)),q(h,v,wing.chord(x),d10(x)),a,cld) 

    return specialAbs(normalLift,normalDrag,a) 

    return specialAbs(normalLift,normalDrag,a)

def c4moment(x,v = 10,a = 1.75,h = 0): #x = point on the wing, v = velocity, a = angle of attack, given PER UNIT SPAN 
    return q(h,v,wing.chord(x),c40(x)) + a * 1/10 * q(h,v,wing.chord(x),c410(x))

def curveFit(v = 10,a = 1.75,h = 0, function = normalAeroForce, plot = False):
    xVal = []
    yVal = []
    for i in range(int(10 * wing.span /2)):
        xVal.append(i/10)
        yVal.append(function(i/10))
    
    return np.polyfit(xVal,yVal,3)
    print(np.polyfit(xVal,yVal,3))
    plt.plot(xVal,yVal)
    plt.show()


