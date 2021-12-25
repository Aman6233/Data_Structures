#Problem-9: Delete the i-th element in a given min-heap

def delete(A, i):
	n = len(A)
	if n < i:
		print("Wrong position")
	key = A[i]
	A[i] = A[n-1]
	A.pop()				#not necessary, just print till n only
	n -= 1
	procolateDown(A,i,n)
	return key