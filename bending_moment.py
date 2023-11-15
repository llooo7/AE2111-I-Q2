from scipy.integrate import quad
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
import aeroforces

L = int(12.815 * 1000)
xtab, ytab, x1tab, y1tab, x2tab, y2tab = [], [], [], [], [], []

def w(x):
    returnValue = 0
    for i in range(len(aeroforces.curveFit())):
        returnValue += x**(len(aeroforces.curveFit())-i) * aeroforces.curveFit()[i]
    #return 1/10000*(-0.3344*x**5 + 10.009*x**4 - 108.58*x**3 + 499.98*x**2 - 827.24*x + 4039.3)

def plot_w():
    for i in range(0, L):
        xtab.append(i / 1000)
        ytab.append(w(i / 1000))

def s(x):
    result, _ = quad(w, 0, x)
    return result


def s2(x):
    return s(x)-s_react

def plot_s():
    for i in range(0, L):
        x1tab.append(i / 1000)
        y1tab.append(s2(i / 1000))

def m(x):
    result, _ = quad(s2, 0, x)
    return result

def plot_m():
    for p in range(0, L):
        x2tab.append(p / 1000)
        y2tab.append(m(p / 1000) - m_react)

plot_w()
s_react = s(L/1000)
plot_s()
m_react = m(L/1000)
plot_m()

fig, ax = plt.subplots(2, 2, constrained_layout=True)
ax[0][0].set_title('Load distribution')
ax[0][1].set_title('Shear Stress')
ax[1][0].set_title('Bending Moment')
ax[0][0].plot(np.arange(0, 12.815, 0.1), [w(i) for i in np.arange(0, 12.815, 0.1)])
ax[0][1].plot(x1tab, y1tab)
ax[1][0].plot(x2tab, y2tab)
plt.show()
