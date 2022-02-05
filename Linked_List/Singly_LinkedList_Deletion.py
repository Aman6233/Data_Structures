#Deletion in singly linked list

#from the beginning
def deleteFromBeginning(self):
	if self.length == 0:
		print('The list is empty')
	else:
		self.head = self.head.next
		self.length -= 1

#from the end
def deleteLastNode(self):
	if self.length == 0:
		print('The list is empty')
	else:
		currentNode = self.head
		previousNode = self.head
		while currentNode.next:
			previousNode = currentNode
			currentNode = currentNode.next
		previousNode.next = None
		self.length -= 1

# an Intermediate node

def deleteWithNode(self, node):			#Delete with node from linked list
	if self.length == 0:
		raise ValueError('list is empty')
	else:
		current = self.head
		previous = None
		found = False
		while not found:
			if current == node:
				found = True
			elif current is None:
				raise ValueError('Node not in Linked list')
			else:
				previous = current
				current = current.next
		if previous == None:
			self.head = current.next
		else:
			previous.next = current.next
		self.length -= 1

def deleteWithValue(self, value):			#Delete with data from linked list
	currentNode = self.head
	previousNode = None
	while currentNode.next:
		if currentNode.data == value:
			if previousNode == None:
				self.head = currentNode.next
			else:
				previousNode.next = currentNode.next
			self.length -= 1
			return
		else:
			previousNode = currentNode
			currentNode = currentNode.next
	print('Value provide is not present')

def deleteAtPosition(self, pos):			#Delete a node at a particular position
	count = 0
	currentNode = self.head
	previousNode = None
	if pos < 0 or pos > self.length:
		print('The position does not exist')
	else:
		while currentNode.next:
			if count == pos:
				if previousNode == None:
					self.head = currentNode.next
				else:
					previousNode.next = currentNode.next
				self.length -= 1
				return
			else:
				previousNode = currentNode
				currentNode = currentNode.next

# Delete Singly linked list
def clear(self):
	self.head = None