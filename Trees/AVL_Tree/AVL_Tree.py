# AVL tree declaration

''' The AVL declaration is similar to BST but we include the height as a part of the declaration to simlipfy the operations '''

class AVLNode:
	def __init__(self, data, balanceFactor, left, right):
		self.data = data
		self.balanceFactor = balanceFactor		# -1 or 0 or 1
		self.left = left 						# or None
		self.right = right						# or None

# balanceFactor: 1, right height is greater
# balanceFactor: 0, left and right heights are equal
# balanceFactor: -1, left height is greater