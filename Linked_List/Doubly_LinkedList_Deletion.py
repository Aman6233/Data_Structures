#Deletion in doubly linked list

'''Deleting an intermediate node'''

#Deleting element at given position
def getNode(self, index):
	currentNode = self.head
	if currentNode == None:
		return None
	else:
		i = 0
		while currentNode.next:
			if i == index:
				return currentNode
			i += 1
			currentNode = currentNode.next

def deleteAtPosition(self, index):
	if index == 0:
		self.head = self.head.next
		self.head.prev = None

	temp = self.getNode(index)
	if temp:
		temp.prev.next = temp.next
		if temp.next:
			temp.next.prev = temp.prev
		else:							#no need of else
			temp.data = None
			temp = None

#Deleting with given data
def deleteWithData(self, data):
	temp = self.head
	if not temp:
		return None

	while temp:
		if temp.data == data:
			if temp == self.head:
				self.head = temp.next
				self.head.prev = None
				temp = None
				return
			temp.prev.next = temp.next
			if temp.next:
				temp.next.prev = temp.prev
				return
		temp = temp.next


