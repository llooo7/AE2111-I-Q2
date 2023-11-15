import math

#constants
pressure0 = 101325
temp0 = 288.15
R = 287
g0 = 9.80665

#lowbound,upbound,change
zones = [[0,11000,-0.0065],[11000,20000,0],[20000,32000,0.001],[32000,47000,0.0028],[47000,51000,0],[51000,71000,-0.0028],[71000,84852,-0.002],[84852,90000,0],[90000,105000,0.004]]

def getTemp(h):
	hRemaining = float(h)
	temp = temp0
	for i in range(0,len(zones)):
		if hRemaining <= zones[i][1] - zones[i][0]:
			temp += hRemaining*zones[i][2]
			return temp
		elif hRemaining > zones[i][1] - zones[i][0]:
			temp += zones[i][1]*zones[i][2]	
			hRemaining -= zones[i][1]	

def getPress(h):
	press = pressure0
	hRemaining = float(h)
	for i in range(0,len(zones)):
		if zones[i][2] != 0:
			if hRemaining <= zones[i][1] - zones[i][0] :
				press = press*math.pow(getTemp(float(h))/getTemp(zones[i][0]),-g0/zones[i][2]/R)
				return press		
			else:
				press = press*math.pow(getTemp(zones[i][1])/getTemp(zones[i][0]),-g0/zones[i][2]/R) 
				hRemaining -= (zones[i][1] - zones[i][0])	
		else:
			if hRemaining <= zones[i][1] - zones[i][0] :
				press = press*math.exp(-g0*hRemaining/R/getTemp(zones[i][1]))
				return press
			else:
				press = press*math.exp(-g0*(zones[i][1] - zones[i][0])/R/getTemp(zones[i][1]))
				hRemaining -= zones[i][1] - zones[i][0]	

def getDensity(h):
	return getPress(h) / getTemp(h) / R
