surface = 75.33
aspRat = 8.74
wingspan = 25.63
taperRat = 0.30
rootCh = 4.52
tipCh = 1.36
mac = 3.22
dihed = 2.12
ymac = 5.26
xlemac = 0.35
Cd0 = 0.0198
e = 0.517

def chord(y):
    return rootCh - y * (rootCh-tipCh) / (wingspan/2)