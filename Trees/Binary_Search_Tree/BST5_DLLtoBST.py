#Problem-60: Convert a sorted DLL to balanced BST

def FindMiddleNode(head):
	fastPtr = head
	slowPtr = head

	while fastPtr != None:
		fastPtr = fastPtr.next
		if fastPtr == None:
			return slowPtr
		fastPtr = fastPtr.next
		slowPtr = slowPtr.next
	return slowPtr

def DLLtoBalancedBST(head):
	if not head or not head.next:
		return head

	temp = FindMiddleNode(head)
	p = head
	while p.next != temp:
		p = p.next

	p.next = None
	q = temp.next
	temp.next = None
	temp.prev = DLLtoBalancedBST(head)
	temp.next = DLLtoBalancedBST(q)
	return temp