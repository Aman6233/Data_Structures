#Problem-49: For a given Binary Tree (not threaded), find the preorder successor.

def perorderSuccessor(node):
	S = Stack()
	if node != None:
		P = node
		if P.left != None:
			push(S, P)
			P = P.left
		else:
			while (P.right == None):
				P = pop(S)
			P = P.right
		return P