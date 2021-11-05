#Problem-27: Check whether they are mirrors of each other

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def areMirrors(root1, root2):
	if root1 == None and root2 == None:
		return 1
	if root1 == None or root2 == None:
		return 0
	if (root1.data != root2.data):
		return 0
	else:
		return areMirrors(root1.left, root2.right) and areMirrors(root1.right, root2.left)


root1 = Node(1)
root2 = Node(1)
 
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.right.left = Node(5)
root2.right.right = Node(4)
 
if areMirrors(root1, root2):
    print ("Yes")
else:
    print ("No")