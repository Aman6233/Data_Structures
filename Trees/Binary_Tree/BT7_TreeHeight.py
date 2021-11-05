#Problem-10,11: Find the height of the tree

#Recursive
def maxDepth(root):
	if root == None:
		return 0
	return max(maxDepth(root.left), maxDepth(root.right))+1


#Non-recursive
def maxDepthIterative(root):
	if root == None:
		return 0
	q = []
	q.append([root, 1])
	temp = 0
	while len(q) != 0:
		node, depth = q.pop()
		temp = max(temp,depth)
		if node.left != None:
			q.append([node.left, depth+1])
		if node.right != None:
			q.append([node.right, depth+1])

	return temp