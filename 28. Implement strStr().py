class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # for i in xrange(len(haystack) - len(needle) + 1):
        #     if haystack[i: i + len(needle)] == needle:
        #         return i
        # return -1

        len_s = len(haystack)
        len_t = len(needle)
        for i  in range(len_s - len_t):
            if haystack[i:i +len_t] == needle:
                return i
        return -1


if __name__ == "__main__":
    print(Solution2().strStr("a", "bdsdf"))
    print(Solution2().strStr("aabababcdab", "aba"))