class Solution:
	def isHappy(self, n):
		numSet = set()
		while n != 1 and n not in numSet:
			numSet.add(n)
			sum = 0
			while n:
				dight = n %10
				sum += dight*dight
				n /= 10
			n = sum
		return n == 1