import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate
import isa
import wing

data = [open("MainWing_a=0.00_v=10.00ms.txt"), open("MainWing_a=10.00_v=10.00ms.txt")]
aoas = [0,10]
ypos0 = np.array([])
lcoe0 = np.array([])
ypos1 = np.array([])
lcoe1 = np.array([])

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
    global x_shear___, y_shear___, x_moment___, y_moment___
    l0 = interpolate.InterpolatedUnivariateSpline(ypos,lcoe,k=3)
    shear = l0.antiderivative(1)

    x_shear___ = np.array([])
    y_shear___ = np.array([])
    for i in range(0, 12815):
        x_shear___ = np.append(x_shear___, i/1000)
        y_shear___ = np.append(y_shear___, shear(i/1000) - shear(12.815))

    shear0 = interpolate.InterpolatedUnivariateSpline(x_shear___,y_shear___,k=3)
    moment = shear0.antiderivative(1)

    x_moment___ = np.array([])
    y_moment___ = np.array([])
    for i in range(0, 12815):
        x_moment___ = np.append(x_moment___, i/1000)
        y_moment___ = np.append(y_moment___, moment(i/1000) - moment(12.815))


def plot():
    fig, ax = plt.subplots(2, 3, constrained_layout=True)
    integrate_spline(ypos0, lcoe0)
    ax[0][0].plot(ypos0, lcoe0, "o")
    ax[0][0].plot(ypos0, lcoe0, "--", label="Interpolated Spline 1")
    ax[0][1].plot(x_shear___, y_shear___, label="Shear stress 1")
    ax[0][2].plot(x_moment___, y_moment___, label="Bending moment 1")
    integrate_spline(ypos1, lcoe1)
    ax[1][0].plot(ypos1, lcoe1, "o")
    ax[1][0].plot(ypos1, lcoe1, "--", label="Interpolated Spline 2")
    ax[1][1].plot(x_shear___, y_shear___, label="Shear stress 2")
    ax[1][2].plot(x_moment___, y_moment___, label="Bending moment 2")
    plt.show()
plot()
