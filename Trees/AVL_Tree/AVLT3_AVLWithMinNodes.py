#Problem-82: Given a height h, generate an AVL tree with minimum no. of nodes

# It does not satisfy BST

from AVL_Tree_InsertNode import TreeNode, AVL_Tree

count = 1
def generateAVLTree(h):
	global count
	if h < 0:			# h<=0: height of root is 1 ; h<0: height of root is 0
		return None
	avlNode = AVL_Tree()
	avlNode.root = avlNode
	avlNode.left = generateAVLTree(h-2)
	avlNode.right = generateAVLTree(h-1)
	avlNode.val = count
	count += 1
	return avlNode

if __name__ == '__main__':

	Tree = generateAVLTree(3)
	print(Tree.preOrder(Tree.root))
	print(Tree.inOrder(Tree.root))