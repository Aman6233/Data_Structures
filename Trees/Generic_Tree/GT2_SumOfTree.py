#Problem-40: Find the sum of all elements in a Generic Tree

class GenericTreeNode:
	def __init__(self, data = None):
		self.data = data
		self.firstChild = None
		self.nextSibling = None

root = GenericTreeNode(1)
root.firstChild = GenericTreeNode(2)
root.firstChild.nextSibling = GenericTreeNode(3)
root.firstChild.nextSibling.nextSibling = GenericTreeNode(4)
root.firstChild.nextSibling.firstChild = GenericTreeNode(5)


if __name__ == '__main__':
	def findSum(root):
		if root == None:
			return 0
		return (root.data + findSum(root.firstChild) + findSum(root.nextSibling))

	print(findSum(root))