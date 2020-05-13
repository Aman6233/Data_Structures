#geeksforgeeks-linked list set-2

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

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head		#we used a variable because we cannot use self.head directly as it will change the position of head.
		while (last.next):
			last = last.next

		last.next = new_node

	def insert_after(self, prev_node, data):
		new_node = Node(data)

		if prev_node is None:
			print("The previous node should be in Linked list.")
			return
		new_node.next = prev_node.next
		prev_node.next = new_node

	def get_count_rec(self, node):
		if (not node):
			return 0
		else:
			return 1+ self.get_count_rec(node.next)

	def get_count(self):
		return self.get_count_rec(self.head)

	def delete_node(self, key):
		temp = self.head
		if temp.data == key:
			self.head = temp.next
			temp = None
			return

		while (temp):
			if (temp.data == key):
				break
			prev = temp
			temp = temp.next
		if temp == None:
			return

		prev.next = temp.next
		temp = None

	def delete_node_position(self, position):
		if self.head == None:
			return

		temp = self.head

		if position == 0:
			self.head = temp.next
			temp = None
			return

		for i in range(position-1):
			temp = temp.next
			if temp == None:
				break

		if temp == None:
			return
		if temp.next == None:
			return

		nxt = temp.next.next
		temp.next = None
		temp.next = nxt

	def search(self, curr_node, key):
		if (not curr_node):
			return False

		if curr_node.data == key:
			return True
		return self.search(curr_node.next, key)

	def swap_nodes(self, x, y):
		if x==y:
			return
		
		prevX = None
		currX = self.head
		while currX != None and currX.data != x:
			prevX, currX = currX, currX.next

		prevY = None
		currY = self.head
		while currY != None and currY.data != y:
			prevY, currY = currY, currY.next

		if currX == None or currY == None:
			return

		if prevX != None:
			prevX.next = currY
		else:
			self.head = currY

		if prevY != None:
			prevY.next = currX
		else:
			self.head = currX

		#temp = currX.next
		currX.next, currY.next = currY.next, currX.next
		#currY.next = temp

	def print_list(self):
		temp = self.head		#we used a variable because we cannot use self.head directly as it will change the position of head.
		while (temp):
			print(temp.data, end=" ")
			temp = temp.next


if __name__ == "__main__":

	llist = Linked_list()

	llist.append(6)
	llist.push(7)
	llist.push(1)
	llist.append(4)
	llist.insert_after(llist.head.next, 8)

	print("Created list is:",end=" ")
	llist.print_list()
	print("\nNo. of nodes:",end=" ")
	print(llist.get_count(),end="")
	print("\nList after swaping nodes:", end=" ")
	llist.swap_nodes(8, 4)
	llist.print_list()
	llist.delete_node(6)
	print("\nList after deleting  node:", end=" ")
	llist.print_list()
	llist.delete_node_position(2)
	print("\nList after deleting  node position:", end=" ")
	llist.print_list()
	print("\nNo. of nodes:",end=" ")
	print(llist.get_count())

	if llist.search(llist.head, 4):
		print("yes")
	else:
		print("no")