class Calculator:
	result = 0

	def __init__(self):
		pass

	def add(self, a, b):
		self.result = addition(a, b)
		return self.result

	def subtract(self, a, b):
		self.result = subtraction(a, b)
		return self.result

	def multiplication(self, a, b):
		self.result = multiplication(a, b)
		return self.result

	def division(self, a, b):
		self.result = division(a, b)
		return self.result

	def square(self, a):
		self.result = square(a)
		return self.result

	def root(self, a):
		self.result = root(a)
		return self.result


def addition(a, b):
	return a + b


def subtraction(a, b):
	return b - a


def multiplication(a, b):
	return a * b


def division(a, b):
	return b / a


def square(a):
	return a ** 2


def root(a):
	return a ** 0.5
