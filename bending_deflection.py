import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate
import isa
import wing
import aeroforces
from Moment_of_inertia import moment_of_inertia, E
import bending_moment

n = 1
mass = 1
v = 260
h = 3000
a = 10

t_spar = 0.005
t_skin = 0.002
A_str = 0.0008
n_str = 7


def deflection():
    moments = bending_moment.plot(n, mass, v, h, a)
    x_vals, bending_moments = moments[4], moments[2]

    M = interpolate.InterpolatedUnivariateSpline(x_vals, bending_moments/E/moment_of_inertia(A_str,n_str,t_spar,t_skin),k=5)
    v1_deflection = M.antiderivative(1)

    x_v1___, y_v1___ = np.array([]), np.array([])
    for i in range(0, int(12.815*1000)):
        x_v1___ = np.append(x_v1___, i/1000)
        y_v1___ = np.append(y_v1___, v1_deflection(i/1000) - v1_deflection(0))

    v1_deflection___ = interpolate.InterpolatedUnivariateSpline(x_v1___,y_v1___,k=5)
    v_deflection = v1_deflection___.antiderivative(1)

    fig, ax = plt.subplots()
    y_vals2 = [v_deflection(x) for x in x_vals]
    plt.axhline(y=0.15*12.815, color='red', linestyle='-', linewidth=0.8)  
    ax.plot(x_vals, y_vals2)
    plt.show()
    return v_deflection

#plot_deflection(bending_moment.plot(n, mass, v, h, a)[4])

deflection()
