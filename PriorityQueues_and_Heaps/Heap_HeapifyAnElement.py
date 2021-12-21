#Heapifying an element
#below functions should be inside heap class in Heap.py

#Deletion of element uses procolateDown
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

#Insertion of element uses procolateUp 
def procolateUp(self, i):
	while i//2 > 0:			#since heap starts from index 1
		if self.heapList[i] < self.heapList[i//2]:
			temp = self.heapList[i]
			self.heapList = self.heapList[i//2]
			self.heapList = temp
		i = i//2