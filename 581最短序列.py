class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        s = e = -1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if s == -1: s = i
                e = i
        return e - s + 1 if e != s else 0



n, sorts = len(nums), sorted(nums)
        if nums == sorts: return 0
        l, r = min(i for i in range(n) if nums[i] != sorts[i]), max(i for i in range(n) if nums[i] != sorts[i])
        return r - l + 1