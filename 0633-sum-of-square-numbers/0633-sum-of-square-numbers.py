class Solution(object):
    def judgeSquareSum(self, c):
       
        sq = int(sqrt(c))
        
        for i in range(sq + 1):
            b = sqrt(c -(i*i))
            if b == int(b):
                return True
        return False
        
        """
        :type c: int
        :rtype: bool
        """
        