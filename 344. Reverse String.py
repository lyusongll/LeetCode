class Solution:
	def reverseString(self,s):
		return s[::-1]




    def reverseString(self,s):
    	s = list(s)
    	for i in range(0,len(s)/2):
	    	tmp = s[i]
	    	s[i] = s[len(s)-1 -i]
	    	s[len(s)-1-i] =tmp

	    return ''.join(s)
	    
