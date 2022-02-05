#Singly Linked List

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self, next):
		self.next = next

	def getNext(next):
		return self.next

	def hasNext(self):
		return self.next != None

class LinkedList:
	def __init__(self, node=None):
		self.length = 0
		self.head = node