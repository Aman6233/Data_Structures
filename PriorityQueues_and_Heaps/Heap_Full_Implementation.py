#Full implementation of heap

class Heap:
	def __init__(self):
		self.heapList = [0]
		self.size = 0
	def parent(self, i):
		return i//2
	def leftChild(self, i):
		if 2*i <= self.size:
			return self.heapList[2*i]
		return -1
	def rightChild(self, i):
		if 2*i+1 <= self.size:
			return self.heapList[2*i+1]
		return -1

	def searchElement(self, itm):
		i = 1
		while i <= self.size:
			if itm == self.heapList[i]:
				return i
			i += 1

	def getMinimum(self):
		if self.size == 0:
			return -1
		return self.heapList[1]

	def procolateDown(self, i):
		while (i*2) <= self.size:
			minimumChild = self.minChild(i)
			if self.heapList[i] > self.heapList[minimumChild]:
				temp = self.heapList[i]
				self.heapList[i] = self.heapList[minimumChild]
				self.heapList[minimumChild] = temp
			i = minimumChild

	def minChild(self,i):
		if (i*2 + 1) > self.size:
			return i*2
		else:
			if self.heapList[i*2+1] > self.heapList[i*2]:
				return i*2
			else:
				return (i*2 + 1)

	def procolateUp(self, i):
		while i//2 > 0:	
			print(self.heapList[i//2])	#since heap starts from index 1
			if self.heapList[i] < self.heapList[i//2]:
				temp = self.heapList[i]
				self.heapList = self.heapList[i//2]
				self.heapList = temp
			i = i//2

	#Insertion of an element
	def insert(self, k):
		self.heapList.append(k)
		self.size += 1
		self.procolateUp(self.size)

	#Deletion of an element
	def deleteMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.size]		#replace by last element
		self.size -= 1
		self.heapList.pop()								#pop last element
		self.procolateDown(1)
		return retval

	def printHeap(self):
		print(self.heapList[1:])