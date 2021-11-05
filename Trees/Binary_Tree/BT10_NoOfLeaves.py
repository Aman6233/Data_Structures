#Problem-14: Find the no. of leaves in BT without using recursion

def leavesInBinaryTreeUsingLevelOrder(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	count = 0

	while not q.isEmpty():
		node = q.deQueue()
		if node.left is None and node.right is None:
			count += 1
		else:
			if node.left is not None:
				q.enQueue(node.left)
			if node.right is not None:
				q.enQueue(node.right)
	return count

