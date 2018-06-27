# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dic = {}
#         for index, num in enumerate(nums):
#             if num in dic:
#                 return [dic[num], index]
#             dic[target - num] = index
#             #将索引记录到dic中，直接返回就行了
#
# #更好理解一点，
# class Solution(object):
#     def twoSum(self, nums, target):
#         #hash用于建立数值到下标的映射
#         hash = {}
#         #循环nums数值，并添加映射
#         for i in range(len(nums)):
#             if target - nums[i] in hash:
#                 return [hash[target - nums[i]], i]
#             hash[nums[i]] = i
#         #无解的情况
#         return [-1, -1]
#
#
# if __name__ == "__main__":
#     # nums = [2, 7, 11, 15]
#     # target = 9
#     # print(Solution().twoSum(nums, target))
#     # # assert (Solution().twoSum(nums, target) == [0, 1])
#     nums = [3, 2, 4]
#     target = 9
#     # assert (Solution().twoSum(nums, target) == [1, 2])
#     print(Solution().twoSum(nums, target))-

def twosum(num,target):
    dir = {}
    for i in range(len(num)):
        if target - num[i] in dir:
            return [dir[target - num[i]], i]
        dir[num[i]] = i
    return [-1, -1]

num = [3, 2, 4, 6]
target = 9
print(twosum(num,target))
