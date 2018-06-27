
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution2().lengthOfLastWord(""))

    #先按照空格分割，生成列表。后去掉最后一个单词的前面空格