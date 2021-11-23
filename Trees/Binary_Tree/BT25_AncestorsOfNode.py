#Problem-31: Find all the Ancestors of a node in Binary Tree.

class newNode:
 
    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printAllAncestors(root, node):
	if not root:
		return False
	if root.data == node:
		return True
	if printAllAncestors(root.left, node) or printAllAncestors(root.right, node):
		print(root.data, sep=' ', end=' ')
		return True		

	return False


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

printAllAncestors(root, 24)