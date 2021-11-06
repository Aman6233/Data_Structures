#Problem-50: For a given Binary Tree (not threaded), find the inorder successor.

def inorderSuccessor(node):
	S = Stack()
	if node != None:
		P = node
		if P.right == None:
			P = pop(S)
		else:
			P = P.right
			while P.left != None:
				push(S, P)
				P = P.left
		return P