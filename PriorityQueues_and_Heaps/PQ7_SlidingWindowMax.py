#Problem-30: Find max in the sliding window (say, w) in a given array.

from collections import deque		#doubly ended queue

def maxSlidingWindow(A,k):
	D = deque()
	res = []

	for i in range(len(A)):
		while D and D[-1][0] < A[i]:
			D.pop()
		D.append((A[i], i+k-1))		# i+k-1 to remove from left if window is full
		if i >= k-1:
			res.append(D[0][0])
		if i == D[0][1]:
			D.popleft()
	return res

print(maxSlidingWindow([4,3,2,1,5,7,6,8,9], 3))