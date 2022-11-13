import numpy as np

class Variable:
	def __init__(self, data) -> None:
		self.data = data

class Function:
	def __call__(self, input):
		x = input.data
		y = self.forward(x)
		output = Variable(y)
		return output

	def forward(self, x):
		raise NotImplementedError()

class Square(Function):
	def forward(self, x):
		return x ** 2

class Exp(Function):
	def forward(self, x):
		return np.exp(x)

a = Square()
b = Exp()

x = Variable(np.array(2))
y = a(b(a(x)))
print(y.data)