from scipy.integrate import quad
from matplotlib import pyplot as plt

L = 28 * 10
x1tab, y1tab, x2tab, y2tab = [], [], [], []

def integrate(func, j):
    return quad(func, j, L)

def w(x):
    return 10

def plot_w():
    for i in range(0, L):
        x1tab.append(i / 10)
        y1tab.append((w(i / 10))) 

def s(x):
    return integrate(w, 0)[0] - integrate(w, x)[0]

def s2(x):
    return s(x)-s(L/10)

def plot_s():
    for i in range(0, L):
        x1tab.append(i / 10)
        y1tab.append((s2(i / 10))) 

def m(o):
    return integrate(s2, 0)[0] - integrate(s2, o)[0]

def plot_m():
    for p in range(0, L):
        x2tab.append(p / 10)
        y2tab.append((m(p / 10)-m(L/10)))

plot_s()
plot_m()
fig, ax = plt.subplots(2, 2, layout="constrained")
ax[0][0].set_title('Shear Stress')
ax[0][1].set_title('Bending Moment')
ax[0][0].plot(x1tab, y1tab)
ax[0][1].plot(x2tab, y2tab)
plt.show()  
