from quaternionM import *
from matplotlib.pyplot import *

duration = 60.0		# seconds
dt = 0.10					# seconds
time = list()

num_elements = int(duration/dt)

# Fill out time Array
time.append(0.0)
for i in range(num_elements)[1:]:
	time.append( time[i-1] + dt )

time = np.array( time )


""" * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                  Simulation Set-Up                    *
* * * * * * * * * * * * * * * * * * * * * * * * * * * """

torque = list()
for i in range(num_elements):
	torque.append( np.matrix([ [0], [0], [0] ]) )

start_time = 25.0
start_idx = int(start_time/dt)
duration 	 = 1.0
dur_idx = int(duration/dt)

torque_pulse_mag = np.matrix([ [0.100], [0.100], [0.100] ])
for i in torque[start_idx: start_idx + dur_idx]:
	torque.append( torque_pulse_mag )


torque_x = list()
for i in torque:
	torque_x.append(i.item(0))

plot(time, torque_x)
show()
