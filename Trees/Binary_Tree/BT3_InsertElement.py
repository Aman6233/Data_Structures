#Problem-5: Insert an element in BT

class BinaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def setData(self):
		self.data = data
	def getData(self):
		return self.data
	def getLeft(self):		#get left child
		return self.left
	def getRight(self):
		return self.right

	#insert node
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp

# insertion using level order
def insertUsingLevelOrder(root, data):
	newNode = BinaryTree(data)
	if root is None:
		root = newNode
		return root
	q = Queue()
	q.enQueue(root)
	node = None
	while not q.isEmpty():
		node = q.deQueue()
		if data == node.data:
			return root
		if node.left is not None:
			q.enQueue(node.left)
		else:
			node.left = newNode
			return root
		if node.right is not None:
			q.enQueue(node.right)
		else:
			node.right = newNode
	return root