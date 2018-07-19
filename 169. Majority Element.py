def majorityElement2(self, nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1 
			
			
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate, count = None, 0
        for e in num:
            if count == 0:
                candidate, count = e, 1
            elif e == candidate:
                count += 1
            else:
                count -= 1
        return candidate