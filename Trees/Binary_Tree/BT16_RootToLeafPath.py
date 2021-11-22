#Problem-20: Print out all root-to-leaf paths of a Binary Tree

class newNode:
 
    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathsAppender(root, path, paths):
	if not root:
		return 0

	path = path + [root.data]		# new object is created
	#path += [root.data]			# same object is modified
	#path.append(root.data)			# same object is modified   i.e. path += [root.data] is same as path.append(root.data)

	if root.left == None and root.right == None:
		paths.append(path)
		return		# to stop execution of upcomming steps
	pathsAppender(root.left, path, paths)
	pathsAppender(root.right, path, paths)


def pathsFind(root):
	paths = []
	pathsAppender(root, [], paths)
	print('paths: ', paths)


root = newNode(10)
root.left = newNode(28)
root.right = newNode(13)

root.right.left = newNode(14)
root.right.right = newNode(15)

root.right.left.left = newNode(21)
root.right.left.right = newNode(22)
root.right.right.left = newNode(23)
root.right.right.right = newNode(24)

pathsFind(root)

