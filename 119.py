class Solution:
	def getRow(self, rowIndex):
		result = [0] * (rowIndex+1)  #刚开始就给所有的值赋值为0 
		for i in range(rowIndex+1):
			old = result[0] = 1
			for j in range (1,i+1):
				old, result[j] = result[j],old +result[j]   #所以这里加杨辉三角中上一个不存在的位置，其实是加了0，而不是空数组
				print(old,result)
		return result

if __name__ == "__main__":
    print(Solution().getRow(3))
