#Problem-23: Check the existence of path with given sum (path from root to any node)

class newNode:
 
    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathFinder(root, val, path, paths):
	if not root:
		return False
	path = path + [root.data]
	#if not root.left and not root.right:
	if val == root.data:
		paths.append(path)
		return True
	# else: 
	# 	return False
	left = pathFinder(root.left, val-root.data, path, paths)
	right = pathFinder(root.right, val-root.data, path, paths)
	return left or right


def hasPathWithSum(root, val):
	paths = []
	pathFinder(root, val, [], paths)
	print('sum: ', val)
	print('paths: ', paths)


root = newNode(10)											#		    10
root.left = newNode(28)										#		  /   \
root.right = newNode(13)									#		 /     \
															#		28     13
root.right.left = newNode(14)								#			  /   \
root.right.right = newNode(15)								#			14     15
															#		   / \     / \
root.right.left.left = newNode(21)							#		  /   \   /   \
root.right.left.right = newNode(22)							#		 21   22 23   24
root.right.right.left = newNode(23)
root.right.right.right = newNode(24)

sum = 38

hasPathWithSum(root, sum)