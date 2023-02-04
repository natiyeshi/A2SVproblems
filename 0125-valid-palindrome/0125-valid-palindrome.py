class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        newS = []
        for i in s:
            if i.isalpha() or i.isdigit():
                newS.append(i)
        
        start = 0
        end = len(newS) - 1
        
        while start < end:
            if newS[start] != newS[end]:
                return False
            start += 1
            end -= 1
            
        return True
        
        
        """
        :type s: str
        :rtype: bool
        """
        