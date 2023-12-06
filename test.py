import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from useful_functions import *

thickness_chord = 0.14
start_point = 0.288
end_point = 0.9
left_side = 0.052700 + 0.052900
right_side = 0.051600 + 0.028600
height = end_point - start_point
span = np.arange(0,12.815,0.001)

E = 68.94757*10**9
rho = 2700


def chord_length(y):
    return (-0.2472*y + 4.52)


def stringer(left,right,top,bottom,n_str_top,n_str_bottom):    
    str_top = [0]
    str_bottom = [0]

    space_top = top/(n_str_top-1)
    space_bottom = (left-right)/(n_str_bottom-1)
    
    for i in range(n_str_top-1):
       x_top = space_top + str_top[-1]
       str_top.append(x_top)

    for j in range(n_str_bottom-1):
        y_bottom = space_bottom + str_bottom[-1]
       
        str_bottom.append(y_bottom)
        
    
    return str_top,str_bottom
    
  

def area(c,t_spar,t_skin):
    t = thickness_chord*c
    diff = t - 0.14
    left = left_side + diff
    right = right_side + diff
    height = 0.9*c - 0.288*c
    bottom = np.sqrt((left-right)**2+height**2)
    A1 = height*t_skin
    A2 = left*t_spar
    A3 = right*t_spar
    A4 = bottom*t_skin
    return A1,A2,A3,A4,height,left,right,bottom


def moment_of_inertia(A_str,n_str_top,n_str_bottom,t_spar,t_skin,n_str_topc,n_str_botc,t_sparc,t_skinc):
    
    chords = chord_length(span)
    moment_of_inertia = []
    mass_dist = []
    change = chords[9500]
    centroid = []
    for i in chords:
        if i <= change:
            t_spar = t_sparc
            t_skin = t_skinc
            n_str_top = n_str_topc
            n_str_bot = n_str_botc

        Atop,Aleft,Aright,Abottom,height,left,right,bottom = area(i,t_spar,t_skin)

        c_x = (left**2 + right**2 + left*right)/(3*(left+right))
        c_y = (left+2*right)/(3*(left+right))*height
        centroid.append(c_x)
        distance_top = c_x
        distance_bottom = left - np.sqrt((bottom/2)**2/(1+(height/(left-right))**2)) - c_x
        distance_left = left/2 - c_x
        distance_right = right/2 - c_x
        t,b = stringer(left,right,height,bottom,n_str_top,n_str_bottom)
        I_str_bottom = []
        for j in b:
            
            dist = left - c_x - j
            steiner = A_str*dist**2
            I_str_bottom.append(steiner)

        
        I_str_bottom = sum(I_str_bottom)

        I_str_top = n_str_top*A_str*distance_top**2

        I_top = 1/12*height*t_skin**3 + Atop*distance_top**2
        I_left = 1/12*t_spar*left**3 + Aleft*distance_left**2
        I_right = 1/12*t_spar*right**3 + Aright*distance_right**2
        I_bottom = 1/12*t_skin*bottom*(bottom**2*((left-right)/bottom)**2)+Abottom*distance_bottom**2
        
        
        I_tot = I_top + I_left + I_right + I_bottom + I_str_bottom + I_str_top
        
        moment_of_inertia.append(I_tot)
        
        area_tot = Atop + Aleft + Abottom + Aright + (n_str_top + n_str_bottom)*A_str
        m_dist = area_tot*rho
        mass_dist.append(m_dist)
    return moment_of_inertia,mass_dist,centroid

I_lst = []
for tspar,tskin,nstrtop,nstrbot,astr,tsparc,tskinc,nstrtopc,nstrbotc in zip(t_sparl, t_skinl, n_str_topl, n_str_botl, A_strl,t_sparcl,t_skincl,n_str_topcl,n_str_botcl):
    I,m,cx = moment_of_inertia(astr, nstrtop, nstrbot, tspar, tskin, nstrtopc, nstrbotc, tsparc, tskinc)
    I_lst.append(I)
    plt.plot(span,I)
    a1,b1 = np.polyfit(span,m,1)

    def mass(y):
        return a1*y + b1

    result, error = sp.integrate.quad(mass, 0, 12.815)

    print(result)
plt.show()