# class Solution:
#     """
#     @param A : a list of integers
#     @param target : an integer to be inserted
#     @return : an integer
#     """
#
#     def searchInsert(self, A, target):
#         if len(A) == 0:
#             return 0
#
#         start, end = 0, len(A) - 1
#         # first position >= target
#         while start + 1 < end:
#             mid = (start + end) // 2
#             if A[mid] >= target:
#                 end = mid
#             else:
#                 start = mid
#
#         if A[start] >= target:
#             return start
#         if A[end] >= target:
#             return end
#         return len(A)
#
# if __name__ == "__main__":
#     print(Solution().searchInsert([1, 3, 5, 6], 5))
#     # print Solution().searchInsert([1, 3, 5, 6], 2)
#     # print Solution().searchInsert([1, 3, 5, 6], 7)
#     # print Solution().searchInsert([1, 3, 5, 6], 0)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    # print Solution().searchInsert([1, 3, 5, 6], 2)
    # print Solution().searchInsert([1, 3, 5, 6], 7)
    # print Solution().searchInsert([1, 3, 5, 6], 0)