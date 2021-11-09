#Find minimum element in Binary Search Tree

#Recursive

def findMin(root):
	currentNode = root
	if currentNode.left is None:
		return currentNode
	else:
		return findMin(currentNode.left)

#Non-recursive

def findMinElement(root):
	currentNode = root
	if currentNode is None:
		return None
	while currentNode.left is not None:
		currentNode = currentNode.left

	return currentNode