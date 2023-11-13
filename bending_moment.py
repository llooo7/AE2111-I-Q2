from scipy.integrate import quad 
  
def s(x): 
  return 3.0*x*x + 1.0
  
I, err = quad(s, x, L) 
print(I) 
print(err)
