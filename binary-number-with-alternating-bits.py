class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        temp = n & 1
        n >>= 1
        while n:
            if temp == n & 1:
                return False
            temp = n & 1 
            n >>= 1
        return True