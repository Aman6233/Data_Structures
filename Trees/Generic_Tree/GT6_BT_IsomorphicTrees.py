#Problem-46: Check whether the trees are isomorphic to each other or not.

''' Two binary trees root1 and root2 are isomorphic if they have the same structure. The values of the nodes doesn't affect isomorphism.'''

def isIsomorphic(root1, root2):
	if not root1 and not root2:
		return 1
	if (root1 and not root2) or (not root1 and root2):
		return 0

	return (isIsomorphic(root1.left, root2.left) and isIsomorphic(root1.right, root2.right))