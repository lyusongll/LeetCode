class Solution:
	def getRow(self, rowIndex):
		result = [0] * (rowIndex+1)
		for i in range(rowIndex+1):
			old = result[0] = 1
			for j in range (1,i+1):
				old, result[j] = result[j],old +result[j]
		return result

if __name__ == "__main__":
    print(Solution().getRow(3))
