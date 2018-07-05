class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = 0, 0
        for x in nums:
            local_max = max(0, local_max + x)               #负数再加之前得最大值  肯定使最大值减小，所以得判断局部得最大值是不是负数
            global_max = max(global_max, local_max)     
        return global_max


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    #先判断加上下一个数后，是否大于0 ，如果大于0，则取上这个数，再和之前的值相比，
    # 如果比他大，则最为新的最大值