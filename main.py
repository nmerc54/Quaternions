from quaternionM import *
from matplotlib.pyplot import *

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$ NOTE: qdot.setQMat() is not working properly, giving a\
#$			 None Type.
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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

#########################################################
start_time = 25.0
start_idx = int(start_time/dt)
duration 	 = 1.0
dur_idx = int(duration/dt)

torque_pulse_mag = np.matrix([ [0.01], [0.021], [-0.01] ])
for i in range(start_idx, start_idx + dur_idx):
	torque[i] = torque_pulse_mag

start_time = 35.0
start_idx = int(start_time/dt)
duration 	 = 1.0
dur_idx = int(duration/dt)

torque_pulse_mag = np.matrix([ [-0.021], [-0.01], [0.0] ])
for i in range(start_idx, start_idx + dur_idx):
	torque[i] = torque_pulse_mag
#########################################################

torque_x = list()
for i in torque:
	torque_x.append(i.item(0))


I = np.matrix([ [0.041667, 0.0, 0.0], [0.0, 0.041667, 0.0], [0.0, 0.0, 0.066667] ])
w = [np.matrix([ [0.0], [0.0], [0.0] ])]
H = [I*w[0]]
q = [ QuaternionM(1, -1, -1, 1) ]
qdot = [ QuatDotM(0.0, 0.0, 0.0, 0.0) ]




""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                            SIMULATION                           *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * """

for i in range(num_elements)[1:]:

	H.append( H[i-1] + torque[i-1]*dt )
	w.append( np.linalg.inv(I) * H[i] )

	S = quatSkew( np.squeeze(np.asarray( w[i]) ))
	
	fill = 0.5 * S * q[i-1].getQMat()
	qd_temp = QuatDotM(fill.item(0), fill.item(1), fill.item(2), fill.item(3))
	qdot.append( qd_temp )
	q.append( quatIntegrate(q[i-1], qdot[i], dt) )
	


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                              PLOTTING                           *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * """
roll = list()
pitch = list()
yaw = list()

torquex = list()
torquey = list()
torquez = list()

for i in range(num_elements):
	roll.append( q[i].getEulerD().item(0) )
	pitch.append( q[i].getEulerD().item(1) )
	yaw.append( q[i].getEulerD().item(2) )
	
	torquex.append( torque[i].item(0) )
	torquey.append( torque[i].item(1) )
	torquez.append( torque[i].item(2) )

figure(1)
subplot(211)
plot(time, roll, time, pitch, time, yaw)
xlabel("Time (sec)")
ylabel("System Respose (Deg)")

subplot(212)
plot(time, torquex, time, torquey, time, torquez)
xlabel("Time (sec)")
ylabel("Torques (N-m)")


show()























