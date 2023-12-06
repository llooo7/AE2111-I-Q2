from math import pi
from matplotlib import pyplot as plt
import numpy as np
from Internal_moment import momentmin
from Moment_of_inertia import moment_of_inertia, area, chord_length

poisson = 0.3
kc = 5
E = 68.94757*10**9
A_str = 0.0005
n_str_top = 2
n_str_bottom =  2
t_spar = 0.004
t_skin = 0.002
t_str = 0.0005
l_str = 0.001

M_x = momentmin
I_xx = moment_of_inertia(A_str,n_str_top,n_str_bottom,t_spar,t_skin,t_str,l_str)[0]
span = np.arange(0,12.815,0.001)
a,b,c,d,e = np.polyfit(span,I_xx,4)
I_xx = a*span**4 + b*span**3 + c*span**2 + d*span + e


z = 1 #insert height of the skin panel

def t_b(y):
    return (t_skin/(area(chord_length(y), 1, 1)[4]))


def skin_buckling_crit(poisson, kc, E, t_b):
    return (((pi**2*kc*E)/(12*(1-poisson**2)))*(t_b**2))


def skin_stress(M_x, I_xx, z):
    return (((M_x)*z)/(I_xx))

def safety_margin(a, b):
    return (a/b)

def plot_skin_buckling(poisson, kc, E, t_b, M_x, I_xx, z):
    fig, ax = plt.subplots()
    ytab = [safety_margin(skin_buckling_crit(poisson, kc, E, t_b(y/1000)), skin_stress(M_x(y/1000), I_xx(y/1000), z)) for y in range(1, 12815)]
    xtab = np.array([])
    for i in range (1, 12815):
        xtab = np.append(xtab, i/1000)
    ax.plot(xtab, ytab)
    plt.show()
    
plot_skin_buckling(poisson, kc, E, t_b, M_x, I_xx, z)
