#Problem-18: Find the diameter of the tree 
#(Diameter: sometimes called width, is the no. of nodes on the longest path b/w two leaves in the tree)

#Recursive-1
ptr = 0
def diameter(root):
	global ptr
	if not root:
		return 0
	left = diameter(root.left)		#left height
	right = diameter(root.right)	#right height
	if (left+right+1)>ptr:
		prt = left+right+1			#actual diameter i.e. (D=L+R+1)
	return 1+ max(left,right)
print(ptr)


#Recursive-2
def height(root):
	if root == None:
		return 0
	return 1+ max(height(root.left), height(root.right))

def diameter(root):
	if root == None:
		return 0

	lheight = height(root.left)
	rheight = height(root.right)

	ldiameter = diameter(root.left)
	rdiameter = diameter(root.right)

	return max(lheight+rheight+1, max(ldiameter, rdiameter))