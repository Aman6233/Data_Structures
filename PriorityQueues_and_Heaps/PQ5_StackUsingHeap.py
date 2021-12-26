#Problem-19: Implement stack using heap.

''' Take one extra element say c(initialize with 0). Here c is used as the priority while inserting/deleting the elements. 
	c is taken as negative here '''

def push(element):
	PQ.insert(c, element)
	c -= 1

def pop():
	return PQ.deleteMin()

def top():
	return PQ.Min()

def size():
	return PQ.size()

def isEmpty():
	return PQ.isEmpty()

# push method can be replaced by below one and in this way we can eliminate c
def push(element):
	PQ.insert(-gettime(), element)