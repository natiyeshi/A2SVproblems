class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        check = lambda i , j: -1 < i < m and -1 < j < n
        memo = {}
        def dp(i,j):
            if not check(i,j):
                return 0
            if i == m - 1 and j == n - 1:
                return 1 
            if (i,j) not in memo:
                memo[(i,j)] = dp(i + 1,j) + dp(i , j + 1)
            return memo[(i,j)]

        return dp(0,0)