#this file extends Heap.py and Heap_HeapifyAnElement
#below functions should be inside heap class in Heap.py

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

