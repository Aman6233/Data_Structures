#Problem-16: Find kth smallest element in min-heap.

''' Insert min from HOrig(original min heap) to HAux(auxilary min heap). Here we don't delete min from HOrig. '''

from Heap_Full_Implementation import Heap

def findKthLargestElement(HOrig, k):
	count = 1
	HAux = Heap()
	itm = HOrig.getMinimum()
	
	HAux.insert(itm)
	if count == k:
		return itm
	while HAux.size>=1:
		itm = HAux.deleteMin()
		print(itm)
		count += 1
		if count == k:
			return itm
		else:
			if HOrig.rightChild(HOrig.searchElement(itm)) != -1:
				print('b',HOrig.rightChild(HOrig.searchElement(itm)))
				HAux.insert(HOrig.rightChild(HOrig.searchElement(itm)))
			if HOrig.leftChild(HOrig.searchElement(itm)) != -1:
				print('a',HOrig.leftChild(HOrig.searchElement(itm)))
				HAux.insert(HOrig.leftChild(HOrig.searchElement(itm)))

HOrig = Heap()
HOrig.insert(1)
HOrig.insert(20)
HOrig.insert(5)
HOrig.insert(100)
HOrig.insert(1000)
HOrig.insert(12)
HOrig.insert(18)
HOrig.insert(16)
HOrig.printHeap()

print(findKthLargestElement(HOrig,6))
print(findKthLargestElement(HOrig,3))

