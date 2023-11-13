from scipy.integrate import quad 
from matplotlib import pyplot as plt

L = 28*100

def s(x): 
  return 3.0*x*x + 1.0   # example, input the shear stress function when it is done

def integrate(j):
    return quad(s, j, L) 




xtab = []
ytab = []

for i in range(0, L):
    xtab.append(i/100)
    I, err = integrate(i/100)
    ytab.append(I)

fig, ax = plt.subplots()
ax.plot(xtab, ytab, color="black")
#plt.ylim(-0.5, 0.5)
plt.title("Bending moment diagram")

plt.show()
