#Problem-36,37: Populate nextSibling pointer in Binary Tree assuming they are None initially.

from BinaryTree_LevelOrderTraversal import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.nextSibling = None

#Code-1
def fillNextSiblingsWithLevelOrderTraversal(root):
	if root == None:
		return 0
	q = Queue()
	q.enQueue(root)
	q.enQueue(None)
	node = None
	while not q.isEmpty():
		node = q.deQueue()
		if node == None:
			if not q.isEmpty():
				q.enQueue(None)
		else:
			node.nextSibling = q.front()
			if node.left is not None:
				q.enQueue(node.left)
			if node.right is not None:
				q.enQueue(node.right)

#Code-2
def fillNextSiblings(root):
	if root == None:
		return 0
	if root.left:
		root.left.nextSibling = root.right
	if root.right:
		if root.nextSibling:
			if root.nextSibling.left:
				root.right.nextSibling = root.nextSibling.left
			else:
				root.right.nextSibling = root.nextSibling.right
		else:
			root.right.nextSibling = None
	fillNextSiblings(root.left)
	fillNextSiblings(root.right)


# Constructed Binary tree is:
#              1
#            /   \
#          2      3
#        /  \      \
#       4    5      8
#                 /   \
#                6     7  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

# Populates nextSibling pointer in all nodes

fillNextSiblingsWithLevelOrderTraversal(root)
#fillNextSiblings(root)

# Let us check the values of nextSibling pointers
print("Following are populated nextSibling",
      "pointers in the tree (-1 is printed",
                "if there is no nextSibling)")
print("nextSibling of", root.data, "is ", end = "")
if root.nextSibling:
    print(root.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.left.data, "is ", end = "")
if root.left.nextSibling:
    print(root.left.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.right.data, "is ", end = "")
if root.right.nextSibling:
    print(root.right.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.left.left.data, "is ", end = "")
if root.left.left.nextSibling:
    print(root.left.left.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.left.right.data, "is ", end = "")
if root.left.right.nextSibling:
    print(root.left.right.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.right.right.data, "is ", end = "")
if root.right.right.nextSibling:
    print(root.right.right.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.right.right.left.data, "is ", end = "")
if root.right.right.left.nextSibling:
    print(root.right.right.left.nextSibling.data)
else:
    print(-1)
print("nextSibling of", root.right.right.right.data, "is ", end = "")
if root.right.right.right.nextSibling:
    print(root.right.right.right.nextSibling.data)
else:
    print(-1)

print('aman')