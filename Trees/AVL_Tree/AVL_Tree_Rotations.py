#GeeksForGeeks

#Single Rotations

#Left Left Case (x is left child of root and y is left child of x)(right rotation for root, newRoot= x)
def singleRightRotaion(root):
	x = root.left
	root.left = x.right
	x.right = root
	return x

#Right Right Case (x is right child of root and y is right child of x)(left rotation for root, newRoot= x)
def singleLeftRotaion(root):
	x = root.right
	root.right = x.left
	x.left = root
	return x

#Double Rotations

#Left Right Case(x is left child of root and y is right child of x)(left rotation for x and right rotation for root, newRoot= y)
def leftRightRotation(root):
	x = root.left
	if x.balanceFactor == -1:
		root.balanceFactor = 0
		x.balanceFactor = 0
		root = singleRightRotaion(root)
	else:
		y = x.right
		if y.balanceFactor == -1:
			root.balanceFactor = 1
			x.balanceFactor = 0
		elif y.balanceFactor == 0:
			root.balanceFactor = 0
			x.balanceFactor = 0
		else:
			root.balanceFactor = 0
			x.balanceFactor = -1
		y.balanceFactor = 0
		root.left = singleLeftRotaion(root.left)
		root = singleRightRotaion(root)
	return root

#Right Left Case(x is right child of root and y is left child of x)(right rotation for x and left rotation for root, newRoot= y)
def rightLeftRotation(root):
	x = root.right
	if x.balanceFactor == 1:
		root.balanceFactor = 0
		x.balanceFactor = 0
		root = singleRightRotaion(root)
	else:
		y = x.left
		if y.balanceFactor == -1:
			root.balanceFactor = 0
			x.balanceFactor = 1
		elif y.balanceFactor == 0:
			root.balanceFactor = 0
			x.balanceFactor = 0
		else:
			root.balanceFactor = -1
			x.balanceFactor = 0
		y.balanceFactor = 0
		root.right = singleRightRotaion(root.right)
		root = singleLeftRotaion(root)
	return root