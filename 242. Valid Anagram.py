def isAnagram1(self,s,t):
	dict1, dict2 = {}, {}
	for item in s:
		dict1[item] = dict1.get(item, 0) +1
	for item in t:
		dict2[item] = dict2.get(item, 0) +1
	return dict1 == dict2


def isAnagram2(self,s,t):
	return sorted(s) = sorted(t)