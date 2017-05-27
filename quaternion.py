""" 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Quaternion Class for Python
* N.Mercadante
* 
* Engineer           | Date           | Description
* ---------------------------------------------------------------
* N.Mercadante       | 05-24-2017     | Initial Release
* ---------------------------------------------------------------
*
* COPYRIGHT 2017 NICHOLAS MERCADANTE, All Rights Reserved.
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
from math import *

class Quaternion:
	def __init__(self, q1, q2, q3, q4):
		self._q1 = q1
		self._q2 = q2
		self._q3 = q3
		self._q4 = q4

	def get_q1(self):
		return self._q1
	
	def get_q2(self):
		return self._q2
	
	def get_q3(self):
		return self._q3
	
	def get_q4(self):
		return self._q4

	def getQ(self):
		return [self.get_q1(), self.get_q2(), self.get_q3(), self.get_q4()]

	def set_q1(self, q):
		self._q1 = q
	
	def set_q2(self, q):
		self._q2 = q
	
	def set_q3(self, q):
		self._q3 = q
	
	def set_q4(self, q):
		self._q4 = q
	
	def normalize(self):
		norm = pow(self.get_q1(),2) + pow(self.get_q2(),2) + pow(self.get_q3(),2) + pow(self.get_q4(),2)
		norm = sqrt(norm)
	
		self._q1 = self._q1 / norm
		self._q2 = self._q2 / norm
		self._q3 = self._q3 / norm
		self._q4 = self._q4 / norm
	
	def rotate(self, vector_3d):
		"""
		Rotate the vector (vx, vy, vz) by self (q1, q2, q3, q4).
		should implement without cosine matrix if possible.
		"""
		self.normalize()
		
		vx = vector_3d[0]
		vy = vector_3d[1]
		vz = vector_3d[2]

		q0 = self.get_q1()
		q1 = self.get_q2()
		q2 = self.get_q3()
		q3 = self.get_q4()
	
		r1 = vx*(1-2*pow(q2, 2)-2*pow(q3, 2)) + vy*(2*(q1*q2+q0*q3)) + vz*(2*(q1*q3-q0*q2))	
		r2 = vx*(2*(q1*q2-q0*q3)) +	vy*(1-2*pow(q1, 2)-2*pow(q3, 2)) + vz*(2*(q2*q3+q0*q1))
		r3 = vx*(2*(q1*q3+q0*q2)) +	vy*(2*(q2*q3-q0*q1)) + vz*(1-2*pow(q1, 2)-2*pow(q2, 2))

		## Return Rotated Vector
		return [r1, r2, r3]  

	def __gt__(self, vector_3d):
		""" 
		q > r
		returns vector, r rotated by quaternion, q
		"""
		return self.rotate(vector_3d)
	
	def q2dc(self):
		"""
		Convert self to directional cosine matrix.
		"""
	

	def getEuler(self):
		
		q1 = self.get_q1()
		q2 = self.get_q2()
		q3 = self.get_q3()
		q4 = self.get_q4()

		## Euler Angles in Radians
		roll  = atan2( 2*(q1*q4 + q2*q3) , 1 - 2*(pow(q1, 2) + pow(q2, 2)) )
		pitch = asin( 2*(q2*q4 - q1*q3))
		yaw   = atan2( 2*(q3*q4 + q1*q2) , 1-2*(pow(q2, 2) + pow(q3, 2)))
	
		return [roll, pitch, yaw]

	def getEulerD(self):

		r2d = 180/pi
	
		q1 = self.get_q1()
		q2 = self.get_q2()
		q3 = self.get_q3()
		q4 = self.get_q4()

		## Euler Angles in Radians
		roll  = atan2( 2*(q1*q4 + q2*q3) , 1 - 2*(pow(q1, 2) + pow(q2, 2)) ) * r2d
		pitch = asin( 2*(q2*q4 - q1*q3)) * r2d
		yaw   = atan2( 2*(q3*q4 + q1*q2) , 1-2*(pow(q2, 2) + pow(q3, 2))) * r2d
	
		return [roll, pitch, yaw]

	def __add__(self, other):
		q_1 = self.get_q1() + other.get_q1() 
		q_2 = self.get_q2() + other.get_q2()
		q_3 = self.get_q3() + other.get_q3()
		q_4 = self.get_q4() + other.get_q4()

		return Quaternion(q_1, q_2, q_3, q_4)
	
	def __sub__(self, other):
		q_1 = self.get_q1() - other.get_q1() 
		q_2 = self.get_q2() - other.get_q2()
		q_3 = self.get_q3() - other.get_q3()
		q_4 = self.get_q4() - other.get_q4()

		return Quaternion(q_1, q_2, q_3, q_4)

	def __repr__(self):
		disp = "Quaternion Class\n----------------\n"
		disp += "q1 = " + str(self.get_q1()) + '\n' 
		disp += "q2 = " + str(self.get_q2()) + '\n' 
		disp += "q3 = " + str(self.get_q3()) + '\n'
		disp += "q4 = " + str(self.get_q4()) + '\n'
		return disp

	def __str__(self):
		disp =  "[" + str(self.get_q1()) + ', ' 
		disp += str(self.get_q2()) + ', ' 
		disp += str(self.get_q3()) + ', '
		disp += str(self.get_q4()) + ']'
		return disp

if __name__ == "__main__":
	
	"""
	q1 = Quaternion(0.50, -0.50, -0.50, 0.50)
	q1.normalize()
	
	q2 = Quaternion(0.01, 0.10, 0.02, 0.25)
	
	q3 = q1 + q2
	q4 = q1 - q2

	print "q1: " + str(q1)
	print "q2: " + str(q2)
	print "q3: " + str(q3)
	print "q4: " + str(q4)


	print "Quaternions:"	
	print q

	euler_angles = q.getEuler()
	euler_angles_deg = q.getEulerD()

	print "\nEuler Angles (rad):"
	print euler_angles
	
	print "\nEuler Angles (deg):"
	print euler_angles_deg
	
	print "\nRotate vector r (1,2,3) by quaternion:"
	r = [1,2,3]
	print q > r
	"""
	


	
