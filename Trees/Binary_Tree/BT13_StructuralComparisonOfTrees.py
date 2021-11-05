#Problem-17: Given two Binary Trees, return True if they are structurally identical

#If both trees are None then return True
#If both trees are not None, then compare data and recursively check left and right subtree structures

def areStructurallySameTrees(root1, root2):
	if (not root1.left) and (not root2.left) and (not root1.right) and (not root2.right) and (root1.data == root2.data):
		return True

	if (root1.data != root2.data) or (root1.left and not root2.left) or (not root1.left and root2.left) or (root1.right and not root2.right) or (not root1.right and root2.right):
		return False

	left = areStructurallySameTrees(root1.left, root2.left) if root1.left and root2.left else True      #Block-1
	if root1.right and root2.right:																		#Block-2
		right = areStructurallySameTrees(root1.right, root2.right)
	else:
		True

#Block-1 and Block-2 are similar