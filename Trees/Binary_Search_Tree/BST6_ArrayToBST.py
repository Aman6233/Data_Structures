#Problem-61: Convert a sorted array to BST

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

def inorder(root):
	if not root:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

def buildBST(A, left, right):
	if left > right:
		return
	
	newNode = Node()
	if not newNode:
		print('Memory Error')
		return

	if left == right:
		newNode.data = A[left]

	else:
		mid = left + (right-left)//2
		newNode.data = A[mid]
		newNode.left = buildBST(A, left, mid-1)
		newNode.right = buildBST(A, mid+1, right)

	return newNode


if __name__ == '__main__':
	A = [2,3,4,5,6,7]
	root = buildBST(A, 0, len(A)-1)
	inorder(root)
