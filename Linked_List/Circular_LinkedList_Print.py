#Printing the Contents of a Circular list

def printCircularList(self):
	currentNode = self.head
	if currentNode == None:
		return 0

	print(currentNode.data)
	currentNode = currentNode.next
	while currentNode != self.data:
		print(currentNode.data)
		currentNode = currentNode.next