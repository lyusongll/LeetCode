class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def maxdepth(self,root):
		if root is None:
			return 0
		else:
			return max(self.maxdepth(root.left),self.maxdepth(root.right))+1

if __name__ == "__main__":
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	print(Solution().maxdepth(root))