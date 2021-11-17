#Problem-9: Delete the Binary Tree

def deleteBinaryTree(root):
	if root==None:
		return

	deleteBinaryTree(root.left)
	deleteBinaryTree(root.right)
	del root