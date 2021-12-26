#Problem-20: Implement Queue using Heap.

''' Take one extra element say c(initialize with 0). Here c is used as the priority while inserting/deleting the elements.
	c is taken as positive here '''

def enQueue(element):
	PQ.insert(c, element)
	c += 1

def deQueue():
	return PQ.deleteMin()

def front():
	return PQ.Min()

def size():
	return PQ.size()

def isEmpty():
	return PQ.isEmpty()

# push method can be replaced by below one and in this way we can eliminate c
def push(element):
	PQ.insert(gettime(), element)