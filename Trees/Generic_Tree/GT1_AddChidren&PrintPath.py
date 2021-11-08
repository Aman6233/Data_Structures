#Problem-39: Implement simple Generic tree to add children and print path from root to leaf for every node

''' Children are additive; no provision for deleting them.
	The birth order of children is recorded: 0 for the first child added, 1 for the second, ...
	GenericTree(parent, value=None)		Contructor
	parent		 If this is root, None, otherwise the parent's GenericTree object.
	childList	 List of children, zero or more GenericTree objects.
	value		 Value passed to constructor; can be any type.
	birthOrder	 If this is the root, 0, otherwise the index of this child in the parent's.childList.
	nChildren()	 Returns the no. of self's children.
	nthChild(n)	 Returns the nth child; raises IndexError if n is not a valid child no.
	fullPath():  Returns path to self as a list of child nos.
	nodeId():	 Returns path to self as a NodeId.
'''

import string
class GenericTree:
	def __init__(self, parent, value=None):
		self.parent = parent
		self.value = value
		self.childList = []
		if parent is None:
			self.birthOrder = 0
		else:
			self.birthOrder = len(parent.childList)
			parent.childList.append(self)

	def nChildren(self):
		return len(self.childList)

	def nthChild(self):
		return self.childList[n]

	def fullPath(self):
		result = []
		parent = self.parent
		kid = self
		while parent:
			result.insert(0, kid.birthOrder)
			parent, kid = parent.parent, parent
		#result.insert(0, 0)		# I think this is required to add root also
		return result

	def nodeID(self):
		fullPath = self.fullPath()
		return nodeID(fullPath)		# this should be replaced by next line
		#return NodeId(fullpath)

class NodeId:
	def __init__(self, path):
		self.path = path

	def __str__(self):
		L = map(str, self.path)
		return string.join(L, '/')

	def find(self, node):
		return self.__reFind(node, 0)

	def __reFind(self, node, i):
		if i >= len(self.path):
			return node.value
		else:
			childNo = self.path[i]
		try:
			child = node.nthChild(childNo)
		except IndexError:
			return None
		return self.__reFind(child, i+1)

	def isOnPath(self, node):		# parameter should be nodePath 
		if len(nodePath) > len(self.path):
			return 0		# node is deeper than self.path
		for i in range(len(nodePath)):
			if nodePath[i] != self.path[i]:
				return 0	# node is at different route than self.path
		return 1