class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                #将不是0的数和最前一个是0的数交换位置
                y += 1

        return nums   


print(Solution().moveZeroes([1,2,30,0,4]))