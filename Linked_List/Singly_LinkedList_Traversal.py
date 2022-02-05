#Traversing the linked list

def length(self):
	current = self.head
	count = 0
	while (current):
		count += 1
		current = current.next

	return count