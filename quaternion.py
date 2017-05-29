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
from sys import *

class Quaternion(object):
	def __init__(self, q1, q2, q3, q4):
		self._q1 = q1
		self._q2 = q2
		self._q3 = q3
		self._q4 = q4
		
		if self.norm() != 0:
			self.normalize()

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
		norm = self.norm()
	
		self._q1 = self._q1 / norm
		self._q2 = self._q2 / norm
		self._q3 = self._q3 / norm
		self._q4 = self._q4 / norm


	def norm(self):
		Qnorm = pow(self.get_q1(),2) + pow(self.get_q2(),2) + pow(self.get_q3(),2) + pow(self.get_q4(),2)
		return sqrt(Qnorm)

	
	def rotate(self, vector_3d):
		"""---------------------------------------------------------
		Rotate the vector (vx, vy, vz) by self (q1, q2, q3, q4).
		should implement without cosine matrix if possible.
		---------------------------------------------------------"""
		if type(vector_3d) is not list:
			raise QuatError("ERROR: Input must be a List")

		if len(vector_3d) != 3:
			raise QuatError("ERROR: Input must be of length 3")

		if self.norm() != 1:
			raise QuatError("ERROR: Not Unit-Quaternion")		

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

		return [r1, r2, r3] # Rotated Vector 


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
		if type(other) is not Quaternion:
			raise QuatError("ERROR: Can only add with type Quaternion")

		q_1 = self.get_q1() + other.get_q1() 
		q_2 = self.get_q2() + other.get_q2()
		q_3 = self.get_q3() + other.get_q3()
		q_4 = self.get_q4() + other.get_q4()

		return Quaternion(q_1, q_2, q_3, q_4)

	
	def __sub__(self, other):
		if type(other) is not Quaternion:
			raise QuatError("ERROR: Can only subtract with type Quaternion")

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



class QuatError(Exception):
	pass



if __name__ == "__main__":
	
	q1 = Quaternion(0.50, -0.50, -0.50, 0.50)
	q2 = Quaternion(1,2,3,4)

	try:
		r = [1,2,2,3]
		q1 > r
	except QuatError as detail:
		print "Rotate vector of length 4"
		print detail	

	try:
		q1 > "apples"
	except QuatError as detail:
		print "\nRotate a non-vector"
		print detail
	
	try:
		q1 + [1,2]
	except QuatError as detail:
		print "\nAdd with a non-quaternion vector"
		print detail

	try:
		q1 + 5
	except QuatError as detail:
		print "\nAdd with a non-quaternion scalar"
		print detail

	try:
		q1 + "apples"
	except QuatError as detail:
		print "\nAdd with a non-quaternion string"
		print detail

	try:
		q1 + q2
	except QuatError as detail:
		print "\nAdd with a quaternion"
		print detail

