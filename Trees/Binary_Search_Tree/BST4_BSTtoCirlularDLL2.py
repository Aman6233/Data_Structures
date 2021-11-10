#Problem-59: Convert BST to circular DLL using divide and conquer
#IGNORE

''' -when the current node(root) is a leaf node
	-when there exists no left child
	-when there exists no right child
	-when there exists both left and right child '''

from Binary_Search_Tree import BSTNode

def BSTtoDLL(root):
	if root.left == None and root.right == None:		# for leaf node
		return root

	elif root.left == None:								# no left subtree
		h2 = BSTtoDLL(root.right)
		root.right = h2
		h2.left.right = root
		root.left = h2.left
		h2.left = root
		return root

	elif root.right == None:							# no right subtree
		h1 = BSTtoDLL(root.left)
		root.left = h1.left
		h1.left.right = root
		root.right = h1
		h1.left = root
		return h1

	else:
		h1 = BSTtoDLL(root.left)
		h2 = BSTtoDLL(root.right)
		
		l1 = h1.left
		l2 = h2.left

		h1.left = l2
		l2.right = h1

		l1.right = root
		root.left = l1

		root.right = h2
		h2.left = root
		return h1

def displayCList(head):
	print("Circular Linked List is :") 
	itr = head
	first = 1
	while (head != itr or first):
		print(itr.data, end = " ") 
		itr = itr.right
		first = 0
	print()

if __name__ == '__main__':
    root = BSTNode(10) 
    root.left = BSTNode(12) 
    root.right = BSTNode(15) 
    root.left.left = BSTNode(25) 
    root.left.right = BSTNode(30) 
    root.right.left = BSTNode(36) 

    head = BSTtoDLL(root) 
    displayCList(head) 
