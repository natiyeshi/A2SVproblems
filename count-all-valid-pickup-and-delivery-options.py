class Solution:
    def countOrders(self, n: int) -> int:
        
        def count(n):
            if n == 1:
                return 1
            return n*(2*n - 1) * count(n - 1)
        return count(n) % (10**9 + 7)