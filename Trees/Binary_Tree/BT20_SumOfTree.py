#Problem-24,25: Find the Sum of all elements in Binary Tree

#Recursive
def sumInBinaryTreeRecursive(root):
	if not root:
		return 0
	return (root.data + sumInBinaryTreeRecursive(root.left) + sumInBinaryTreeRecursive(root.right))


#Non-recursive
def sumInBinaryTreeLevelOrder(root):
	if not root:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	sum = 0
	while not q.isEmpty():
		node = q.deQueue()
		sum += node.data
		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)
	return sum
