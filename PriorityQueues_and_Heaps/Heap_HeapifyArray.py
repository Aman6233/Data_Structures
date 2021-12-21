#Heapify the Array or Build a heap from an array

''' Leaf nodes always satisfy the heap property. So, start with first non-leaf node and start heapification '''

def buildHeap(self, A):
	i = len(A)//2 			#First non-leaf node if heap starts at i=1, if it starts with i=0 then len(A)//2-1
	self.size = len(A)
	self.heapList = [0] + A[:]
	
	while i>0:
		self.procolateDown(i)
	i -= 1					# Moves left in level-order