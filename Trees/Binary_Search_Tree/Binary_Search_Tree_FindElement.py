#Find an element in Binary Search Tree

#Recursive
def search(root, data):
	if root is None or root.data == data:
		return root
	if data > root.data:
		return search(root.right, data)
		
	return search(root.left, data)


#Non-recursive

#Solution-1
def find(root, data):
	currentNode  = root
	while currentNode:
		if data == currentNode.data:
			return currentNode
		if data < currentNode.data:
			currentNode = currentNode.left
		else: 
			currentNode = currentNode.right

	return None

#Solution-2
def findElement(root, data):
	currentNode = root
	while currentNode is not None and data != currentNode.data:
		if data > currentNode.data:
			currentNode = currentNode.right
		else:
			currentNode = currentNode.left

	return currentNode