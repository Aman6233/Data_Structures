#Problem-22: Find Max Path Sum(Path may start and end at any node)
#GeeksForGeeks

def findMaxUtil(root):
	if root is None:
		return 0

	l = findMaxUtil(root.left)
	r = findMaxUtil(root.right)

	max_single = max(max(l, r) + root.data, root.data)		# max path for current node

	max_top = max(max_single, l+r+ root.data)				# max path
	findMaxUtil.res = max(findMaxUtil.res, max_top)

	return max_single


def findMaxSum(root):
	findMaxUtil.res = float("-inf")		# negative infinity
	findMaxUtil(root)
	return findMaxUtil.res

