class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        curr = 1
        memo = [-1 for i in range(len(nums) + 1)]
        def dp(ind,s):
            nonlocal curr
            if not (0 <= ind < len(nums) - curr):
                return s
            if memo[ind] == -1:
                memo[ind] = max(dp(ind + 2,nums[ind]),dp(ind + 3,nums[ind]))
            return memo[ind] + s
        
        op1 = dp(0,0)
        curr = 0
        memo = [-1 for i in range(len(nums) + 1)]
        return max(op1,dp(1,0),dp(2,0))