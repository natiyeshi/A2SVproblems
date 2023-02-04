class Solution(object):
    def reverseWords(self, s):
        
        newS = s.split(" ")
        arr = []
        for i in newS:
            arr.append(i[::-1]) 
            
        return " ".join(arr)
        
        """
        :type s: str
        :rtype: str
        """
        