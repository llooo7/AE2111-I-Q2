import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from math import cos
from scipy import interpolate
import isa
import wing
import aeroforces

data = [open("MainWing_a=0.00_v=10.00ms.txt"), open("MainWing_a=10.00_v=10.00ms.txt")]
aoas = [0,10]
ypos0, lcoe0, ypos1, lcoe1, dcoe0, dcoe1 = np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([])

# Aircraft parameters
def chord(x):
    return (-root_chord+tip_chord)*x/L + root_chord
L = 12.815
wing_weight = 2387.38 * 9.80655 + 2635*9.80655
engine_weight = 2079 * 9.80655
engine_ypos= 0.4 * L
root_chord = 4.523337094
tip_chord = 1.355080022
Lambda_c2 = 0.453399865
thrust = 96500
dz = 0.05*chord(engine_ypos)+1.35/2

# Read files
i = 0
for datapoint in data:
    #dcoe.append([])
    for line in datapoint.readlines():
        items = line.split(' ')
        if float(items[0]) > 0:
            if i == 0:
                ypos0 = np.append(ypos0, float(items[0]))
                lcoe0 = np.append(lcoe0, float(items[3]))
                dcoe0 = np.append(dcoe0, float(items[3]))
            elif i == 1:
                ypos1 = np.append(ypos1, float(items[0]))
                lcoe1 = np.append(lcoe1, float(items[3]))
                dcoe1 = np.append(dcoe1, float(items[3]))
    datapoint.close()
    i += 1
# Load functions

def wing_load_dist(x):
    wing_density = wing_weight/75.3316174
    return wing_density*chord(x)

def torque_dist(x):
    return -0.061807835*x + 1.130834274

def t(x):
    return x

def normal_force(x, a):
    l_0 = interpolate.InterpolatedUnivariateSpline(ypos0,lcoe0,k=5)
    l_10 = interpolate.InterpolatedUnivariateSpline(ypos1,lcoe1,k=5)
    d_0 = interpolate.InterpolatedUnivariateSpline(ypos0,dcoe0,k=5)
    d_10 = interpolate.InterpolatedUnivariateSpline(ypos1,dcoe1,k=5)
    #return ((l_0(x) + l_10(x))/10*a + l_0(x)) / np.cos(a / 57.2958)
    return np.sqrt(pow((l_0(x) + a * 1/10 * l_10(x)) / np.cos(a / 57.2958),2) + pow((d_0(x) + a * 1/10 * d_10(x)) / np.cos(a / 57.2958),2))

def integrate_spline(n=1, mass=320000, v=10, h=1, a=0):
    global x_load___, y_load___, x_load___other, y_load___other, x_shear___, y_shear___, x_moment___, y_moment___, x_torque___, y_torque___
    x_load___, y_load___, x_load___other, y_load___other  = np.array([]), np.array([]), np.array([]), np.array([])
    
    
    for i in range(0, int(L*1000)):
        if i == int(engine_ypos*1000):
            y_load___ = np.append(y_load___, float(isa.getDensity(h))*normal_force(i/1000, a)/2*v*v*chord(i/1000) + n*(- engine_weight - wing_load_dist(i/1000)))
            #y_load___ = np.append(y_load___, aeroforces.normalAeroForce(i/1000, v, a, h) + n*(- engine_weight - wing_load_dist(i/1000)))
            y_load___other = np.append(y_load___other, - engine_weight - wing_load_dist(i/1000))
        else:
            y_load___ = np.append(y_load___, float(isa.getDensity(h))*normal_force(i/1000, a)/2*v*v*chord(i/1000) + n*(- wing_load_dist(i/1000)))
            #y_load___ = np.append(y_load___, aeroforces.normalAeroForce(i/1000, v, a, h) + n*(- engine_weight - wing_load_dist(i/1000)))
            y_load___other = np.append(y_load___other, - wing_load_dist(i/1000))
        x_load___ = np.append(x_load___, i/1000)

        x_load___other = np.append(x_load___other, i/1000)


    load = interpolate.InterpolatedUnivariateSpline(x_load___,y_load___,k=5)
    shear = load.antiderivative(1)

    x_shear___, y_shear___ = np.array([]), np.array([])
    for i in range(0, int(L*1000)):
        x_shear___ = np.append(x_shear___, i/1000)
        y_shear___ = np.append(y_shear___, shear(i/1000) - shear(L))

    shear0 = interpolate.InterpolatedUnivariateSpline(x_shear___,y_shear___,k=5)
    moment = shear0.antiderivative(1)

    x_moment___, y_moment___ = np.array([]), np.array([])
    for i in range(0, int(L*1000)):
        x_moment___ = np.append(x_moment___, i/1000)
        y_moment___ = np.append(y_moment___, moment(i/1000) - moment(L))

    x_Ndy___, y_Ndy___ = np.array([]), np.array([])
    for i in range(0, int(L*1000)):
        x_Ndy___ = np.append(x_Ndy___, i/1000)
        #y_Ndy___ = np.append(y_Ndy___, load(i/1000)*torque_dist(i/1000) + t(i/1000))
        y_Ndy___ = np.append(y_Ndy___, aeroforces.c4moment(i/1000, 0, h)*v*v/2*chord(i/1000))

    Ndy = interpolate.InterpolatedUnivariateSpline(x_Ndy___,y_Ndy___,k=5)
    torque = Ndy.antiderivative(1)

    x_torque___, y_torque___ = np.array([]), np.array([])
    for i in range(0, int(L*1000)):
        x_torque___ = np.append(x_torque___, i/1000)
        if i <= int(engine_ypos*1000):
            y_torque___ = np.append(y_torque___, torque(i/1000) -thrust*dz*cos(Lambda_c2) - torque(L))
        else:
            y_torque___ = np.append(y_torque___, torque(i/1000) - torque(L))


