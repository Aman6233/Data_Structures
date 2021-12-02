#Problem-84,85: Given a BST (applicable to AVL trees as well) where each node contains two data elements (its data 
#			 	and also the number of nodes in its subtrees) as shown below. Convert the tree to another BST by replacing 
#			 	the second data element (number of nodes in its subtrees) with previous node data in inorder traversal. 
#			 	Note that each node is merged with inorder previous node data. Also make sure that conversion happens in-place.

''' Use level order. If left subtree is greater than right subtree, find max in left subtree and replace the current node 
	second data with it. Otherwise, find min in right subtree and replace the current node second data with it. '''

def treeCompression(root):		# in-efficient because for right node, root should be prev (i guess)
	if not root:
		return None
	q = Queue()
	q.enQueue(root)
	while not q.isEmpty():
		temp = q.deQueue()
		if temp.left and temp.right and (temp.left.data2 > temp.right.data2):
			temp2 = findMax(temp)
		elif temp.left and not temp.right:
			temp2 = findMax(temp)
		else:
			temp2 = findMin(temp)

		temp.data2 = temp2.data
		temp2 = None
		if temp.left:
			q.enQueue(temp.left)
		if temp.right:
			q.enQueue(temp.right)

# Alternate coding
import sys
def treeCompression1(root, prevNodeData):		# here, root is prev for right node
	global min
	if not root:
		return
	treeCompression1(root.left, prevNodeData)
	if prevNodeData == -sys.maxsize:
		prevNodeData = root.data
		free(root)					# frees the root pointer
	if prevNodeData != -sys.maxsize:
		root.data2 = prevNodeData
		prevNodeData = root.data
	return treeCompression1(root.right, prevNodeData)