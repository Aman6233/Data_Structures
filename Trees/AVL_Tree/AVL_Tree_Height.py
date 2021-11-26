# Height of the AVL tree

class AVLNode:
	def __init__(self, data, balanceFactor, left, right):
		self.data = data
		self.balanceFactor = balanceFactor		# 0 or 1
		self.left = left 						# or None
		self.right = right

	def height(self):
		return recHeight(self.root)

	def recHeight(self, root):
		if not root:
			return 0

		else:
			leftH = recHeight(root.left)
			rightH = recHeight(root.right)

			if leftH > rightH:
				return 1 + leftH
			else:
				return 1 + rightH