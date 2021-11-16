#Problem-3,4: Search an element in BT

#Recursive
def findRecursive(root, data):
	if not root:
		return 0
	if root.data == data:
		return 1
	else:
		temp = findRecursive(root.left)
		if temp == 1:
			return temp
		else:
			return findRecursive(root.right)


#Non-Recursive
def findUsingLevelOrder(root, data):
	if root is None:
		return -1
	q = Queue()
	q.enQueue(root)
	node = None
	while not q.isempty():
		node = q.deQueue()
		if node.data == data:
			return 1
		if node.left is not None:
			q.enQueue(root.left)
		if node.right is not None:
			q.enQueue(root.right)
	return 0