#Problem-91: Remove elements from the BST that are not within a given range.

def pruneBST(root, A, B):
	if not root:
		return None
	root.left = pruneBST(root.left,A,B)
	root.right = pruneBST(root.right,A,B)
	if A <= root.data and root.data <= B:
		return root
	if root.data < A:
		return root.right
	if root.data > B:
		return root.left


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
	root = Node(5)
	root.left = Node(4)
	root.right = Node(7)
	root.left.left = Node(3)
	root.right.left = Node(6)
	root.right.right = Node(8)

	inOrder(root)
	print()
	root1 = pruneBST(root,5,7)
	inOrder(root1)