#Problem-47: Check whether the trees are quasi-isomorphic to each other or not.

''' Two binary trees root1 and root2 are quasi-isomorphic if root1 can be transformed into root2 by swapping the left and right children 
	of some of the nodes of root1. Data in the nodes are not important only shape is. '''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def quasiIsomorphic(root1, root2):
	if not root1 and not root2:
		return 1
	if (not root1 and root2) or (root1 and not root2):
		return 0
	a = (quasiIsomorphic(root1.left, root2.left) and quasiIsomorphic(root1.right, root2.right) or quasiIsomorphic(root1.left, root2.right) and quasiIsomorphic(root1.right, root2.left))
	return a
	
root1 = Node(1)
root2 = Node(1)
 
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.left.right.left = Node(7)
root1.right.left.left = Node(8)
 
root2.left = Node(5)
root2.right = Node(6)
root2.left.left = Node(3)
root2.right.left = Node(8)
root2.right.right = Node(2)
root2.left.left.right = Node(7)
root2.right.left.left = Node(4)

print(quasiIsomorphic(root1, root2))