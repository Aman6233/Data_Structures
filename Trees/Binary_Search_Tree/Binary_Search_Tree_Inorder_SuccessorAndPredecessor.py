#Find Inorder Predecessor and Successor in BST

''' -If X has 2 children, Inorder Predecessor is max of left subtree and Inorder Successor is min of right subtree.
	-If X does not have a left child, Inorder Predecessor is 1st left ancestor. '''

#Successor
def successorOfBST(node):
	temp = None
	if node.right:
		temp = node.right
		while temp.left:
			temp = temp.left
	return temp

#Predecessor
def prdecessorOfBST(node):
	temp = None
	if node.left:
		temp = node.left
		while temp.right:
			temp = temp.right
	return temp