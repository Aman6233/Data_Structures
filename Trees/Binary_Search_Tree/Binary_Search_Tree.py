#Binary Search Tree class and its method

class BSTNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def setData(self, data):
		self.data = data

	def getData(self, data):
		return self.data

	def getLeft(self):		#get left child of a node
		return self.left

	def getRight(self):		#get right child of a node
		return self.right