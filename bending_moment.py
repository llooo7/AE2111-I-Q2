import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate
import isa
import wing

data = [open("MainWing_a=0.00_v=10.00ms.txt"), open("MainWing_a=10.00_v=10.00ms.txt")]
aoas = [0,10]
ypos0, lcoe0, ypos1, lcoe1 = np.array([]), np.array([]), np.array([]), np.array([])

L = 12.815
wing_weight = 10
engine_weight = 2
engine_ypos= 0.4 * L
root_chord = 4.523337094
tip_chord = 1.355080022
Lambda_c2 = 0.453399865
thrust = 11
dz = 1

def chord(x):
    return (-root_chord+tip_chord)*x/L + root_chord


def wing_load_dist(x):
    wing_density = wing_weight/75.3316174
    return wing_density*chord(x)

def torque_dist(x):
    return -0.061807835*x + 1.130834274


i = 0
for datapoint in data:
    #dcoe.append([])
    for line in datapoint.readlines():
        items = line.split(' ')
        if float(items[0]) > 0:
            if i == 0:
                ypos0 = np.append(ypos0, float(items[0]))
                lcoe0 = np.append(lcoe0, float(items[3]))
                #dcoe[i].append(float(items[3]))
            elif i == 1:
                ypos1 = np.append(ypos1, float(items[0]))
                lcoe1 = np.append(lcoe1, float(items[3]))
                #dcoe[i].append(float(items[3]))
    datapoint.close()
    i += 1


def integrate_spline(ypos, lcoe):
    global x_load___, y_load___, x_load___other, y_load___other, x_shear___, y_shear___, x_moment___, y_moment___, x_torque___, y_torque___
    l0 = interpolate.InterpolatedUnivariateSpline(ypos,lcoe,k=5)
    x_load___, y_load___, x_load___other, y_load___other  = np.array([]), np.array([]), np.array([]), np.array([])
    
    
    for i in range(0, int(L*1000)):
        if i == int(engine_ypos*1000):
            y_load___ = np.append(y_load___, l0(i/1000) - engine_weight - wing_load_dist(i/1000))
            y_load___other = np.append(y_load___other, - engine_weight - wing_load_dist(i/1000))
        else:
            y_load___ = np.append(y_load___, l0(i/1000) - wing_load_dist(i/1000))
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
        y_Ndy___ = np.append(y_Ndy___, y_load___(i/1000)*torque_dist(i/1000))

    Ndy = interpolate.InterpolatedUnivariateSpline(x_Ndy___,y_Ndy___,k=5)
    torque = Ndy.antiderivative(1)

    x_torque___, y_torque___ = np.array([]), np.array([])
    for i in range(0, int(L*1000)):
        x_torque___ = np.append(x_torque___, i/1000)
        y_torque___ = np.append(y_torque___, torque(i/1000) - a)


def plot():
    fig, ax = plt.subplots(2, 4, constrained_layout=True)
    integrate_spline(ypos0, lcoe0)
    ax[0][0].plot(ypos0, lcoe0, "o")
    ax[0][0].plot(x_load___other, y_load___other, color="red", linestyle="--")
    ax[0][0].plot(x_load___, y_load___, label="Interpolated Spline 1")
    ax[0][1].plot(x_shear___, y_shear___, label="Shear stress 1")
    ax[0][2].plot(x_moment___, y_moment___, label="Bending moment 1")
    integrate_spline(ypos1, lcoe1)
    ax[1][0].plot(ypos1, lcoe1, "o")
    ax[1][0].plot(x_load___other, y_load___other, color="red", linestyle="--")
    ax[1][0].plot(x_load___, y_load___, label="Interpolated Spline 2")
    ax[1][1].plot(x_shear___, y_shear___, label="Shear stress 2")
    ax[1][2].plot(x_moment___, y_moment___, label="Bending moment 2")
    plt.show()

# MAIN    
plot()
