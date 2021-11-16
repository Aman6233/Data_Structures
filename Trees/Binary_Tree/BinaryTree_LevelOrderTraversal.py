#BinaryTree_LevelOrderTraversal

class Queue:
	def __init__(self):
		self.array = []

	def enQueue(self, data):
		self.array.append(data)
	
	def deQueue(self):
		if len(self.array) == 0:
			return None
		return self.array.pop(0)

	def size(self):
		return len(self.array)

	def front(self):
		if len(self.array) == 0:
			return None
		return self.array[0]

	def isEmpty(self):
		return (len(self.array) == 0)

class BTNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = data
		self.right = right

class BinaryTree:
	def __int__(self, root):
		self.root = root

	def levelOrder(self, root):
		if root == None:
			return
		q = Queue()
		q.enQueue(root)
		while not q.isEmpty():
			temp = q.deQueue()
			print(temp.data, sep='-->',end='-->')
			if temp.left:
				q.enQueue(temp.left)
			if temp.right:
				q.enQueue(temp.right)