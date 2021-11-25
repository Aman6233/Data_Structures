#Problem-32: Traverse a Binary Tree in Zigzag order

class newNode:
 
    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigZagTraversal(root):
	result = []
	currentLevel = []
	if root != None:
		currentLevel.append(root)
	leftToRight = True
	while len(currentLevel)>0:
		levelResult = []
		nextLevel = []
		while len(currentLevel)>0:
			node = currentLevel.pop()
			levelResult.append(node.data)

			if leftToRight:
				if node.left != None:
					nextLevel.append(node.left)
				if node.right != None:
					nextLevel.append(node.right)
			else:
				if node.right != None:
					nextLevel.append(node.right)
				if node.left != None:
					nextLevel.append(node.left)
		currentLevel = nextLevel
		result+=levelResult
		leftToRight = not leftToRight
	
	return result

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

print(zigZagTraversal(root))




