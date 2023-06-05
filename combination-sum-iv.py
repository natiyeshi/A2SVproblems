class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(s):
            if s >= target:
                return s == target
            ans = 0
            if s in memo:
                return memo[s]
            for i in nums:
                ans += dp(s + i)
            memo[s] = ans
            return memo[s]
        return dp(0)