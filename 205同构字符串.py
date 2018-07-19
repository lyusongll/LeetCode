class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sourceMap, targetMap = dict(), dict()
        for x in range(len(s)):
            source, target = sourceMap.get(t[x]), targetMap.get(s[x])   #取s，t相对应的位置的数，
            if source is None and target is None:                         #如果两个数不存在，则相互以对方字母存入 哈希表中，
                sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:   #如果字母存在，相互比较 位置
                return False
        return True