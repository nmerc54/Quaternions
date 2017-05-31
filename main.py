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
for i in range(start_idx, start_idx + dur_idx):
	torque[i] = torque_pulse_mag

torque_x = list()
for i in torque:
	torque_x.append(i.item(0))


I = np.matrix([ [0.041667, 0.0, 0.0], [0.0, 0.041667, 0.0], [0.0, 0.0, 0.066667] ])
w = [np.matrix([ [0.0], [0.0], [0.0] ])]
H = [I*w[0]]
q = [ QuaternionM(1, -1, -1, 1) ]
qdot = [ np.matrix([ [0], [0], [0], [0] ]) ]


print I
print w[0]
print H[0]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                            SIMULATION                           *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * """

for i in range(num_elements)[1:]:

	H.append( H[i-1] + torque[i-1]*dt )
	w.append( np.linalg.inv(I) * H[i] )

	S = quatSkew( np.squeeze(np.asarray( w[i]) ))
	qdot.append( 0.5 * S * q[i-1] )
	qdot_temp = QuaternionM(qdot[i].item(0)*dt, qdot[i].item(1)*dt, qdot[i].item(2)*dt, qdot[i].item(3)*dt)
	
	q.append( q[i-1] + qdot[i] )
	


#plot(time, torque_x)
#show()























