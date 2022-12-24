class Solution(object):
    def findTheDifference(self, s, t):
        b = False
        s = list(s)
        for i in t:
            if i in s:
                s.remove(i)
            else:
                return i
                
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        