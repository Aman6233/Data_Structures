# Insertion into an AVL tree / Full implementation.
# GeeksForGeeks

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1			# Tree height

# AVL class which supports Insertion
class AVL_Tree(object):
	def __init__(self):
		self.root = None
		
	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	def getBalance(self, root):
		if not root:
			return 0
		return self.getHeight(root.right) - self.getHeight(root.left)		# in GeeksforGeeks, +ve BFs are taken for left

	def leftRotate(self, root):
		x = root.right
		root.right = x.left
		x.left = root

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

		return x

	def rightRotate(self, root):
		x = root.left
		root.left = x.right
		x.right = root

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
		
		return x

	def insert(self, root, key):

		# step-1 perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# step-2 update height of ancestor
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

		# step-3 Get balance factor
		balance = self.getBalance(root)

		# step-4 if node is unbalanced
		# Case-1: Left Left
		if balance < -1 and key < root.left.val:
			return self.rightRotate(root)

		# Case-2: Right Right
		if balance > 1 and key > root.right.val:
			return self.leftRotate(root)

		# Case-3: Left Right
		if balance < -1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case-4: Right Left
		if balance > 1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def preOrder(self, root):
		if not root:
			return

		print('{0}'.format(root.val), end = ' ')
		self.preOrder(root.left)
		self.preOrder(root.right)

	def inOrder(self, root):
		if not root:
			return

		self.inOrder(root.left)
		print('{0}'.format(root.val), end = ' ')
		self.inOrder(root.right)

if __name__ == '__main__':

	myTree = AVL_Tree()
	root = None
	 
	root = myTree.insert(root, 10)
	root = myTree.insert(root, 20)
	root = myTree.insert(root, 30)
	root = myTree.insert(root, 40)
	root = myTree.insert(root, 50)
	root = myTree.insert(root, 25)

	myTree.preOrder(root)
	print()
	myTree.inOrder(root)

			