#Problem-13: Delete an element from Binary Tree

def deleteElement(root, element):
	if root is None:
		return 0

	temp_node = None
	# if root.data == element:
	# 	temp_node = root
	
	q = Queue()
	q.enQueue(root)
	node = None

	while not q.isEmpty():
		node = q.deQueue()
		if node.data == element:
			temp_node = node

		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)

	temp_node.data = node.data
	del node

