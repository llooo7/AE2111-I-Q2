import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from isa import *
from wing import *
from Moment_of_inertia import *
from aeroforces import *



n_values1 = [2.5]
mass_values1 = [31139.2]
v_values1 = [133.5]
h_values1 = [10668]

wing_weight = 2387.38 * 9.80655 + 2635*9.80655
engine_weight = 2079 * 9.80655

def wing_load_dist(y):
    wing_density = wing_weight/75.3316174
    return wing_density*chord_length(y)



for n,mass,v,h in zip(n_values1,mass_values1,v_values1,h_values1):

    Weight = mass*9.81
    rho = getDensity(h)
    v = v*np.sqrt(1.225/rho)
    q = 1/2*rho*v**2
    CLd = n*Weight/(q*surface)
    CDd = Cd0 + CLd**2/np.pi/aspRat/e
    CL0 = 0.383907
    CL10 = 1.2045817
    
    CD0 = 0.005339
    CD10 = 0.051295
    factor = (CLd-CL0)/(CL10-CL0)
    factor2 = (CDd - CD0)/(CD10 - CD0)
    
    CLd_dist = l0(span) + factor*(l10(span) -l0(span))
    L_dist = CLd_dist*q*surface
    print(rho)
    print(q)
    print(surface)
    CDd_dist = d0(span) + factor*(d10(span)-d0(span))
    D_dist = CDd_dist*q*surface
    
    alpha = np.arcsin(factor*np.sin(10/57.3))*57.3
    print(alpha)
    N_dist = L_dist*np.cos(alpha) + D_dist*np.sin(alpha)
    print(wing_load_dist(span))
    result_dist = N_dist - n*wing_load_dist(span)
plt.plot(span, N_dist)

plt.xlabel('y')
plt.ylabel('I')
plt.title('Span-wise moment of Inertia')

plt.show()