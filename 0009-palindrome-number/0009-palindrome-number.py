class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        y = len(x) - 1
        for i in range(len(x)):
            if x[i] == x[y]:
                pass
            else:
                return False
            y -= 1
        return True
        
        
        """
        :type x: int
        :rtype: bool
        """
        