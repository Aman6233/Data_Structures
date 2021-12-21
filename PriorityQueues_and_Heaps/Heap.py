#Declaration of Heap

#Here, indexing is taken from 1
class Heap:
	def __init__(self):
		self.heapList = [0]		#Elements in heap
		self.size = 0			#Size of the heap

	#Parent of a node
	def parent(self,index):
		return index//2			

	#Left child
	def leftChild(self,index):
		return 2*index

	#Right child
	def rightChild(self,index):
		return (2*index + 1)

	#Get maximum in maxHeap
	def getMaximum(self):
		if self.size == 0:
			return -1
		return self.heapList[1]

	#Get minimum in minHeap
	def getMinimum(self):
		if self.size == 0:
			return -1
		return self.heapList[1]