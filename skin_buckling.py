from math import pi
from matplotlib import pyplot as plt
import numpy as np
import Internal_moment

poisson = 0.3
kc = 5
E = 69*(10**9)
t_b = 0.002

M_x = Internal_moment.momentmin
M_y = 0
I_xx = 2
I_yy = 1
I_xy = 0
x = 1
y = 1

def skin_buckling_crit(poisson, kc, E, t_b):
    return (((pi**2*kc*E)/(12*(1-poisson**2)))*(t_b**2))


def skin_stress(M_x, I_xx, y):
    return (((M_x)*y)/(I_xx))

def safety_margin(a, b):
    return (a/b)

def plot_skin_buckling(poisson, kc, E, t_b, M_x, M_y, I_xx, I_yy, I_xy, x, y):
    fig, ax = plt.subplots()
    ytab = [safety_margin(skin_buckling_crit(poisson, kc, E, t_b), skin_stress(M_x, M_y, I_xx, I_yy, I_xy, x/1000, y)) for x in range(1, 12815)]
    xtab = np.array([])
    for i in range (1, 12815):
        xtab = np.append(xtab, i/1000)
    ax.plot(xtab, ytab)
    plt.show()
    
plot_skin_buckling(poisson, kc, E, t_b, M_x, M_y, I_xx, I_yy, I_xy, x,y)
