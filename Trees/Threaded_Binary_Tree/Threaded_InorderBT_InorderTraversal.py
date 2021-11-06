#Find Inorder successor in Inorder Threaded Binary Tree

''' Strategy: If P(node) has no right subtree, return right child of P. If P has right subtree, return the left of the nearset node 
	whose left subtree(predecessor) contains P '''

def inorderSuccessor(P):
	if P.RTag == 0:
		return P.right	# will point to dummy node

	else:
		Position = P.right
		while Position.LTag == 1:
			Position = Position.left

		return Position

#Inorder Traversal in Inorder Threaded Binary Tree

''' We start with dummy node and call inordeSuccessor() to visit each node untill we reach dummy node. '''

def inorderTraversal(root):		# root is dummy node
	P = inorderSuccessor(root)
	while P != root:
		print (P.data)
		P = inorderSuccessor(P)

#Alternate coding

def inorderTraversal1(root):
	P = root
	while (1):
		P = inorderSuccessor(P)
		if P == root:
			return
		print (P.data)
