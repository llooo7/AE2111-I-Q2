import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp



thickness_chord = 0.14
start_point = 0.288
end_point = 0.9
left_side = 0.052700 + 0.052900
right_side = 0.051600 + 0.028600
height = end_point - start_point
span1 = np.arange(0,12.000,0.001)
b_front = 0.376666544
b_back = 0.35126654399999996

t_sparl = [0.015,0.013,0.017]
t_skinl = [0.01,0.0085,0.0075]
A_strl = [0.00155,0.00108,0.00085]
l_strl = [0.16,0.08,0.065]
n_str_topl = [8,15,21]
n_str_botl = [8,15,21]
t_sparcl = [0.015,0.013,0.017]
t_skincl = [0.01,0.0085,0.0075]
n_str_topcl = [8,15,5]
n_str_botcl = [8,15,5]


b_top = 1.7969480351999998
b_bottom = 1.797201170322717


def chord_length(y):
    return (-0.2472*y + 4.52)

def wingbox_height(y):
    return 0.5*0.612*chord_length(y)

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

def area_section(c,t_spar,t_skin,n_str_top,n_str_bot,A_str):

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

def area_enclosed(c,t_spar,t_skin,n_str_top,n_str_bot,A_str):
    t = thickness_chord*c
    diff = t - 0.14
    left = left_side + diff
    right = right_side + diff
    height = 0.9*c - 0.288*c
    bottom = np.sqrt((left-right)**2+height**2)

    A = 0.5*(left+right)*height+A_str*(n_str_top+n_str_bot)
    return A,left,right,height,bottom



    
    
a = np.sqrt((wingbox_height(0)-wingbox_height(12.815))**2+12.815**2)

    
    
    
    
    
    