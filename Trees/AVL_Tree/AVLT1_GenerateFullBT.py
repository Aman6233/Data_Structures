#Problem-77,78: Given a height h, give an algorithm for generating the HB(0) i.e. full binary tree.

from AVL_Tree_InsertNode import TreeNode, AVL_Tree

count = 0
def buildHB0(h):	# It generates BT but not BST
	global count
	if h <= 0:
		return None
	avlNode = AVL_Tree()
	avlNode.root = avlNode
	avlNode.left = buildHB0(h-1)
	avlNode.right = buildHB0(h-1)
	avlNode.val = count
	count += 1
	return avlNode

Tree = buildHB0(3)
print(Tree.preOrder(Tree.root))
print(Tree.inOrder(Tree.root))


#Alternate coding
''' Using mergeSort logic. That means, instead of working with height, we can take the range. Hence, we don't need any global 
	counter to be maitained. '''

def buildHB0_mergeSort(l, r):		# This generates BST
	mid = l + (r-l)//2
	if l>=r:
		return None

	avlNode = AVL_Tree()
	avlNode.root = avlNode
	avlNode.left = buildHB0_mergeSort(l, mid)
	avlNode.right = buildHB0_mergeSort(mid+1, r)
	avlNode.val = mid
	return avlNode

Tree = buildHB0_mergeSort(0,7)			# 0 <= a < 7
print(Tree.preOrder(Tree.root))
print(Tree.inOrder(Tree.root))
