class Solution(object):
    def countGoodSubstrings(self, s):
        
        end = 2
        count = 0
        while end < len(s):
            if s[end] != s[end-1] != s[end-2] and s[end] != s[end-2]: 
                count += 1
            end += 1
        
        return count
        
        
        """
        :type s: str
        :rtype: int
        """
        