#Problem-45: Count the no. of children for a given node 

def childrenCount(node):
	count = 0
	node = node.firstChild
	while node:
		count += 1
		node = node.nextSibling

	return count

# With generic tree representation(GT1 and GT4), we can count the siblings of a given node with below code.

def childrenCount1(self):		# same as nChildren function
	return len(self.childList)