class Solution:
    """
    :type n: int
    :rtype: int
    """

    # Time:  O(2^n)
    # Space: O(n)
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2) #到达第n个台阶，可以是第n-1个台阶走一步，第n-2个台阶走两步

if __name__ == "__main__":
    result = Solution().climbStairs1(4)
    print(result)



# class Solution:
#     """
#     @param n: An integer
#     @return: An integer
#     """
#     def climbStairs(self, n):
#         # write your code here
#         if n == 0:
#             return 1
#         if n <= 2:
#             return n
#         result=[1,2]
#         for i in range(n-2):
#             result.append(result[-2]+result[-1])
#         return result[-1]
# if __name__ == "__main__":
#     result = Solution().climbStairs(4)
#     print(result)