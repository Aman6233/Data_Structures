#Problem-21: Given a BT containing digits 0-9 only, each root-to-leaf could represent a no.(1->2->3 represents 123).
#Find the total sum of all root-to-leaf nos.(2->3 = 23, 2->4 = 24, Sum = 23+24 = 47 )

# A Binary tree node
class Node:
  
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def calSum(root, current, sum):
	if not root:
		return		# to stop execution of upcomming steps
	current = current*10 + root.data
	if not root.left and not root.right:
		sum[0] += current
		return
	calSum(root.left, current, sum)
	calSum(root.right, current, sum)


def sumOfNumbers(root):
	if not root:
		return 0
	current = 0
	sum = [0]		# list can be manipulated inside a function
	calSum(root, current, sum)
	return sum[0]

root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print ("Sum of all paths is", sumOfNumbers(root))

