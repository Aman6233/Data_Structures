#Problem-86,87: Find the element in BST which is closest to the given key.

import sys
import math
import queue
import AVL_Tree_InsertNode as avl

#Non-recursive
def closestInBST(root, key):
	difference = sys.maxsize
	element = None
	if not root:
		return None
	q = queue.Queue()
	q.put(root)
	while not q.empty():
		temp = q.get()
		if difference > abs(temp.val - key):
			difference = abs(temp.val - key)
			element = temp
		if temp.left:
			q.put(temp.left)
		if temp.right:
			q.put(temp.right)

	return element

#Recursive
def closestInBST1(root, key):
	if not root:
		return None
	if root.val == key:
		return root
	if key < root.val:
		if not root.left:
			return root
		temp = closestInBST1(root.left, key)
		if abs(temp.val - key) > abs(root.val - key):
			return root
		else:
			return temp

	else:
		if not root.right:
			return root
		temp = closestInBST1(root.right, key)
		if abs(temp.val - key) > abs(root.val - key):
			return root
		else:
			return temp
	return None

if __name__ == '__main__':

	myTree = avl.AVL_Tree()
	root = None
	 
	root = myTree.insert(root, 10)
	root = myTree.insert(root, 20)
	root = myTree.insert(root, 30)
	root = myTree.insert(root, 40)
	root = myTree.insert(root, 50)
	root = myTree.insert(root, 25)

	print(closestInBST(root, 29).val)
	print(closestInBST1(root, 29).val)
