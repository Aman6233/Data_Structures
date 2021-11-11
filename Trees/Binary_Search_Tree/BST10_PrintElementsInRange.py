#Problem-69,70: Print all the elements of BST in range K1 and K2

from Binary_Search_Tree import BSTNode

root = BSTNode(20)
root.left = BSTNode(8)
root.right = BSTNode(22)	
root.right.left = BSTNode(21)
root.left.left = BSTNode(4)
root.left.right = BSTNode(12)
root.left.right.left = BSTNode(10)
root.left.right.right = BSTNode(14)

#Recursive
def rangePrinter(root, K1, K2):
	if not root:
		return

	if K1 <= root.data <= K2:
		rangePrinter(root.left, K1, K2)
		print(root.data, end= ' ')
		rangePrinter(root.right, K1, K2)

	if root.data < K1:
		rangePrinter(root.right, K1, K2)

	if root.data > K2:
		rangePrinter(root.left, K1, K2)

rangePrinter(root, 12, 22)

#Non-recursive
# import sys
# sys.path.insert(0,"D:/Python/Data Structures/Trees/Binary_Tree/")
# from BinaryTree_LevelOrderTraversal import Queue
import queue

def rangePrinterNonRecursive(root, K1, K2):
	if not root:
		return
	q = queue.Queue()
	q.put(root)				#enqueue
	temp = None
	while not q.empty():
		temp = q.get()		#dequeue
		if K1 <= temp.data <= K2:
			print(temp.data, end= ' ')
		if temp.left and temp.data >= K1:		# node > K2 will get covered here
			q.put(temp.left)
		if temp.right and temp.data <= K2:		# node < K1 will get covered here
			q.put(temp.right)

print()
rangePrinterNonRecursive(root, 12, 22)