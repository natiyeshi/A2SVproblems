class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n < 1:
            neg = True
            n = abs(n)
            x = 1 / x
        if n % 2 == 0:
            ans = self.myPow(x , n // 2)
            return ans ** 2
        return x * self.myPow(x,n - 1)