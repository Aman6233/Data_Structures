#Problem-26: Convert a tree to its mirror

def mirrorOfBinaryTree(root):
	if root != None:
		mirrorOfBinaryTree(root.left)
		mirrorOfBinaryTree(root.right)

		temp = root.left
		root.left = root.right
		root.right = temp
	return root