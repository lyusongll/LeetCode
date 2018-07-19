class Solution:
	def isHappy(self, n):
		numSet = set()
		while n != 1 and n not in numSet:  #用来判断n是否已经计算guo
			numSet.add(n)
			sum = 0
			while n:
				dight = n %10
				sum += dight*dight
				n /= 10
			n = sum
		return n == 1