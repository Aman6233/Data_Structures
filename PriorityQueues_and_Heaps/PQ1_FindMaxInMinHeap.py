#Problem-7: Given a minHeap, find max element

''' first non-leaf node from bottom or last parent is at n//2 -1. First Leaf is at parent+1 (i.e n//2) '''

def findMaxInMinHeap(heap):
	max = -1
	n = len(heap)
	for i in range(n//2, n):		
		if heap[i] > max:
			max = heap[i]
	return max