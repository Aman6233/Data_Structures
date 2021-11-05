#Problem-33: Find vertical sum of a Binary Tree

'''Horizontal Distance for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance 
and a left edge is considered as -1 horizontal distance. For left subtree, we pass the Horizontal Distance as
Horizontal distance of root minus 1. For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1.
If two nodes have the same Horizontal Distance (HD), then they are on the same vertical line.'''

class newNode: 
      
    def __init__(self, data): 
          
        self.left = None
        self.right = None
        self.data = data 

hastable = {}		# just a dict.
def verticalSumInBinaryTree(root, column):
	if not root:
		return
	if not column in hastable:
		hastable[column] = 0
	hastable[column] = hastable[column] + root.data
	verticalSumInBinaryTree(root.left, column -1)
	verticalSumInBinaryTree(root.right, column +1)


root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(3) 
root.left.left = newNode(4) 
root.left.right = newNode(5) 
root.right.left = newNode(6) 
root.right.right = newNode(7)

verticalSumInBinaryTree(root, 0)
print(hastable)


