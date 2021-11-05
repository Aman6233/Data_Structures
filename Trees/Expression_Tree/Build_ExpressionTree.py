# Expression tree is a Binary Tree whose internal nodes are operators and leaves are operands.

# Algorithm for building Expression Tree from Postfix Expression
# stack = [] postfix = [A, B, C, *, +, D, /]  (a+b*c)/d 	d+a*b/c
 
operatorPrecedence = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2, '^':3}

def postfixConvert(infix):
	stack = []
	postfix = []

	for char in infix:
		if char not in operatorPrecedence:
			postfix.append(char)
		else:
			if len(stack) == 0:
				stack.append(char)
			else:
				if char == '(':
					stack.append(char)
				elif char == ')':
					while stack[-1] != '(' and len(stack) != 0:		#GeeksForGeeks
						postfix.append(stack.pop())
					stack.pop()
				# elif operatorPrecedence[char] > operatorPrecedence[stack[-1]]:	#This will get covered in else body
				# 	stack.append(char)
				else:
					while len(stack) != 0 and operatorPrecedence[char] <= operatorPrecedence[stack[-1]]:	#GeeksForGeeks
						if stack[-1] == '(':
							break
						postfix.append(stack.pop())
					stack.append(char)
	
	while len(stack) != 0:
		postfix.append(stack.pop())

	return postfix

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class ExpressionTree(object):
	def __init__(self, root = None):
		self.__root = root
	
	def inorder(self):
		self.__inorderHelper(self.__root)
	
	def __inorderHelper(self, node):
		if node:
			self.__inorderHelper(node.left)
			print(node.value, sep = ' ', end = ' ')
			self.__inorderHelper(node.right)

	def preorder(self):
		self.__preorderUtil(self.__root)
	
	def __preorderUtil(self, node):
		if node:
			print(node.value, sep = ' ', end = ' ')
			self.__preorderUtil(node.left)
			self.__preorderUtil(node.right)

	def postorder(self):
		self.__postorderUtil(self.__root)

	def __postorderUtil(self, node):
		if node:
			self.__postorderUtil(node.left)
			self.__postorderUtil(node.right)
			print(node.value, sep = ' ', end = ' ')

def buildExpressionTree(infix):
	postfix = postfixConvert(infix)
	stack = []
	for char in postfix:
		if char not in operatorPrecedence:
			node = Node(char)
			stack.append(node)
		else:
			node = Node(char)
			right = stack.pop()
			left = stack.pop()
			node.left = left
			node.right = right
			stack.append(node)
	return ExpressionTree(stack.pop())

res = buildExpressionTree('(5+3)*6')
print('\nInorder:')
res.inorder()
print('\nPreorder:')
res.preorder()
print('\nPostorder:')
res.postorder()