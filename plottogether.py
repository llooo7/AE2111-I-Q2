import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from Moment_of_inertia import *
from Twist import torsional_constant
from test import L
from test2 import K

t_spar = [0.015,0.01]
t_skin = [0.002,0.001]
A_str = [0.0005,0.0005]
n_str_top = [6,12]
n_str_bot = [6,12]



for tspar,tskin,astr,nstrtop,nstrbot in zip(t_spar,t_skin,A_str,n_str_top,n_str_bot):
    I,m = moment_of_inertia(astr, nstrtop, nstrbot, tspar, tskin)
    l = 'ok'
    if tspar == 0.015:
        l = 'Design Option 1'
    elif tspar == 0.01:
        l = 'Design Option 2'
    plt.plot(span,I,label=l)
plt.plot(span,L,label='Design Option 3')
plt.xlabel('y [m]')
plt.ylabel('I [m^4]')
plt.title('Span-wise moment of Inertia in [m^4]')
plt.grid(True)
plt.legend()

plt.show()


for tspar,tskin,astr,nstrtop,nstrbot in zip(t_spar,t_skin,A_str,n_str_top,n_str_bot):
    J = torsional_constant(nstrtop,nstrbot,astr,tspar, tskin)
    k = 'ok'
    if tspar == 0.015:
        k = 'Design Option 1'
    elif tspar == 0.01:
        k = 'Design Option 2'

    plt.plot(span,J,label=k)
plt.plot(span,K,label='Design Option 3')
plt.xlabel('y [m]')
plt.ylabel('J [m^4]')
plt.title('Span-wise torsonal constant in [m^4]')
plt.grid(True)
plt.legend()

plt.show()


