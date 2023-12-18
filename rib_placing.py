import numpy as np
from Moment_of_inertia import area, chord_length
from matplotlib import pyplot as plt
from airfoil import data1, data2
from math import sin

aspect_ratio = 0.5
rib_placing = [0]
rib_weights = []
rib_thickness = 0.002
density = 2700
sweep_LE = 0.54837445


def plot_wingspars():
    xtab = np.arange(0, 12.815, 0.001)
    ytab = [area(chord_length(i), 1, 1)[4] for i in xtab]
    return ytab

def find_rib_placing(ytab):
    for i in np.arange(0, 12.815, 0.001):
        # Ensure that we have enough distance between ribs
        if i - rib_placing[-1] >= aspect_ratio * float(ytab[int(i*1000)]) * 2:
            rib_placing.append(round(i, 3))

def rib_weighting(rib_placing):
    airfoil_area = 0
    for i in range(0, len(data1) - 2, 2):
        x_upper1, y_upper1 = data1[i], data1[i + 1]
        x_upper2, y_upper2 = data1[i + 2], data1[i + 3]
        x_lower1, y_lower1 = data2[i], data2[i + 1]
        x_lower2, y_lower2 = data2[i + 2], data2[i + 3]
        trapezoid_area_upper = 0.5 * (x_upper2 - x_upper1) * (y_upper1 + y_upper2)
        trapezoid_area_lower = 0.5 * (x_lower2 - x_lower1) * (y_lower1 + y_lower2)
        airfoil_area += trapezoid_area_upper - trapezoid_area_lower
    airfoil_area = abs(airfoil_area)
    for i in rib_placing:
        rib_weights.append(round(airfoil_area*chord_length(i)*density*rib_thickness, 3))

def plot_wing():
    global y1tab, y2tab, y3tab, y4tab
    xtab = np.arange(0, 12.815, 0.001)
    y1tab = []
    y2tab = []
    y3tab = []
    y4tab = []
    for i in xtab:
        y1tab.append(4.523337094 - sin(sweep_LE)*i)
        y2tab.append(4.523337094 - sin(sweep_LE)*i - chord_length(i))
        y3tab.append(4.523337094 - sin(sweep_LE)*i - 0.9*chord_length(i))
        y4tab.append(4.523337094 - sin(sweep_LE)*i - 0.288*chord_length(i))
    


ytab = plot_wingspars()
find_rib_placing(ytab)
rib_weighting(rib_placing)
print(rib_placing)
print(rib_weights)

plot_wing()

fig, ax = plt.subplots()
"""
ax.plot(np.arange(0, 12.815, 0.001), ytab)
for j in range(len(rib_placing)):
    ax.vlines(rib_placing[j], ymin=0, ymax=ytab[int(rib_placing[j]*1000)])
ax.hlines(0, xmin=0, xmax=12.815)
ax.vlines(12.815, ymin=0, ymax=ytab[12814])
"""
ax.plot(np.arange(0, 12.815, 0.001), y1tab, "black")
ax.plot(np.arange(0, 12.815, 0.001), y2tab, "black")
ax.plot(np.arange(0, 12.815, 0.001), y3tab, "blue")
ax.plot(np.arange(0, 12.815, 0.001), y4tab, "blue")
for j in range(len(rib_placing)):
    ax.vlines(rib_placing[j], ymin=y3tab[int(rib_placing[j]*1000)], ymax=y4tab[int(rib_placing[j]*1000)])
ax.vlines(12.815, ymin=y2tab[int(12.815*1000-1)], ymax=y1tab[int(12.815*1000-1)], color="black")
ax.vlines(0, ymin=y2tab[int(0)], ymax=y1tab[int(0)], color="black")
ax.set_xlabel("Wingspan (m)")
ax.set_ylabel("Longitudinal axis (m)")
ax.set_title("Wing planform")
plt.show()
