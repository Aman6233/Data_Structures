#Find maximum element in Binary Search Tree

#Recursive

def findMax(root):
	if root.right is None:
		return root
	else:
		return findMax(root.right)


#Non-recursive

def findMaxElement(root):
	if root is None:
		return None
	while root.right is not None:
		root = root.right

	return root
