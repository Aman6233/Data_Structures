#Problem-28: Find LCA (Least Common Ancestor) of two nodes in a Binary Tree

class newNode:
 
    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, alpha, beta):
	if not root:
		return None
	if root.data == alpha or root.data == beta:
		return root

	left = lca(root.left, alpha, beta)
	right = lca(root.right, alpha, beta)
	
	if left and right:
		return root		# alpha and beta are on both sides

	else:
		return left if left else right		# EITHER alpha/beta is on one side OR alpha/beta is not in L&R subtrees


root = newNode(10)											#		    10
root.left = newNode(28)										#		  /   \
root.right = newNode(13)									#		 /     \
															#		28     13
root.right.left = newNode(14)								#			  /   \
root.right.right = newNode(15)								#			14     15
															#		   / \     / \
root.right.left.left = newNode(21)							#		  /   \   /   \
root.right.left.right = newNode(22)							#		 21   22 23   24
root.right.right.left = newNode(23)
root.right.right.right = newNode(24)

print(lca(root, 21, 15).data)