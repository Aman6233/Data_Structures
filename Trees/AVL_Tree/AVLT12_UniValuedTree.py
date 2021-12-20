#Problem-99: Check whether the given BT is an uni-valued tree or not.

def isUnivaluedTree(root):
	isLeft = (not root.left or root.data == root.left.data and isUnivaluedTree(root.left))
	isRight = (not root.right or root.data == root.right.data and isUnivaluedTree(root.right))

	return isLeft and isRight

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrder(root):
	if not root:
		return
	inOrder(root.left)
	print(root.data, end=' ')
	inOrder(root.right)

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(1)
	root.right = Node(1)
	root.left.left = Node(1)
	root.right.left = Node(1)
	root.right.right = Node(1)
	root.right.right.left = Node(1)

	inOrder(root)
	print()
	root1 = isUnivaluedTree(root)
	print(root1)