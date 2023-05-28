class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [-1 for i in range(n + 1)]
        def dp(val):
            if val < 2:
                return val
            if memo[val] == -1:
                if val % 2 == 0:
                    memo[val] = dp(val // 2)
                else:
                    memo[val] = dp((val // 2)) + dp((val // 2) + 1)
            return memo[val] 
        if n < 2:
            return n
        for i in range(len(memo) - 1,-1,-1):
            dp(i)
        return max(memo)