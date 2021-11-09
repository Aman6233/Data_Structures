#Deleting an element from BST

def findMin(root, parent):
	if root.left:
		return findMin(root.left, root)
	else:
		return [parent, root]

def deleteNode(root, data):		#delete node and return the root of the tree
	if root.data == data:
		if root.right and root.left:
			[psucc, succ] = findMin(root.right, root)		#get the successor node and its parent

			#splice out the succcessor (we need the parent to do this)
			if psucc.left == succ:
				psucc.left = succ.right

			else:
				psucc.right = succ.right

			#reset left and right children of the successor
			succ.left = root.left
			succ.right = root.right
			return succ

		else:
			#easier case
			if root.left:
				return root.left
			else:
				return root.right

	else:
		if root.data > data:
			if root.left:
				root.left = deleteNode(root.left, data)
		else:
			if root.right:
				root.right = deleteNode(root.right, data)

	return root