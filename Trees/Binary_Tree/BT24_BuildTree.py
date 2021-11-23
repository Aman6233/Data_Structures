#Problem-29: Construct Binary Tree from given Inorder and Preorder traversals

#Solution-1
from Binary_Tree import BinaryTree 

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Solution:
	def buildTree(self, preorder, inorder):
		if not inorder:
			return None
		root = TreeNode(preorder[0])
		rootPos = inorder.index(preorder[0])
		root.left = self.buildTree(preorder[1: 1+rootPos], inorder[:rootPos])
		root.right = self.buildTree(preorder[1+rootPos:], inorder[rootPos+1:])

		return root

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
tree = Solution()
root = tree.buildTree(preOrder, inOrder)
BT = BinaryTree(root)
print(root.data)
print(BT.inOrder(root))
print(BT.preOrder(root))
print(BT.postOrder(root))
