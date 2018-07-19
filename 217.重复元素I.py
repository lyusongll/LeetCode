class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False
        
 class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
