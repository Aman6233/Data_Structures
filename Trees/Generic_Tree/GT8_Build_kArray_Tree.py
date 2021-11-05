#Problem-48: A full k-ary tree is a tree where each node has either 0 or k children. Given an array which contains the preorder traversal of full k-ary tree,
# construct the full k-ary tree

''' In k-ary tree, for a node at ith position its children will be at (k*i + 1) to (k*i + k) '''

import sys

#import os
#sys.path.append(os.path.abspath("D:/Python/Data Structures/Trees/Binary_Tree"))

sys.path.insert(0,"D:/Python/Data Structures/Trees/Binary_Tree")	#either above 2 lines(with os) or this(without os)

from BinaryTree_LevelOrderTraversal import Queue

#from D:/Python/Data Structures/Trees/Binary_Tree/BinaryTree_LevelOrderTraversal import Queue

class KaryTreeNode:
	def __init__(self, data=None):
		self.data = data
		self.childList = []

def buildKaryTree(A, k):
	n = len(A)
	if n <= 0:
		return None
	index = 0
	root = KaryTreeNode(A[0])
	if not root:
		print('Memory error')
		return

	Q = Queue()
	print('q',Q)
	if Q == None:
		return None
		print('qa',Q)
	Q.enQueue(root)

	while (not Q.isEmpty()):
		temp = Q.deQueue()
		for i in range(0, k):
			index += 1
			if index < n:
				temp.childList.insert(i, KaryTreeNode(A[index]))	#  1-[2,3,4] 2-[5,6,7] 3-[8,9,10] 4-[11,12,13]
				Q.enQueue(temp.childList[i])
	return root

def preorderRecursive(kroot):
	if not kroot:
		return 0
	print(kroot.data)
	for node in kroot.childList:
		preorderRecursive(node)

A = [1,2,3,4,5,6,7,8,9,10,11,12,13]
kroot = buildKaryTree(A, 3)
preorderRecursive(kroot)
