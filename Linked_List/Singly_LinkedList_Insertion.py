#Insertion in singly linked list

#At the beginning
def insertAtBeginning(self, data):
	newNode = Node()
	newNode.data = data
	if self.length == 0:
		self.head = newNode
	else:
		newNode.next = self.head
		self.head = newNode
	self.length += 1

#At the end
def insertAtEnd(self, data):
	newNode = Node()
	newNode.data = data
	if self.length == 0:
		self.head = newNode
		return
	current = self.head
	while current.next :
		current = current.next

	current.next = newNode
	self.length += 1

#In the middle
def insertAtGivenPosition(self, pos, data):
	if pos > self.length+1 or pos < 0:
		return None
	else:
		if pos == 0:
			self.insertAtBeginning(data)
		else:
			if pos == self.length+1:
				self.insertAtEnd(data)
			else:
				newNode = Node()
				newNode.data = data
				count = 1
				current = self.head
				while count < pos - 1:
					count += 1
					current = current.next
				newNode.next = current.next
				current.next = newNode
				self.length += 1

