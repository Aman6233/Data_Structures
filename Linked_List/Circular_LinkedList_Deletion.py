#Deletion in circular linked list

#From the last
def deleteLastNodeInCLL(self):
	current = self.head
	previous = None
	if current == None:
		print('List Empty')
		return
	while current.next != self.head:
		previous = current
		current = current.next

	if previous == None:
		self.head = None
	else:
		previous.next = self.head		#or previous.next = current.next
	return

#From the beginning
def deleteFirstNodeInCLL(self):
	current = self.head
	if self.head == None:
		return None

	while current.next != self.head:
		current = current.next

	current.next = self.head.next
	self.head = self.head.next
	return