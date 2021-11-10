#Problem-54,55,56,57: Check whether the given tree is BST or not

from Binary_Search_Tree_FindMaxElement import findMax
from Binary_Search_Tree_FindMinElement import findMin

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = newNode(3) 
root.left = newNode(2) 
root.right = newNode(5) 
root.right.left = newNode(1) 
root.right.right = newNode(6)

#54-simple but this is wrong, since checking current node only is not enough
def isBSTWrong(root):		
	if root is None:
		return 1
	if root.left and root.left.data > root.data:
		return 0
	if root.right and root.right.data < root.data:
		return 0

	if not isBSTWrong(root.left) or not isBSTWrong(root.right):
		return 0

	return 1

print(isBSTWrong(root))

#55-correct
def isBST(root):
	if root is None:
		return 1
	if root.left and findMax(root.left).data >= root.data:
		return 0
	if root.right and findMin(root.right).data <= root.data:
		return 0

	if not isBST(root.left) or not isBST(root.right):
		return 0

	return 1

print(isBST(root))

#56-improve complexity on 55
''' visit each node only once '''
def isBST_1(root, min, max):
	if root is None:
		return 1
	if root.data <= min or root.data >= max:
		return 0
	result = isBST_1(root.left, min, root.data)
	result = result and isBST_1(root.right, root.data, max)

	return result

print(isBST_1(root, float('-infinity'), float('infinity')))		# infinity or inf

#57-improve complexity on 56
''' use inorder traversal as it produces sorted list '''
previousValue = float('-inf')
def isBST_2(root, previousValue):
	if root is None:
		return 1
	if not isBST_2(root.left, previousValue):
		return 0
	if root.data < previousValue:
		return 0
	previousValue = root.data
	return isBST_2(root.right, previousValue)

print(isBST_2(root, previousValue))
