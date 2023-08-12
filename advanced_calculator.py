from simple_calculator import SimpleCalculator
from stack import Stack

def maximum(operator_list):
	
    precedence = {'+':1, '-':1, '*':2, '/':3}
    n = len(operator_list)
    ind = n-1
    
    for i in range(n-2, -1, -1):
	    if precedence[operator_list[i]] > precedence[operator_list[ind]]:
		    ind = i
            
    return ind

def bodmas(operator_list, operand_list):
    
    if operator_list:
        i = maximum(operator_list)
        op = operator_list.pop(i)
        n2 = operand_list.pop(i)
        n1 = operand_list.pop(i)
        if op == '+':
            operand_list.insert(i,n1+n2)
        elif op == '-':
            operand_list.insert(i,n1-n2)
        elif op == '*':
            operand_list.insert(i,n1*n2)
        elif n2:
            operand_list.insert(i,n1/n2)
        else:
            return 'Error'
        
        return bodmas(operator_list, operand_list)
        
    else:
        return operand_list[0]
	


class AdvancedCalculator(SimpleCalculator):
	
	def __init__(self):
		self.history = []

	def evaluate_expression(self, input_expression):
		
		res = self.evaluate_list_tokens(self.tokenize(input_expression))
		self.history.insert(0,(input_expression, res))
		return res

	def tokenize(self, input_expression):
		
		tokens = []
		f = 1
		for i in input_expression:
			if i == " ":
				if tokens:
					if str(tokens[-1]).isnumeric():
						f = 0
				continue
			elif i.isnumeric():
				if tokens:
					if str(tokens[-1]).isnumeric() and f:
						tokens[-1] = tokens[-1]*10 + int(i)
					else:
						tokens.append(int(i))
						f = 1
				else:
					tokens.append(int(i))
			else:
				tokens.append(i)	
				f = 1
		return tokens

	def check_brackets(self, list_tokens):

		cu_op = 0
		cu_cl = 0
		ro_op = 0
		ro_cl = 0
		flag = True
		for i in list_tokens:
			
			if i == '{':
				cu_op += 1
				if ro_op>ro_cl:
					flag = False
					break

			elif i == '}':
				cu_cl += 1
				if cu_op < cu_cl:
					flag = False
					break

			elif i == '(':
				ro_op += 1

			elif i == ')':
				ro_cl += 1
				if ro_op<ro_cl:
					flag = False
					break
		
		if cu_op != cu_cl or ro_op != ro_cl:
			flag = False

		return flag
	
	def evaluate_list_tokens(self, list_tokens):
		
		operators = Stack()
		operands = Stack()
		if self.check_brackets(list_tokens):
			try:
				c = -1
				n = len(list_tokens)
				for i in list_tokens:
					
					c += 1
					if str(i).isnumeric():
						operands.push(i)
						if c<n-1:
							if str(list_tokens[c+1]).isnumeric():
								return 'Error'
					elif i in '+-*/{(':
						operators.push(i)
						if c<n-1:
							if str(list_tokens[c+1]) in '+-*/})':
								return 'Error'
				
					elif i == ')' :
						if str(list_tokens[c-1]) in '{(+-*/':
							return 'Error'
						if c<n-1:
							if str(list_tokens[c+1]).isnumeric():
								return 'Error'
						op = operators.pop()
						operator_list = []
						operand_list = []
						while op != '(':
							operator_list.append(op)
							operand_list.append(operands.pop())
							op = operators.pop()
						a = operands.pop()
						operand_list.append(a)
						if a != None:
							res = bodmas(operator_list, operand_list)
							if res == 'Error':
								return 'Error'
							else:
								operands.push(res) 
						else:
							return 'Error'	
						
					elif i == '}':
						if str(list_tokens[c-1]) in '{(+-*/':
							return 'Error'
						if c<n-1:
							if str(list_tokens[c+1]).isnumeric():
								return 'Error'
						
						operator_list = []
						operand_list = []
						op = operators.pop()
						while op != '{':
							operator_list.append(op)
							operand_list.append(operands.pop())
							op = operators.pop()
						a = operands.pop()
						operand_list.append(a)
						if a != None:
							res = bodmas(operator_list, operand_list)
							if res == 'Error':
								return 'Error'
							else:
								operands.push(res) 
						else:
							return 'Error'	
					
				operator_list = []
				operand_list = []
				while operators:
					
					op = operators.pop()
					operator_list.append(op)
					operand_list.append(operands.pop())
				a = operands.pop()
				operand_list.append(a)
				
				if a != None:
					res = bodmas(operator_list, operand_list)
					if res == 'Error':
						return 'Error'
					else:
						operands.push(res) 
				else:
					return 'Error'	
						
				return operands.peek()
					
			except:
				return 'Error'

		else:
			return 'Error'
			

	def get_history(self):
		return self.history

calci = AdvancedCalculator()
print(calci.evaluate_expression('  4657 *(6557/(75/88))'))