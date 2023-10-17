class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        a = (pow(5,ceil(n / 2),10**9 + 7))
        b = (pow(4,floor(n / 2),10**9 + 7))
        ans = (a * b) % (10**9 + 7) 
        return ans