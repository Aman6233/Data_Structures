#Problem-62,63: Convert singly linked list to height balanced BST

#62- same as BST5

#63
from Binary_Search_Tree import BSTNode

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)

def inorder(root):
	if not root:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

def sortedListToBST(start, end):
	global head
	#print(head.data)
	if start > end:
		return None

	mid = start + (end-start)//2
	left = sortedListToBST(start, mid-1)
	root = BSTNode(head.data)
	head = head.next

	print('root data mid: ', mid, root.data)
	root.left = left
	root.right = sortedListToBST(mid+1, end)
	return root

def convertSortedListToBST(n):
	return sortedListToBST(0, n-1)

root = convertSortedListToBST(5)
print(root.data)
inorder(root)
