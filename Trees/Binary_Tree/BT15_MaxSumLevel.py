#Problem-19: Find the level that has max sum in Binary Tree

from BinaryTree_LevelOrderTraversal import Queue
class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None

def findLevelWithMaxSum(root):
	if root is None:
		return 0

	q = Queue()
	q.enQueue(root)
	q.enQueue(None)
	node = None
	level = maxLevel = currentSum = maxSum = 0
	while not q.isEmpty():
		node = q.deQueue()
		if node == None:
			if currentSum > maxSum:
				maxSum = currentSum
				maxLevel = level

			currentSum = 0
			if not q.isEmpty():
				q.enQueue(None)
				level += 1
		else:
			currentSum += node.data
			if node.left is not None:
				q.enQueue(node.left)
			if node.right is not None:
				q.enQueue(node.right)

	return maxLevel


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

# Constructed Binary tree is:
#              1
#            /   \
#          2      3
#        /  \      \
#       4    5      8
#                 /   \
#                6     7   
print("Maximum level sum is", findLevelWithMaxSum(root))
