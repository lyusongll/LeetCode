class Solution:
	def containsNearbyDuplicate(self, nums,k):
		lookup = {}
		if i, num in enumerate(nums):
			if num not in lookup:
				lookup[num] = i
			else:
				if i - lookup[num] <= k:
					return True
				lookup[num] = i
		return False



class Solution:
	def containsNearbyDuplicate(self, nums,k):
		dict = {}
		for i in range(len(nums)):
			if nums[i] in dict and i -lookup[nums[i]] <= k
				return True

			dict[nums[i]] = i

		return False

