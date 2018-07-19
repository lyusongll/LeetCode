本题最重要的是思路的转化，我们要找妹妹可以获取的糖果最多的种类数量，那么我们只需要知道糖果总的种类数量，由于弟弟妹妹平分偶数个糖果，那么我们比较糖果总的种类数量和每个人可以获取的糖果数量，如果种类数较多，妹妹获取的糖果每个都可以不同。如果种类数较少，那么妹妹每种糖果都可以获得一颗


解题思路：
返回 min( 糖果总数的一半, 糖果种类数 ) 即可

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) / 2, len(set(candies)))   #种类少，则均分的话，每个种类都可分到，种类多的话，糖果只能分总数的一半