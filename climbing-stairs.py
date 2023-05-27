class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        memo = [-1 for i in range(n)]
        def dp(i,count):
            if i >= n:
                return count
            if memo[i] == -1:
                memo[i] = dp(i + 1,count) + dp(i + 2,count + 1)
            return memo[i]
        return dp(0,0)