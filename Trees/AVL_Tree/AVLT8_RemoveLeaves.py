#Problem-90: Given a Binary Tree, remove leaves.

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


def removeLeaves(root):
	if not root:
		return None
	if not root.left and not root.right:
		return None
	else:
		root.left = removeLeaves(root.left)
		root.right = removeLeaves(root.right)

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
	root1 = removeLeaves(root)
	inOrder(root1)