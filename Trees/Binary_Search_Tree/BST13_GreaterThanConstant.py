#Problem-76: Give an O(h) algorithm GreaterThanConstant(r, k) to find the no. keys that are strictly greater than k (h is height)

''' Given a BST of size n, in which each node 'r' has an additional field r->size, the no. of the keys in the sub-tree
	rooted r (including root node r). '''

def greaterThanConstant(r, k):
	keysCount = 0
	while r:
		if k < r.data:
			keysCount = keysCount + r.right.size + 1
			r = r.left
		elif k > r.data:
			r = r.right
		else:
			keysCount = keysCount + r.right.size
			break
	return keysCount
 