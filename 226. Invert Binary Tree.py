class Solution:
	def invertTree(self, root):
		if root is None:
			return None
		if root.left:
			self.invertTree(root.left)
		if root.right:
			self.invertTree(root.right)
		root.left, root.right = root.right, root.left
		return root


class Solution:
	def inverTree(self, root):
		if root is None:
			return None
		queue =[root]
		while queue:
			front = queue.pop(0)
			if front.left:
				queue.append(front.left)
			if front.right:
				queue.append(front.right)
			front.left, front.right = front.right, front.left
		return root



def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

   #简洁  左边换到右边去 但是右边自己也要左右换