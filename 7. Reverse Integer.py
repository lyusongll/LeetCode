# class Solution:
#     # @param {int} n the integer to be reversed
#     # @return {int} the reversed integer
#     def reverseInteger(self, n):
#         if n == 0:
#             return 0
#
#         neg = 1
#         if n < 0:
#             neg, n = -1, -n
#
#         reverse = 0
#         while n > 0:
#             reverse = reverse * 10 + n % 10
#             n = n / 10
#
#         reverse = reverse * neg
#         if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
#             return 0
#         return reverse
#
#
# print(Solution().reverseInteger(123))


def reverseInteger(n):

    if n < 10:
        return -reverseInteger(-n)
    x = 0
    while n>0:
        x = n %10+x*10
        n = n//10
    return x


A=reverseInteger(-10)
print(A)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

    def reverse3(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(`s * x`[::-1])
        return s * r * (r < 2 ** 31)


if __name__ == "__main__":
    # print
    # Solution().reverse(123)
    # print
    # Solution().reverse(-321)