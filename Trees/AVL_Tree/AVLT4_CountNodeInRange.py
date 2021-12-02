#Problem-83: Given an AVL with n integer items and two integers a and b (a<=b). Count no. of nodes in range [a,b].

import AVL_Tree_InsertNode as avl

def rangeCount(root, a, b):
	if root == None:
		return 0

	elif root.val > b:
		return rangeCount(root.left, a, b)
	elif root.val < a:
		return rangeCount(root.right, a, b)

	elif root.val >= a and root.val <= b:
		return rangeCount(root.left, a, b) + rangeCount(root.right, a, b) +1

if __name__ == '__main__':

	myTree = avl.AVL_Tree()
	root = None
	 
	root = myTree.insert(root, 10)
	root = myTree.insert(root, 20)
	root = myTree.insert(root, 30)
	root = myTree.insert(root, 40)
	root = myTree.insert(root, 50)
	root = myTree.insert(root, 25)

	myTree.preOrder(root)
	print()
	print(rangeCount(root, 10, 30))
