#Threaded Binary Tree Structure

class ThreadedBinaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None	#left child
		self.LTag = None	# 0 or 1; [0: left points to predecessor] or [1: left points to left child]
		self.right = None 	#right child
		self.RTag = None	# 0 or 1; [0: right points to successor] or [1: right points to right child]

