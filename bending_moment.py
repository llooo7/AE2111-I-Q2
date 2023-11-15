from scipy.integrate import quad
from matplotlib import pyplot as plt

L = 28 * 100


def w(x):
    return 100


def integrate(func, j):
    return quad(func, j, L)


x1tab, y1tab, x2tab, y2tab = [], [], [], []


def s(x):
    return integrate(w, 0)[0] - integrate(w, x)[0]

def s2(x):
    return s(x)-s(L/100)

def plot_s():
    for i in range(0, L):
        x1tab.append(i / 100)
        y1tab.append((s2(i / 100)))


def m(o):
    return integrate(s2, 0)[0] - integrate(s2, o)[0]


def plot_m():
    for p in range(0, L):
        x2tab.append(p / 100)
        y2tab.append((m(p / 100)-m(L/100)))


plot_s()
plot_m()
fig, (ax0, ax1) = plt.subplots(1, 2)
ax0.plot(x1tab, y1tab, color="black", label='Shear Stress')
ax1.plot(x2tab, y2tab, color="red", label='Bending Moment')
# plt.ylim(-0.5, 0.5)
plt.title("Bending moment diagram")

plt.show()
