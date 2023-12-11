import numpy as np
from Moment_of_inertia import area, chord_length
from matplotlib import pyplot as plt

aspect_ratio = 0.5
rib_placing = [0.001]

def plot_wingspars():
    xtab = np.arange(0, 12.815, 0.001)
    ytab = [area(chord_length(i), 1, 1)[4] for i in xtab]
    return ytab

def find_rib_placing(ytab):
    for i in np.arange(0, 12.815, 0.001):
        # Ensure that we have enough distance between ribs
        if i - rib_placing[-1] >= aspect_ratio * float(ytab[int(i*1000)]) * 2:
            rib_placing.append(i)

ytab = plot_wingspars()
find_rib_placing(ytab)
print(rib_placing)

fig, ax = plt.subplots()
ax.plot(np.arange(0, 12.815, 0.001), ytab)
for j in range(len(rib_placing)):
    ax.vlines(rib_placing[j], ymin=0, ymax=ytab[int(rib_placing[j]*1000)])
ax.hlines(0, xmin=0, xmax=12.815)
ax.vlines(12.815, ymin=0, ymax=ytab[12814])
plt.show()
