#Binary Tree

class BinaryTreeNode:
	def __init__(self, data):
		self.data = data	#root_node
		self.left = None
		self.right = None

	#additional functions
	def setData(self, data):
		self.data = data
	def getData(self):
		return self.data
	def getLeft(self):
		return self.left
	def getRight(self):
		return self.right

#Binary Tree traversal
#Recursive

class BinaryTree:
	def __init__(self, root=None):
		self.root = root

	def preOrder(self, root):
		if root == None:
			return
		print (root.data, sep='-->',end='-->')
		self.preOrder(root.left)
		self.preOrder(root.right)

	def inOrder(self, root):
		if root == None:
			return
		self.inOrder(root.left)
		print(root.data, sep='-->', end='-->')
		self.inOrder(root.right)

	def postOrder(self, root):
		if root == None:
			return
		self.postOrder(root.left)
		self.postOrder(root.right)
		print(root.data, sep='-->',end='-->')
