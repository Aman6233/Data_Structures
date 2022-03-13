#Insertion in circular linked list

#At the end
def insertAtEndInCLL(self, data):
	current = self.head
	newNode = Node(data)
	if self.head == None:
		self.head = newNode
		return
	while current.next != self.head:
		current = current.next

	current.next = newNode
	newNode.next = self.head

#At the beginning
def insertAtBeginning(self, data):
	current = self.head
	newNode = Node(data)
	if self.head == None:
		self.head = newNode
		return
	while current.next != self.head:
		current = current.next

	current.next = newNode
	newNode.next = self.head
	self.head = newNode