#Inserting an element into BST

''' Find correct location for element and then insert. '''

def insertNode(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.left == None:
				root.left = node
			else:
				insertNode(root.left, node)
		else:
			if root.right == None:
				root.right = node
			else:
				insertNode(root.right, node)