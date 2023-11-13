import os
import matplotlib.pyplot as plt
import numpy as np

data = open("MainWing_a=0.00_v=10.00ms.txt")
ypos = []
force = []
ints = []
count = 0

for line in data.readlines():
    count += 1
    items = line.split(' ')
    #print(items)
    ints.append(count)
    ypos.append(float(items[0]))
    force.append(float(items[3]))

print(ypos)

plt.plot(ints,force)
plt.show()