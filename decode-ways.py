class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1 for i in range(len(s) + 1)]
        def dp(ind,val):
           
            if val[0] == '0' or int(val) > 26:
                return 0
            if ind >= len(s):
                return 1
            if memo[ind] != -1:
                return memo[ind]
            if ind + 1 < len(s):
                memo[ind] = dp(ind + 2,s[ind : ind + 2]) + dp(ind + 1,s[ind: ind + 1])
            else:
                memo[ind] = dp(ind + 1,s[ind: ind + 1])
            return memo[ind]
        return dp(0,"9")