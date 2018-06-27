def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res