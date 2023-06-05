class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(ind):
            if ind >= len(questions):
                return 0
            if ind not in memo:
                a = dp(ind + 1)
                b = dp(ind + questions[ind][1] + 1) + questions[ind][0]
                memo[ind] = max(a,b)
            return memo[ind]
        return dp(0)