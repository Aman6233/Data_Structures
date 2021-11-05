#Problem-6,7: Find the size of BT

#Recursive
def findSizeRecursive(root):
	if not root:
		return 0
	return findSizeRecursive(root.left) + findSizeRecursive(root.right) + 1


#Non-recursive
def findSizeUsingLevelOrder(root):
	if root is None: 
		return 0
	q = Queue()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()
		count += 1
		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)

	return count