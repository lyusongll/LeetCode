class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A == []:
            return 0
        index = 0
        for i in range(1, len(A)):
            if A[index] != A[i]: #从第一个数开始，
                index += 1
                A[index] = A[i]

        return index + 1   #index是索引，所以返回长度时+1
    ##数组已经默认是安装从小到大的顺序排了