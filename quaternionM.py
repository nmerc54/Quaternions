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
# IMPORTS
from math import *
import numpy as np

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$ NOTE: 1. Need to implement multiply for vectors and scalars $$
#$       2. Need to also implement a "qdot" class that is not  $$
#$          normalized                                         $$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                  Quaternion Matrix Class                      *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
class QuaternionM(object):
	def __init__(self, q1, q2, q3, q4):
		
		self._Q = np.array([q1, q2, q3, q4])
	
		if self.norm() != 0:
			self.normalize()

	def get_q1(self):
		return self._Q.item(0)
	
	def get_q2(self):
		return self._Q.item(1)
	
	def get_q3(self):
		return self._Q.item(2)
	
	def get_q4(self):
		return self._Q.item(3)

	def getQArray(self):
		return self._Q

	def getQMat(self):
		return np.matrix( self.getQArray() ).transpose()

	def setQ(self, q1, q2, q3, q4):
		self._Q = np.array([q1, q2, q3, q4])


	def normalize(self):
		norm = self.norm()
	
		q1 = self.get_q1() / norm
		q2 = self.get_q2() / norm
		q3 = self.get_q3() / norm
		q4 = self.get_q4() / norm

		self.setQ(q1, q2, q3, q4)


	def norm(self):
		Qnorm = np.linalg.norm( self.getQArray() )
		return Qnorm

	
	def rotate(self, vector_3d):
		"""---------------------------------------------------------
		Rotate the vector (vx, vy, vz) by self (q1, q2, q3, q4).
		should implement without cosine matrix if possible.
		---------------------------------------------------------"""
		if type(vector_3d) is list:
			vector_3d = np.array(vector_3d)
		
		if type(vector_3d) is not np.ndarray:
			raise QuatError("ERROR: Input must be a NumPy Array")

		if len(vector_3d) != 3:
			raise QuatError("ERROR: Input must be of length 3")

	#	if self.norm() != 1.0:
	#		print "norm is: " + str(self.norm())
	#		raise QuatError("ERROR: Not Unit-Quaternion")		

		vx = vector_3d.item(0)
		vy = vector_3d.item(1)
		vz = vector_3d.item(2)

		q0 = self.get_q1()
		q1 = self.get_q2()
		q2 = self.get_q3()
		q3 = self.get_q4()
	
		r1 = vx*(1-2*pow(q2, 2)-2*pow(q3, 2)) + vy*(2*(q1*q2+q0*q3)) + vz*(2*(q1*q3-q0*q2))	
		r2 = vx*(2*(q1*q2-q0*q3)) +	vy*(1-2*pow(q1, 2)-2*pow(q3, 2)) + vz*(2*(q2*q3+q0*q1))
		r3 = vx*(2*(q1*q3+q0*q2)) +	vy*(2*(q2*q3-q0*q1)) + vz*(1-2*pow(q1, 2)-2*pow(q2, 2))

		return np.array( [r1, r2, r3] ) # Rotated Vector 


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
	
		return np.array( [roll, pitch, yaw] )


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
	
		return np.array( [roll, pitch, yaw] )


	def __add__(self, other):
		if type(other) is not QuaternionM:
			raise QuatError("ERROR: Can only add with type Quaternion")

		q_1 = self.get_q1() + other.get_q1() 
		q_2 = self.get_q2() + other.get_q2()
		q_3 = self.get_q3() + other.get_q3()
		q_4 = self.get_q4() + other.get_q4()

		return QuaternionM(q_1, q_2, q_3, q_4)

	
	def __sub__(self, other):
		if type(other) is not QuaternionM:
			raise QuatError("ERROR: Can only subtract with type Quaternion")

		q_1 = self.get_q1() - other.get_q1() 
		q_2 = self.get_q2() - other.get_q2()
		q_3 = self.get_q3() - other.get_q3()
		q_4 = self.get_q4() - other.get_q4()

		return QuaternionM(q_1, q_2, q_3, q_4)


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


