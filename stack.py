class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.insert(0,item)
		
	def peek(self):
		if self.stack:
			return self.stack[0]
		else:
			return 'Error'

	def pop(self):
		if self.stack:
			return self.stack.pop(0)

	def is_empty(self):
		return self.stack == []

	def __str__(self):
		if self.stack:
			st = str(self.stack[0])
			n = len(self.stack)
			for i in range(1, n):
				st += ' ' +str(self.stack[i])
			return st
		return ''
		

	def __len__(self):
		return len(self.stack)
		