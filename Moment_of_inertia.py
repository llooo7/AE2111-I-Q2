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
span = np.arange(0,12.815,0.001)
t_spar = 0.02
t_skin = 0.005
A_str = 0.01
n_str = 8
E = 68.94757*10**9



def plot_trapezoid(base1, base2, height):
    """
    Plot a trapezoid with given base1, base2, and height.
    """
    # Define the vertices of the trapezoid
    x = [0, base1, base2, 0]
    y = [0, 0, height, height]

    # Connect the vertices to form the trapezoid
    plt.plot(x + [x[0]], y + [y[0]], 'b-')

    # Set labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Trapezoid')

    # Display the plot
    plt.show()


plot_trapezoid(left_side, right_side, height)

def chord_length(y):
    return (-0.2472*y + 4.52)

def stringer(left,right,top,bottom,n_str):    
    str_top = [0]
    str_bottom = [0]
    
    space_top = top/(n_str-1)
    space_bottom = (left-right)/(n_str-1)
    
    for i in range(n_str-1):
       x_top = space_top + str_top[-1]
       y_bottom = space_bottom + str_bottom[-1]
       str_top.append(x_top)
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


def moment_of_inertia(A_str,n_str,t_spar,t_skin):
    
    chords = chord_length(span)
    moment_of_inertia = []
    
    for i in chords:
        
        Atop,Aleft,Aright,Abottom,height,left,right,bottom = area(i,t_spar,t_skin)
        
        c_x = (left**2 + right**2 + left*right)/(3*(left+right))
        c_y = (left+2*right)/(3*(left+right))*height
        
        distance_top = c_x
        distance_bottom = left - np.sqrt((bottom/2)**2/(1+(height/(left-right))**2)) - c_x
        distance_left = left/2 - c_x
        distance_right = right/2 - c_x
        t,b = stringer(left,right,height,bottom,n_str)
        
        for j in b:
            I_str_bottom = []
            j = c_x - j
            I_str_bottom.append(A_str*j**2)
            
        I_str_bottom = sum(I_str_bottom)
        I_str_top = n_str*A_str*distance_top**2
        I_top = 1/12*height*t_skin**3 + Atop*distance_top**2
        I_left = 1/12*t_spar*left**3 + Aleft*distance_left**2
        I_right = 1/12*t_spar*right**3 + Aright*distance_right**2
        I_bottom = 1/12*t_skin*bottom*((t_skin**2*(height/bottom)**2)+bottom**2*((left-right)/bottom)**2)+Abottom*distance_bottom**2
        
        
        I_tot = I_top + I_left + I_right + I_bottom + I_str_bottom + I_str_top
        
        moment_of_inertia.append(I_tot)

    return moment_of_inertia


I = moment_of_inertia(A_str,n_str,t_spar,t_skin)


a,b,c,d,e = np.polyfit(span,I,4)

I_2 = a*span**4 + b*span**3 + c*span**2 + d*span + e

plt.plot(span, I)
plt.plot(span, I_2)
plt.xlabel('y')
plt.ylabel('I')
plt.title('Span-wise moment of Inertia')

plt.show()
