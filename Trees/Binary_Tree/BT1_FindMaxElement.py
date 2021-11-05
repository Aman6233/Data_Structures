#Problem-1,2: Find the max element in BT

#Recursive
maxData = float('-inf')		# -infinity

def findMaxRecurrsive(root):
	global maxData
	if not root:
		return maxData

	if root.data > maxData:
		maxData = root.data
	findMaxRecurrsive(root.left)
	findMaxRecurrsive(root.right)
	return maxData


#Non-Recursive
def findMaxUsingLevelOrder(root):
	if root is None:
		return 
	q = Queue()
	q.enQueue(root)
	node = None
	maxElement = 0

	while not q.isEmpty():
		node = q.deQueue()
		if node.data > maxElement:
			maxElement = node.data

		if node.left is not None:
			q.enQueue(node.left)
		if node.right is not None:
			q.enQueue(node.right)
	return maxElement
