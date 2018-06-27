class Solution:
	def missingNumber(self, nums):
		n = len(nums)
		return n * (n +1) /2 - sum(nums)



#位运算
class Solution:
	def missingNumber(self,nums):
		a = reduce(operator.xor ,nums)
		b = reduce(operator.xor.range(len(nums)+1))
		return a^b