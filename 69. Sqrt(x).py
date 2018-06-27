class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x :
                right = mid - 1
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    print(Solution().mySqrt(8))