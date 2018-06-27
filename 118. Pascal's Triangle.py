class Solution:
	def generate(self,numRows):
		result = []
		for i in range(numRows):
			result.append([])
			for j in range(i+1):
				if j in (0,i):      ##if j == 0 or j ==i:
					result[i].append(1)   #数组第一个数和最后一个数  均为1
				else:
					result[i].append(result[i-1][j-1] + result[i -1][j])   #这一行的数 是上一行的两个数 相加 
		return result


if __name__ == "__main__":
    print(Solution().generate(5))

