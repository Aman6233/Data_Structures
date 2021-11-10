#Problem-58: Convert BST to circular DLL(Doubly linked list) with space complexity O(1).

from Binary_Search_Tree import BSTNode

def BSTtoDLL(root):
	global tail, head		# tail is prev
	tail = None
	head = None
	BSTtoDoublyList(root)
	return head

def BSTtoDoublyList(root):
	global tail, head
	if not root:
		return

	BSTtoDoublyList(root.left)

	# current node's left points to tail
	if tail:
		tail.right = root
		root.left = tail
	else:
		head = root			# if tail is None then current node is head

	right = root.right		# saving right node

	# now we need to make list created till now as circular
	head.left = root
	root.right = head

	# for right-subtree/parent, current node is in-order predecessor
	tail = root
	BSTtoDoublyList(right)
	
	

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


