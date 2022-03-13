#Counting nodes in a circular list

#This method would be a member of other class(say, CircularList)
def cicularListLength(self):
	currentNode = self.head
	if currentNode == None:
		return 0
	count = 1
	currentNode = currentNode.next
	while currentNode.next != self.head:
		currentNode = currentNode.next
		count += 1
	return count