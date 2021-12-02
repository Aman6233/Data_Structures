#Problem-89: Given a Binary Tree, remove all Half Nodes(which have only 1 child). Note that leaves should not get touched.

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

def removeHalfNodes(root):
	if root is None:
		return None
	root.left = removeHalfNodes(root.left)
	root.right = removeHalfNodes(root.right)
	if not root.left and not root.right:
		return root
	if not root.left:
		return root.right
	if not root.right:
		return root.left

	return root


if __name__ == '__main__':
	root = Node(5)
	root.left = Node(4)
	root.right = Node(7)
	root.left.left = Node(3)
	root.right.left = Node(6)
	root.right.right = Node(8)

	inOrder(root)
	print()
	root1 = removeHalfNodes(root)
	inOrder(root1)
