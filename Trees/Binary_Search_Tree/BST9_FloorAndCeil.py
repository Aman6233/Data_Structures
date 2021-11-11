#Problem-65: Floor and ceiling (floor- node with data just lesser or equal to key) and (ceil- node with data just larger or equal to key)

import sys

from Binary_Search_Tree import BSTNode

root = BSTNode(20)
root.left = BSTNode(8)
root.right = BSTNode(22)	
root.left.left = BSTNode(4)
root.left.right = BSTNode(12)
root.left.right.left = BSTNode(10)
root.left.right.right = BSTNode(14)


def floorInBSTUtil(root, key):
	global maxint
	if not root:
		return sys.maxsize
	if root.data == key:
		return root.data
	if key < root.data:
		return floorInBSTUtil(root.left, key)

	floor = floorInBSTUtil(root.right, key)

	if floor <= key:
		return floor
	else:
		return root.data

def ceilInBSTUtil(root, key):
	if not root:
		return -sys.maxsize
	if root.data == key:
		return root.data
	if root.data < key:
		return ceilInBSTUtil(root.right, key)

	ceil = floorInBSTUtil(root.left, key)

	if ceil >= key:
		return ceil
	else:
		return root.data

print(floorInBSTUtil(root, 11))
print(ceilInBSTUtil(root, 11))