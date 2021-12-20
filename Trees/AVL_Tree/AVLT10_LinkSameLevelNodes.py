#Problem-92,93: Given a BT, connect adjacent nodes at same level. Assume BT has next pointer along with left and right as well.

import queue

class BTNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.next = None

def linkNodesOfSameLevel(root):
	q = queue.Queue()
	if not root:
		return None
	currentLevelNodeCount = 1
	nextLevelNodeCount = 0
	prev = None
	q.put(root)
	while (not q.empty()):
		temp = q.get()
		if temp.left:
			q.put(temp.left)
			nextLevelNodeCount += 1
		if temp.right:
			q.put(temp.right)
			nextLevelNodeCount += 1

		if prev:
			prev.next = temp
		prev = temp
		currentLevelNodeCount -= 1
		if currentLevelNodeCount == 0:					#last node of current level
			currentLevelNodeCount = nextLevelNodeCount
			nextLevelNodeCount = 0
			prev = None

