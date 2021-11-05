#Problem-12: Find deepest node of Binary Tree

def deepestNode(root):
	if root == None:
		return 0

	q = Queue()
	q.enQueue(root)
	node = None
	while not q.isEmpty():
		node = q.deQueue()
		if node.left is not None:
			q.enQueue(root.left)
		if node.right is not None:
			q.enQueue(root.right)

	return node.data

