#Problem-72: Given root of a BST, trim the tree so that all elements in new tree are between the range A and B.

''' Another way of problem 69 (BST10) '''

from Binary_Search_Tree import BSTNode

def inorder(root):
	if not root: return
	inorder(root.left)
	print(root.data)
	inorder(root.right)

root = BSTNode(20)
root.left = BSTNode(8)
root.right = BSTNode(22)	
root.right.left = BSTNode(21)
root.left.left = BSTNode(4)
root.left.right = BSTNode(12)
root.left.right.left = BSTNode(10)
root.left.right.right = BSTNode(14)

def trimBST(root, minValue, maxValue):
	if not root:
		return 
	root.left = trimBST(root.left, minValue, maxValue)
	root.right = trimBST(root.right, minValue, maxValue)

	if minValue <= root.data <= maxValue:         
		return root
	if root.data < minValue:
		return root.right
	if root.data > maxValue:         
		return root.left

r = trimBST(root, 12, 22)
inorder(r)
