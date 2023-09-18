class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        bbbab
        """ 
        memo = {} 
        def dp(l,r):
            temp = 0
            if l > r:
                return 0
            if l == r:
                return 1
            if (l,r) in memo:
                return memo[(l,r)]
            if s[l] == s[r]:
                memo[(l,r)] = dp(l+1,r-1) + 2
            else:
                memo[(l,r)] = max(dp(l,r-1),dp(l+1,r))
            return memo[(l,r)] 
        return dp(0,len(s)-1)