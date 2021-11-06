#Find Preorder successor in Inorder Threaded Binary Tree

''' Strategy: If P(node) has a left subtree, then return the left child of P. If P has no left subtree, then return the right child of the nearest node
	whose left subtree contains P. 
	In other words, If left child exists, then the left child is preoder successor. If left child does not exist and the given node is left child of its
	parent, then its sibling is its preorder successor'''

def preorderSuccessor(P):
	if P.LTag == 1:
		return P.left

	else:
		Position = P
		while Position.RTag == 0:
			Position = Position.right

		return Position.right

#Preorder Travesal in Inorder Threaded Binary Tree

''' As in inorder traversal, start with dummy node and call inordeSuccessor() to visit each node untill we reach dummy node. '''

def preorderTraversal(root):
	P = preorderSuccessor(root)
	while P != root:
		print (P.data)
		P = preorderSuccessor(P)

#Alternate coding

def preorderTraversal1(root):
	P = root
	while (1):
		P = preorderSuccessor(P)
		if P == root:
			return
		print (P.data)
