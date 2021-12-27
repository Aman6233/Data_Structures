#Problem-33: Find Median in a series of integers

import heapq			#heapq is minHeap by default

class StreamMedian:
	def __init__(self):
		self.minHeap, self.maxHeap = [], []
		self.n = 0

	def insert(self, num):
		num = heapq.heappushpop(self.minHeap, num)		#push new element in minHeap and get min element
		num = - heapq.heappushpop(self.maxHeap, -num)	#push element in maxHeap and get max element

		if len(self.minHeap) < len(self.maxHeap):
			heapq.heappush(self.minHeap, num)
		else:
			heapq.heappush(self.maxHeap, -num)
			
	def getMedian(self):
		if len(self.maxHeap) > len(self.minHeap):
			return - self.maxHeap[0]
		else:
			return (self.minHeap[0] - self.maxHeap[0])/2.0

S = StreamMedian()
S.insert(2)
S.insert(9)
result = S.getMedian()
print(result)
S.insert(10)
result = S.getMedian()
print(result)
S.insert(11)
S.insert(12)
S.insert(3)
result = S.getMedian()
print(result)