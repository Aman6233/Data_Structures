#Problem-98: Find second largest element in a given BST.

''' Perform RDL In-order traversal. This will give the elements in desceneding order that means we need second element. '''

count = 0
def secondLargest(root):
	global count
	if not root:
		return None
	right = secondLargest(root.right)
	if right:
		return right
	count += 1
	if count == 2:
		return root.data

	return secondLargest(root.left)

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrder(root):
	if not root:
		return
	inOrder(root.left)
	print(root.data, end=' ')
	inOrder(root.right)

if __name__ == '__main__':
	root = Node(5)
	root.left = Node(4)
	root.right = Node(7)
	root.left.left = Node(3)
	root.right.left = Node(6)
	root.right.right = Node(9)
	root.right.right.left = Node(8)

	inOrder(root)
	print()
	root1 = secondLargest(root)
	print(root1)

