class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        half = ceil(s / 2)
        memo = {}
        def dp(ind,add):
            if add >= half or ind >= len(stones):
                return abs(2*add - s)
            if (ind,add) in memo:
                return memo[(ind,add)]
            memo[(ind,add)] = min(dp(ind + 1,add + stones[ind]),dp(ind + 1,add))
            return memo[(ind,add)]
        return dp(0,0)