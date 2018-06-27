# class Solution:
#     # @param strs: A list of strings
#     # @return: The longest common prefix
#     def longestCommonPrefix(self, strs):

#         # write your code here
#         if len(strs) <= 1:
#             return strs[0] if len(strs) == 1 else ""
#         end, minl = 0, min([len(s) for s in strs])
#         while end < minl:
#             for i in range(1, len(strs)):
#                 if strs[i][end] != strs[i-1][end]:
#                     return strs[0][:end]
#             end = end + 1
#         return strs[0][:end]
#     ##minl 是所有字符串中最短的字符串长度
#     ##end 是每个字符取的长度大小
#
import datetime
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        begin = datetime.datetime.now()
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]




if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["hello", "heaven", "hea"]))