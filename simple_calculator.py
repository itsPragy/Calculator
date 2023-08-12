from stack import Stack

class SimpleCalculator:
	def __init__(self):
		self.history = []

	def evaluate_expression(self, input_expression):
		try:
			tokens = []
			c = 0
			f = 1
			for i in input_expression:
				if i == " ":
					if tokens:
						if tokens[-1].isnumeric():
							f = 0
					continue
				elif i in '+-*/':
					tokens.append(i)
					f = 1
				elif i.isnumeric():
					if tokens:
						if tokens[-1].isnumeric() and f:
							tokens[-1] += i
						else:
							tokens.append(i)
							f = 1
					else:
						tokens.append(i)
						f = 1
				else:
					self.history.insert(0,(input_expression,'Error'))
					return 'Error'
			
			if len(tokens) != 3 or tokens[1] not in '+-*/' or not(tokens[0].isnumeric) or not(tokens[2].isnumeric):
				self.history.insert(0,(input_expression,'Error'))
				return 'Error'
			
			else:
				op = tokens[1]
				n1 = float(tokens[0])
				n2 = float(tokens[2])
				if op == '+':
					res = n1+n2
				elif op == '-':
					res = n1-n2
				elif op == '*':
					res = n1*n2
				elif n2:
					res = n1/n2
				else:
					res = 'Error'
				self.history.insert(0,(input_expression,res))
				return res
		except:
			self.history.insert(0,(input_expression,'Error'))
			return 'Error'

	def get_history(self):
		return self.history
