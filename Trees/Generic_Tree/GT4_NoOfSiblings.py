#Problem-44: Count the no. of siblings for a given node

class GenericTreeNode:
	def __init__(self, data):
		self.data = data
		self.firstChild = None
		self.nextSibling = None

root = GenericTreeNode(1)
root.firstChild = GenericTreeNode(2)
root.firstChild.nextSibling = GenericTreeNode(3)
node3 = root.firstChild.nextSibling.nextSibling = GenericTreeNode(4)
root.firstChild.nextSibling.firstChild = GenericTreeNode(5)

def siblingsCount(node):		# This will not count prev. siblings
	count = 0
	while node:
		count += 1
		node = node.nextSibling
	return count

print('siblingsCount',siblingsCount(node3))

# With generic tree representation(GT1), we can count the siblings of a given node with below code.

class GenericTree:
	def __init__(self, parent, value=None):
		self.parent = parent
		self.value = value
		self.childList = []
		if parent is None:
			self.birthOrder = 0
		else:
			self.birthOrder = len(parent.childList)
			parent.childList.append(self)

	def nChildren(self):
		return len(self.childList)

	def siblingsCount1(self):	# This will count prev. siblings also
		if self.parent is None:
			return 1
		else:
			return self.parent.nChildren()

root = GenericTree(None,1)
node1 = GenericTree(root,2)
node2 = GenericTree(root,3)
node3 = GenericTree(root,4)
node4 = GenericTree(node2,5)

print('siblingsCount1',node2.siblingsCount1())