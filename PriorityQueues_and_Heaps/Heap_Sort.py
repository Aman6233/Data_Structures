# Heapsort
#GeeksForGeeks for reference

def heapSort(A):
	#convert A to heap
	length = len(A)					#size of heap 		
	leastParent = length//2	-1		#First non-leaf node if heap starts at i=0

	#Build maxHeap
	for i in range(leastParent, -1, -1):
		prcolateDown(A, i, length)

	#flatten heap into sorted array
	for i in range(length-1, 0, -1):
		if A[i] < A[0]:
			A[i], A[0] = A[0], A[i]		#swap
			prcolateDown(A, 0, i-1)

#modified procolateDown to skip the sorted elements
def prcolateDown(A, first, last):
	largest = 2*first + 1 			# if heap starts at i=0, leftChild is at (2*first + 1) and rightChild is at (2*first + 2)
	while largest <= last:
		if largest+1 < last and A[largest] < A[largest+1]:
			largest += 1

		if A[largest] > A[first]:
			A[largest], A[first] = A[first], A[largest]
			first = largest
		else:
			return

arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i],end=' '),
