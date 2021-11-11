#Problem-75: For the key values 1...n, how many structurally unique BSTs are possible that store those keys.

''' Strategy- Consider each node can be root. Recursively find size of left and right subtrees. '''

def countTrees(n):
	if n <= 1:
		return 1

	else:
		sum = 0
		for root in range(1, n+1):
			left = countTrees(root-1)
			right = countTrees(n-root)

			#no. of possible trees with this root = left*right
			sum += left*right

	return sum
