# Insertion in doubly linked list

#At the beginning
def insertAtBeginning(self, data):
	newNode = Node(data)
	if self.head == None:
		self.head = newNode
	else:
		newNode.next = self.head
		newNode.prev = None
		self.head.prev = newNode
		self.head = newNode

#At the end
def insertAtEnd(self, data):
	if self.head == None:
		self.head = Node(data)
	else:
		current = self.head
		while current.next:
			current = current.next

		newNode = Node(data)
		newNode.prev = current
		current.next = newNode

#In the middle
def getNode(self, index):
	current = self.head
	if current == None:
		return None
	i = 0
	while i < index and current.next:
		current = current.next
		i += 1
	return current

def insertAtGivenPosition(self, index, data):
	newNode = Node(data)
	if self.head == None or index == 0:
		self.insertAtBeginning(data)

	else:
		temp = self.getNode(index)
		if temp == None or temp.next == None:
			self.insertAtEnd(data)

		else:
			newNode.next = temp.next
			newNode.prev = temp
			temp.next = newNode
			temp.next.prev = newNode