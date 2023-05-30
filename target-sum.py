class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def bt(ind,s):
            if ind >= len(nums):
                if s == target:
                    return 1
                return 0
            if (ind,s) not in memo:
                memo[(ind,s)] = bt(ind + 1,s - nums[ind]) + bt(ind + 1,s + nums[ind])
            return memo[(ind,s)]

        return bt(0,0)