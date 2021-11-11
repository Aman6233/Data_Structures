#Problem-64: Find kth smallest element in BST

from Binary_Search_Tree import BSTNode

root = BSTNode(20)
root.left = BSTNode(8)
root.right = BSTNode(22)	
root.left.left = BSTNode(4)
root.left.right = BSTNode(12)
root.left.right.left = BSTNode(10)
root.left.right.right = BSTNode(14)

count = 0
def kthSmallestInBST(root, k):
	global count
	# print(count,root)
	# if root:
	# 	print(root.data)
	if not root:
		return None

	node = kthSmallestInBST(root.left, k)   		# 8-> 4-> none i.e 8-> none   # 12-> 10-> None
	# print('r', root.data)
	if node:
		# print('node',node.data, root.data)
		return node 								# returns value to itself till root of tree is reached and then returns final value

	count += 1
	if count == k:
		# print('k')
		return root									# returns the value to node variable

	return kthSmallestInBST(root.right, k)			# this is also getting returned into node variable

print(kthSmallestInBST(root, 3).data)