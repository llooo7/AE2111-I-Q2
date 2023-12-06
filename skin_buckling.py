from math import pi
from matplotlib import pyplot as plt
import numpy as np
from Internal_moment import momentmin
from Moment_of_inertia import moment_of_inertia, area, chord_length

poisson = 0.3
kc = 5
E = 69*(10**9)
t_b = 0.002
A_str = 1
n_str_top = 1
n_str_bottom =  1
t_spar = 1
t_skin = 1
t_str = 1
h_str = 1

M_x = momentmin
I_xx = moment_of_inertia(A_str,n_str_top,n_str_bottom,t_spar,t_skin,t_str,h_str)
y = 1 #insert height of the skin panel

def t_b(y):
    return (t_skin/(area(chord_length(y), 1, 1)[4]))


def skin_buckling_crit(poisson, kc, E, t_b):
    return (((pi**2*kc*E)/(12*(1-poisson**2)))*(t_b**2))


def skin_stress(M_x, I_xx, y):
    return (((M_x)*y)/(I_xx))

def safety_margin(a, b):
    return (a/b)

def plot_skin_buckling(poisson, kc, E, t_b, M_x, I_xx, y):
    fig, ax = plt.subplots()
    ytab = [safety_margin(skin_buckling_crit(poisson, kc, E, t_b(x)), skin_stress(M_x(x), I_xx(x), y)) for x in range(1, 12815)]
    xtab = np.array([])
    for i in range (1, 12815):
        xtab = np.append(xtab, i/1000)
    ax.plot(xtab, ytab)
    plt.show()
    
plot_skin_buckling(poisson, kc, E, t_b, M_x, I_xx, y)
