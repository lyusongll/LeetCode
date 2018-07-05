class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1
    ## 从最后一个数开始取，如果扎到目标数，就将目标数放到最后，并把最后不是目标数得往前面放，并把最后得坐标向前进一格