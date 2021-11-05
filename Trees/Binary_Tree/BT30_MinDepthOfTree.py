#Problem-38: Find minimum depth of of a Binary Tree 
#(The min depth is the no. of nodes along the shortest path from the root node down to the nearest leaf node)

class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#Recursive-1
def minimumDepth(root):
	if root == None:
		return 0
	if root.left == None or root.right == None:
		return minimumDepth(root.left) + minimumDepth(root.right) +1
	return min(minimumDepth(root.left), minimumDepth(root.right)) +1

print ('Recursive-1 ',minimumDepth(root))

#Recursive-2
def minDepth(root):
	if root == None:
		return 0
	if root.left is None and root.right is None:
		return 1
	if root.left is None:
		return minDepth(root.right) +1
	if root.right is None:
		return minDepth(root.left) +1

	return min(minDepth(root.left), minDepth(root.right)) +1

print ('Recursive-2 ',minDepth(root))

#Non-recursive
def min_depth(root):
	if root is None:
		return 0
	queue = []
	queue.append((root,1))
	while queue:
		current, depth = queue.pop(0)
		if current.left is None and current.right is None:
			return depth
		if current.left:
			queue.append((current.left, depth+1))
		if current.right:
			queue.append((current.right, depth+1))

print ('Non-recursive ',min_depth(root))