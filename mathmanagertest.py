import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = mathmanager()
		self.assertEqual(math.add(0, 3), 3)

	def testSubtract(self):
		math = mathmanager()
		self.assertEqual(math.subtract(0, 3), -3)

	def testMultiply(self):
		math = mathmanager()
		self.assertEqual(math.multiply(0, 3), 0)

	def testInterest(self):
		math = mathmanager()
		self.assertEqual(round(math.interest(1000, 1)), 3)

	#Interest rate
	#positive amount, term = 2 
	def testInterest1(self):
		math = mathmanager()
		self.assertEqual(math.interest(1000, 2), 3)
	
	#positive amount, term = 3 (invalid) 
	def testInterest2(self):
		math = mathmanager()
		self.assertEqual(math.interest(1000, 3), -2)
		
	#negative amount, term = 1	
	def testInterest3(self):
		math = mathmanager()
		self.assertEqual(math.interest(-1000, 1), -1)

	#add: positive amount, term = 1, 3, 0, -1
	# negative amount, term = 2, -1, 0, 3
	# zero amount, term = 1, 2, 3, 0, -1	


	#Tax calculator
	#income in first bracket
	def testTax(self):
		math = mathmanager()
		self.assertEqual(math.tax(10000), 0)

	#income in second bracket
	def testTax1(self):
		math = mathmanager()
		self.assertEqual(math.tax(15000), 486)

	#income in third bracket
	def testTax2(self):
		math = mathmanager()
		self.assertEqual(math.tax(52000), 8232)
	
	#add income in all brackets, negative income, income equals each threashold


	#Degree classification calculator
	#combination of grades that get a 2:1
	def testDegree(self):
		math = mathmanager()
		self.assertEqual(math.degree(40, 70, 70, 55, 60), "2:1")

	#combination of grades that get a third
	def testDegree1(self):
		math = mathmanager()
		self.assertEqual(math.degree(0, 70, 50, 60, 40), "third")

	#at least one negative grade
	def testDegree2(self):
		math = mathmanager()
		self.assertEqual(math.degree(-1, 40, 40, 40, 40), -1)

	#add at least one grade higher than 100, combination of grades that get a fist, 2:2, fail
