# 题目标签：Array

# 　　题目给了我们一个数组 和 k。 让我们 旋转数组 k 次。

# 　　这里有一个很巧妙的方法：

# 　　　　利用数组的length - k 把数组 分为两半；

# 　　　　reverse 左边和右边的数组；

# 　　　　reverse 总数组。

 

# 　　举一个例子： 

# 　　1 2 3 4 5 6 7　　如果k = 3 的话， 会变成 5 6 7 1 2 3 4

# 　　1 2 3 4 5 6 7　　middle = 7 - 3 = 4，分为左边 4个数字，右边 3个数字

# 　　4 3 2 1 7 6 5　　分别把左右reverse 一下

# 　　5 6 7 1 2 3 4　　把总数组reverse 一下就会得到答案


class Solution:
	def rotate(self, nums,k)
		n= len(nums)
		self.reverse(nums,0,n-k)
		self.reverse(nums,n-k,n)
		self.reverse(nums,0,n)

	def reverse(self,nums, start ,end)
		while start <end:
			nums[start],nums[end-1] = nums[end-1],nums[start]
			start += 1
			end -=1


#方法2
	def rotate2(self,nums,k):
		nums[:] = nums[len(nums)-k:] + nums[:len(nums) - k]
        


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    print nums