class Solution:
    def minSteps(self, n: int) -> int:
        
        result = 0
        d = 2

        while n > 1:
            while n % d == 0:
                n //= d
                result += d
            d += 1
        return result