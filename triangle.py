class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(ind,level):
            if level >= len(triangle):
                return 0
            p1 = p2 = float("inf")
            if ind <= len(triangle[level]):
                if (level,ind) not in memo:
                    memo[(level,ind)] = dp(ind,level + 1)
                p1 = memo[(level,ind)]
            if ind + 1 <= len(triangle[level]):
                if (level,ind + 1) not in memo:
                    memo[(level,ind + 1)] = dp(ind + 1,level + 1)
                p2 =  memo[(level,ind + 1)]
            ans = min(p1,p2)
            if ind < len(triangle[level]):
                ans += triangle[level][ind]
            return ans
        
        return dp(0,0)