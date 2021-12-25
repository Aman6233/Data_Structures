#Problem-15: Find kth smallest element in min-heap.
#GeeksForGeeks for reference
#deletion from min heap k times

def kthSmallest(collection, k):
	A = collection[:k]
	buildHeap(A)
	for i in range(k,len(collection)):
		if collection[i] < A[0]:
			A[0] = collection[i]
			heapify(A, 0, k)

	return A[0]

def buildHeap(A):
	n = len(A)
	for i in range(n//2-1, -1, -1):
		heapify(A, i, n)

def heapify(A, index, maxIndex):		#max heap
	largest = index
	left = 2*index+1
	right = 2*index+2
	if left < maxIndex and A[left] > A[index]:
		largest = left
	if right < maxIndex and A[right] > A[largest]:
		largest = right
	if largest != index:
		A[index], A[largest] = A[largest], A[index]
		heapify(A, largest, maxIndex)


A = [0,3,5,2,6,8,7,1,9,4]	#0-9 only order is different, wrong minHeap (just to check with different sequence)
print(A)
print(kthSmallest(A,3))
print(kthSmallest([*range(10)],1))
print(kthSmallest([*range(10)],10))