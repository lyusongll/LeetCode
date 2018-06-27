class Solution:
	def twoSUm(self,nums,target):
		start, end = 0,len(nums)-1
		while start != end:
			sum = nums[start]+ nums[end]
			if sum > target:
				end -=1
			elif sum < target:
				start+=1
			else:
				return [start+1,end +1]

if __name__ == "__main__":
	print(Solution().twoSUm([2,7,11,15],9))