"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                  Quaternion Matrix Class                      *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
class QuatDotM:
	def __init__(self, qd1 = 0, qd2 = 0, qd3 = 0, qd4 = 0):
		self._Qd = np.array([qd1, qd2, qd3, qd4])
		
	def get_qd1(self):
		return self._Qd.item(0)
	
	def get_qd2(self):
		return self._Qd.item(1)
	
	def get_qd3(self):
		return self._Qd.item(2)
	
	def get_qd4(self):
		return self._Qd.item(3)

	def getQdArray(self):
		return self._Qd

	def getQdMat(self):
		return np.matrix( self.getQdArray() ).transpose()

	def setQd(self, qd1, qd2, qd3, qd4):
		self._Qd = np.array([qd1, qd2, qd3, qd4])

	def setQdM(self, qd_matrix):
		if len(qd_matrix) != 4:
			raise QuatError("ERROR: Matrix must have exactly 4 elements")
	
		self._Qd = np.squeeze(np.asarray(qd_matrix))


	def __repr__(self):
		disp = "Quaternion Derivative Class\n----------------------------\n"
		disp += "qd1 = " + str(self.get_qd1()) + '\n' 
		disp += "qd2 = " + str(self.get_qd2()) + '\n' 
		disp += "qd3 = " + str(self.get_qd3()) + '\n'
		disp += "qd4 = " + str(self.get_qd4()) + '\n'
		return disp


	def __str__(self):
		disp =  "[" + str(self.get_qd1()) + ', ' 
		disp += str(self.get_qd2()) + ', ' 
		disp += str(self.get_qd3()) + ', '
		disp += str(self.get_qd4()) + ']'
		return disp

"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                         Exceptions                            *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

class QuatError(Exception):
	pass




"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                     Helper Functions                          *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
def quatSkew(w):
	"""
	Skew-Symmetric Matrix:
		INPUT: 	np.array of angular velocity
		OUTPUT:	np.matrix of size 4x4
	"""

	if type(w) is not np.ndarray:
		raise QuatError("ERROR: w must be of type np.array")
	if len(w) != 3:
		raise QuatError("ERROR: w must be of length 3")
	

	row_1 = [0					, w.item(2)	, -w.item(1), w.item(0)	]
	row_2 = [-w.item(2), 0					, w.item(0)	, w.item(1)	]
	row_3 = [w.item(1)	, -w.item(0), 0					, w.item(2)	]
	row_4 = [-w.item(0), -w.item(1), -w.item(2), 0					]

	return np.matrix([ row_1, row_2, row_3, row_4 ])



def quatIntegrate(quat1, qdot1, time_step):
	"""
	quat1 		-> type QuaternionM
	qdot1 		-> type QuatDotM
	time-step	-> type float

	Returns a QuaternionM
	"""

	quaternion_matrix = quat1.getQMat()
	quat_deriv_matrix = qdot1.getQdMat()

	new_quaternion = quaternion_matrix + quat_deriv_matrix * time_step

	return QuaternionM(new_quaternion.item(0), new_quaternion.item(1), new_quaternion.item(2), new_quaternion.item(3))




"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*                        Tests                                  *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""


if __name__ == "__main__":

	angular_velocity = np.array([ 0.1, 0.1, 0.2 ])
	print "Length: " + str(len(angular_velocity))
	print quatSkew(angular_velocity)



	"""	
	q1 = QuaternionM(0.50, -0.50, -0.50, 0.50)
	quat2 = QuaternionM(1,2,3,4)

	print "q1: " + str(q1)
	print "norm: " + str(q1.norm())

	print "q2: " + str(quat2)
	print "norm: " + str( quat2.norm() )
	
	try:
		print "Rotate an np.array of lengtrh 3:"
		n = np.array( [1,2,3] )
		#print(q1 > n)
		print(quat2 > n)
	except QuatError as detail:
		print detail


	try:
		r = np.array( [1,2,2,3] )
		q1 > r
	except QuatError as detail:
		print "Rotate an np.array of length 4"
		print detail	

	try:
		r =[1,2,2]
		q1 > r
	except QuatError as detail:
		print "Rotate LIST of length 3"
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
"""
