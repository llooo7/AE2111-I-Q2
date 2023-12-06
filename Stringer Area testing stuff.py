import math

t_str=0.001
l_str=0.01
h_str=0.02

def str_area(h,t,l):
    area=h*t+l*t
    
    return area

print(str_area(h_str, t_str, l_str))

def str_moment_inertia(h,t):
    str_moment_inertia=1/12*h**3*t+h*t*(h/2)**2

    return str_moment_inertia
print(str_moment_inertia(h_str, t_str))