#Problem-43: Given a parrent array P, where P[i] indicates the parent of ith node in the tree (parent of root is -1). Find height/depth of tree

def depthInGenericTree(P):
	maxDepth = -1
	currentDepth = -1
	for i in range(len(P)):
		currentDepth = 0
		j = i
		while P[j] != -1:
			currentDepth += 1
			j = P[j]
		if currentDepth > maxDepth:
			maxDepth = currentDepth
	return maxDepth

P = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
print(depthInGenericTree(P))