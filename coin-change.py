class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort(reverse=True) 
        def dp(curr):
            num = float("inf")
            if curr < 0:
                return float("inf")
            if curr == 0:
                return 0    
            if curr in memo:
                return memo[curr]
            for i in range(len(coins)):
                if curr - coins[i] >= 0:
                    num = min(num,dp(curr - coins[i]))
            memo[curr] = num + 1
            return memo[curr]
        result = dp(amount)
        if result == float("inf"):
            return -1
        return result