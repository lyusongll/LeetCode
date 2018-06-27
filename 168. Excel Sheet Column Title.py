class Solution:
	def converToTitle(self,n):
		result, dvd = '',n
		while dvd:
			result += chr((dvd-1) % 26+ord("A"))
			dvd = (dvd-1) //26

		return result[::-1]

if __name__ == '__main__':
	for i in range(1,29):
		print(Solution().converToTitle(i))


# print(chr(97))
#Excel序是这样的：A~Z, AA~ZZ, AAA~ZZZ, ……

#本质上就是将一个10进制数转换为一个26进制的数

#注意：由于下标从1开始而不是从0开始，因此要减一操作。