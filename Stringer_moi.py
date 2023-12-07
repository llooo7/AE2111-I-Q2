import math

t_str=0.02
l_str=0.05


def str_area(t,l):
    area=2*l*t
    
    return area


def str_moment_inertia(l,t):
    str_moment_inertia=1/12*l**3*t+l*t*(l/2)**2

    return str_moment_inertia

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