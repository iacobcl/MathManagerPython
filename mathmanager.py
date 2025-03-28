class mathmanager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b
	
	def interest(self, deposit, term):
		if deposit <= 0:
			return -1
		if term == 1:
			return (0.038*deposit)/12
		elif term == 2:
				return (0.036*deposit)/12
		else:
				return -2

	def tax(self, income):
		if (income >= 0 and income <= 12570):
			return 0
		elif (income > 12570 and income <= 50270):
			return 20/100*(income-12570)
		elif (income >50270 and income <= 125140):
			return 20/100*(50270-12570) + 40/100*(income-50270)
		elif (income > 125140):
			return 20/100*(50270-12570) + 40/100*(125140-50270) + 45/100*(income-125140)
		else:
			return -1
		

	def degree(self, fyp, comp1, comp2, opt1, opt2):
		if (fyp < 0 or comp1 < 0 or comp2 <0 or opt1 < 0 or opt2 < 0):
			return -1
		if (fyp > 100 or comp1 > 100 or comp2 > 100 or opt1 > 100 or opt2 > 100):
			return -1
		m = min(comp1, comp2, opt1, opt2)
		avg = (fyp + comp1 + comp2 + opt1 + opt2 - m) / 4
		if avg >=70:
			return "first"
		elif (avg < 70 and avg >= 60):
			return "2:1"
		elif (avg < 60 and avg >= 50):
			return "2:2"
		elif (avg < 50 and avg >= 40):
			return "third"
		else:
			return "fail"
			
