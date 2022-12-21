class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        y = len(x) - 1
        i = 0
        # for i in range(len(x)):
        #     if x[i] != x[y]:
        #         return False
        #     y -= 1
        while i < y:
            if x[i] != x[y]:
                return False
            y -= 1 
            i += 1            
        return True
        
        
        """
        :type x: int
        :rtype: bool
        """
        