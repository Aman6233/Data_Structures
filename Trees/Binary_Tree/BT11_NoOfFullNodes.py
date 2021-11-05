#Problem-15: Find the no. of full nodes in BT without using recursion

def numberOfFullNodesInBinaryTreeUsingLevelOrder(root):
	if root is None:
		return 0

	q = Queue()
	q.enQueue(root)
	node = None
	count = 0

	while not q.isEmpty():
		node = q.deQueue()
		if node.left is not None and node.right is not None:
			count += 1

		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)
	return count