def plot(n, mass, v, h, a):
    fig, ax = plt.subplots(1, 4, constrained_layout=True)
    """
    integrate_spline(ypos0, lcoe0, n, mass, v, h, 0)
    #ax[0][0].plot(ypos0, lcoe0, "o")
    #ax[0][0].plot(x_load___other, y_load___other, color="red", linestyle="--")
    ax[0][0].set_ylabel("Angle of attack 0º")
    ax[0][0].set_title("Load distribution diagrams")
    ax[0][0].plot(x_load___, y_load___, label="Interpolated Spline 1")
    ax[0][1].set_title("Shear diagrams")
    ax[0][1].plot(x_shear___, y_shear___, label="Shear stress 1")
    ax[0][2].set_title("Bending moment diagrams")
    ax[0][2].plot(x_moment___, y_moment___, label="Bending moment 1")
    ax[0][3].set_title("Torque diagrams")
    ax[0][3].plot(x_torque___, y_torque___, label="Torque 1")
    integrate_spline(ypos1, lcoe1, n, mass, v, h, 10)
    #ax[1][0].plot(ypos1, lcoe1, "o")
    #ax[1][0].plot(x_load___other, y_load___other, color="red", linestyle="--")
    ax[1][0].set_ylabel("Angle of attack 10º")
    ax[1][0].plot(x_load___, y_load___, label="Interpolated Spline 2")
    ax[1][1].plot(x_shear___, y_shear___, label="Shear stress 2")
    ax[1][2].plot(x_moment___, y_moment___, label="Bending moment 2")
    ax[1][3].plot(x_torque___, y_torque___, label="Torque 2")
    """
    integrate_spline(n, mass, v, h, a)
    #ax[1][0].plot(ypos1, lcoe1, "o")
    #ax[1][0].plot(x_load___other, y_load___other, color="red", linestyle="--")
    ax[0].set_title("Load distribution diagram")
    ax[0].plot(x_load___, y_load___, label="Interpolated Spline 2")
    ax[1].set_title("Shear stress diagram")
    ax[1].plot(x_shear___, y_shear___, label="Shear stress 2")
    ax[2].set_title("Bending moment diagram")
    ax[2].plot(x_moment___, y_moment___, label="Bending moment 2")
    ax[3].set_title("Torque diagram")
    ax[3].plot(x_torque___, y_torque___, label="Torque 2")
    plt.show()
    return y_load___, y_shear___, y_moment___, y_torque___

# MAIN    

n = 1
mass = 1
v = 50
h = 1
a = 5

plot(n, mass, v, h, a)
