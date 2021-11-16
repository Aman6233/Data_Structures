#Problem-8: Print Level order data in reverse order

def levelOrderTraversalInReverse(root):
	if not root:
		return 0
	q = Queue()
	s = Stack()
	q.enQueue(root)
	node = None
	while not q.isEmpty():
		node = q.deQueue()
		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)
		s.push(node)
	while not s.isEmpty():
		print(s.pop().data)