class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tmp = x
        y = 0.0
        while tmp:
            y = y*10 + tmp%10
            tmp = tmp/10
        return y == x

    class Solution:
        # @return a boolean
        def isPalindrome(self, x):
            if x < 0:
                return False
            copy, reverse = x, 0

            while copy:
                reverse *= 10
                reverse += copy % 10
                copy //= 10

            return x == reverse