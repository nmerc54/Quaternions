from quaternion import *
from random import uniform
from matplotlib.pyplot import *


duration = 60.0 		# seconds
dt = 1						# seconds

N = int(duration/dt)

quats = list()
euler = list()
roll = list()

for i in range(N):
	a1 = 1.0*sin(i) + uniform(-0.1, 0.1)
	a2 = 2.0*sin(i) + uniform(-0.1, 0.1)
	a3 = 1.0*cos(i) + uniform(-0.1, 0.1)
	a4 = 2.0*cos(i) + uniform(-0.1, 0.1)

	quats.append( Quaternion(a1, a2, a3, a4) )
	euler.append( quats[i].getEulerD() )
	roll.append( euler[i][0] )
	
"""
Plot Results:
"""

print "N: " + str(N) + "\n"

plot(range(N), roll)
show()
