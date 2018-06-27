# def isValidParentheses(self, s):
#     stack = []
#     for ch in s:
#         # 压栈
#         if ch == '{' or ch == '[' or ch == '(':
#             stack.append(ch)
#         else:
#             # 栈需非空
#             if not stack:
#                 return False
#             # 判断栈顶是否匹配
#             if ch == ']' and stack[-1] != '[' or ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{':
#                 return False
#             # 弹栈
#             stack.pop()
#     return not stack


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}"))