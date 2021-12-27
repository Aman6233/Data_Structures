#Problem-36: Find the smallest range that includes at least one number from each of the k sorted lists.

import heapq

def smallestRange(Lst):
	heap = []
	n = len(Lst)
	mmax = 0

	#populate initial state (insert 1st ele of each list)
	for i in range(n):
		heapq.heappush(heap, (Lst[i][0], i, 0))
		mmax = max(mmax, Lst[i][0])

	minRange = [heap[0][0], mmax]

	while True:
		num, list_index, num_index = heapq.heappop(heap)

		if num_index == len(Lst[list_index])-1:
			break

		next_num = Lst[list_index][num_index+1]
		mmax = max(mmax, next_num)
		heapq.heappush(heap, (next_num, list_index, num_index+1))

		if mmax - heap[0][0] < minRange[1] - minRange[0]:
			minRange = [heap[0][0], mmax]

	return minRange

# ---------------- Wrong method ----------------

def KlistOneElementfromEach(Lst): 		
	heap = []
	end = False
	for l in Lst:
		thisRange = max(l) - min(l)
		heap.append(min(l))
		heapq.heapify(heap)

	while not end:
		elem = heapq.heappop(heap)
		#print(elem)
		for l in Lst:
			if elem in l:
				#print(l)
				l.remove(elem)
				if len(l) == 0:
					end = True
					break
				heapq.heappush(heap, l[0])
		#print(heap)
	minRange = [elem, max(heap)]
	return(minRange)




Lst = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
#print(KlistOneElementfromEach(Lst))
print(smallestRange(Lst))

Lst = [[4, 7, 9, 12, 15],[0, 8, 10, 14, 20],[6, 12, 16, 30, 50]]
#print(KlistOneElementfromEach(Lst))
print(smallestRange(Lst))

Lst = [[10,10],[11,11]]
#print(KlistOneElementfromEach(Lst))
print(smallestRange(Lst))

Lst = [[1],[2],[3],[4],[5],[6],[7]]
#print(KlistOneElementfromEach(Lst))
print(smallestRange(Lst))
