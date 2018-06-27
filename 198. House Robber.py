# f(0) = nums[0]
# f(1) = max(nums[0],nums[1])
# f(k) = max(f(k-2) + nums[k], f(k-1))

class Solution:
	def rob(self, nums):
		last, now = 0, 0
		for i in nums:
			last,now = now, max(last + i ,now)
		return now


class Solution:
	def rob(self, nums):
		if len(nums) == 0:
			return 0
		if len(nums) ==1:
			return nums[0]

		nums_i,nums_i_1 = max(nums[i],num[0]), num[0]

		for i in range(2,len(num)):
			nums_i_1, nums_i_2 = nums_i ,nums_i_1
			num_i = max(nums[i] +nums_i_2, nums_i_1)
		return num_i

if __name__ == '__main__':
        print(Solution().rob([8,4,8,5,9,6,5,4,4,10)]) 