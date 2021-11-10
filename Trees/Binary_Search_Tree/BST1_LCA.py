#Problem-51: Given pointers of two nodes in BST, find the least common ancestor (LCA)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)


def lca(root, a, b):
	if a <= root.data <= b or b <= root.data <= a:
		return root
	if a < root.data and b < root.data:
		return lca(root.left, a, b)
	if a > root.data and b > root.data:
		return lca(root.right, a, b)


n1 = 10 ; n2 = 14
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))
 
n1 = 14 ; n2 = 8
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2 , t.data))
 
n1 = 10 ; n2 = 22
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))