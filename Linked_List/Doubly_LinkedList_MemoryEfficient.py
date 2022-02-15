#Memory-efficient Doubly linked list

''' ptrdiff = (pointer to previous node) xor (pointer to next node) '''

class Node:
	def __init__(self):
		self.data = None
		self.ptrdiff = None

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def setPtrDiff(self):
		self.ptrdiff = prev ^ next

	def getPtrDiff(self):
		return self.ptrdiff