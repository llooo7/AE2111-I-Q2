import os
import matplotlib.pyplot as plt
import numpy as np

data = open("MainWing_a=0.00_v=10.00ms.txt")
xpos = []
force = []
count = 0

for line in data.readlines():
    count += 1
    if count > 21:
        items = line.split('   ')
        print(items)
        force.append(items[0])
        #xpos.append(items[3])

plt.plot(xpos,force)
plt.show()