class Solution:
	def addDigits(self, num):
		while num >9:
			c = 0
			while num:
				c += num%10
				num /= 10
			num = c
		return num



class Solution:
	def addDigits(self, num):
		if num == 0:
			return 0
		return (num-1) %9 +1