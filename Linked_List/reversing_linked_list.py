class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_list:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		prev = None
		curr = self.head
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next


if __name__ == "__main__":
	llist = Linked_list()
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)
	print("Created list:", end=" ")
	llist.print_list()
	print("\nReversed list:", end=" ")
	llist.reverse()
	llist.print_list()
