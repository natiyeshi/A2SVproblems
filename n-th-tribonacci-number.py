class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1 for i in range(n + 1)]
        def dp(curr):
            if curr < 3:
                return 0 if curr == 0 else 1
            if memo[curr] == -1:
                memo[curr] = dp(curr - 1) + dp(curr - 2) + dp(curr - 3) 
            return memo[curr]
        return dp(n)