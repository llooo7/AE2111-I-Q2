import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from Internal_torsion import *


thickness_chord = 0.14
start_point = 0.288
end_point = 0.9
left_side = 0.052700 + 0.052900
right_side = 0.051600 + 0.028600
height = end_point - start_point
span = np.arange(0,12.815,0.001)
t_spar = 0.004
t_skin = 0.002
A_str = 0.0005
n_str_top = 2
n_str_bottom = 2
E = 68.94757*10**9
rho = 2700
N = -95600*np.sin(25.98)
Vmax = 1007760
kv = 3

def chord_length(y):
    return (-0.2472*y + 4.52)

def wingbox_height(y):
    return 0.5*0.612*chord_length(y)



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


def aspect(A_str,n_str_top,n_str_bottom,t_spar,t_skin):
    chords = chord_length(span)
    p = 0
    ab1 = []
    ab2 = []
    for i in chords:
       
        A1,A2,A3,A4,height,left,right,bottom = area(i,t_spar,t_skin)
        L = span[p]
        h = wingbox_height(L) - wingbox_height(12.814)
        a = np.sqrt(h**2 + L**2)
        ab1.append(a/left)
        ab2.append(a/right)
        
        p += 1

    return ab1,ab2

def web_buckling(V,kv):
    t1 =[]
    
    chords = chord_length(span)
    p = 0
    for i in chords:
        A1,A2,A3,A4,height,left,right,bottom = area(i,t_spar,t_skin)
        
        t_avg = V/(left*t_spar + right*t_spar)
        A = 0.5*(left+right)*height+A_str*(n_str_top+n_str_bottom)
        T = torquemax[p]
        t_max = T/(2*A)/t_spar + t_avg
        p += 1
    
    
    
    
    
    
    
    
    
    
    
    
    