#Problem-81: Given a BST, check whether it is an AVL tree or not (in other words a BT is height balanced or not)

# GeekForGeeks

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)


def height(root):
	if not root:
		return 0
	return max(height(root.left), height(root.right)) +1

def isBalanced(root):
	if not root:
		return True

	lh = height(root.left)
	rh = height(root.right)

	if (abs(lh-rh) <= 1) and isBalanced(root.left) and isBalanced(root.right):		# lh-rh: -1, 0, 1
		return True
	return False

if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")