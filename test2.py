import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from Moment_of_inertia import *
from Internal_torsion import torquemax,torquemin


G =26*10**9


def torsional_constant(n_str_top,n_str_bottom,A_str,t_spar,t_skin):
    
    chords = chord_length(span)
    K = []
    t1 = []
    change = chords[9500]
    
    for i in chords:
   
        if i <= change:
           t_spar = t_sparc
           t_skin = t_skinc
           n_str_top = n_str_topc
           n_str_bot = n_str_botc
        
        A1,A2,A3,A4,height,left,right,bottom = area(i,t_spar,t_skin)
        
        A = 0.5*(left+right)*height+A_str*(n_str_top+n_str_bottom)
        
        l = (left + right)/t_spar + (height + bottom)/t_skin
        
        j = 4*A**2/l
        
        K.append(j)
        
    return K
        
     
K = torsional_constant(n_str_top,n_str_bottom,A_str,t_spar, t_skin)





