#Node of a Generic tree

class GenericTreeNode:
	def __init__(self, data = None):
		self.data = data
		self.firstChild = None
		self.nextSibling = None

# We can treat all generic trees with a first child/next sibling representation as binary trees.