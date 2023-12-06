from math import pi
from matplotlib import pyplot as plt
import numpy as np

poisson = 0.3
kc = 5
E = 69*(10**9)
t_b = 0.002

M_x = 1
M_y = 1
I_xx = 2
I_yy = 1
I_xy = 1
x = 1
y = 1

def skin_buckling_crit(poisson, kc, E, t_b):
    return (((pi**2*kc*E)/(12*(1-poisson**2)))*(t_b**2))


def skin_stress(M_x, M_y, I_xx, I_yy, I_xy, x, y):
    return (((M_x*I_yy-M_y*I_xy)*y+(M_y*I_xx-M_x*I_xy)*x)/(I_xx*I_yy-I_xy**2))

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
print(skin_stress(M_x = 1, M_y = 1,I_xx = 2, I_yy = 1, I_xy = 1,x = 1/1000,y = 1))
plot_skin_buckling(poisson = 0.3, kc = 5, E = 69*(10**9), t_b = 0.002, M_x = 1, M_y = 1,I_xx = 2, I_yy = 1, I_xy = 1,x = 1,y = 1)
