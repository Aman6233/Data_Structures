#Problem-35: Given a tree with a special property where leaves are represented with 'L' and internal node with 'I'.
			#Also each node has either 0 or 2 children. Given preorder traversal of this tree, construct the Tree.
			#Construction with preorder only is possible for this case only.

import Binary_Tree as BT

i = 0
def buildTreeFromPreOrder(arr):
	global i
	if arr == None or i >= len(arr):
		return None
	newNode = BT.BinaryTreeNode(arr[i])
	#newNode.data = arr[i]
	if arr[i] == 'L':
		return newNode

	i += 1
	newNode.left = buildTreeFromPreOrder(arr)
	i += 1
	newNode.right = buildTreeFromPreOrder(arr)

	return newNode

# ['I','I','L','I','L','L','I','L','L']
root = buildTreeFromPreOrder(['I','L','I','L','L'])
tree = BT.BinaryTree(root)
print(tree.postOrder(root))
tree.inOrder(root)

