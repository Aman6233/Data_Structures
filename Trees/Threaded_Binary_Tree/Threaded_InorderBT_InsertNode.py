#Insertion of nodes in InOrder Threaded Binary Tree

''' Let us assume that there are 2 nodes P & Q and we want to attach Q to right of P.
	-Node P does not have right child: In this case we just need to attach Q to P and change its left and right pointers.
	-Node P has right child (say, R): In this case we need to traverse R's left subtree and find the left most node and update the left and right pointers. '''

def insertRightInInorderTBT(P, Q):
	Q.right = P.right
	Q.RTag = P.RTag
	Q.left = P		#Predecessor of Q
	Q.LTag = 0
	P.right = Q
	P.RTag = 1
	if Q.RTag == 1:
		temp = Q.right
		while temp.LTag:
			temp = temp.left
		temp.left = Q		#Predecessor of temp