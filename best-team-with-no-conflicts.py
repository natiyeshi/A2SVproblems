class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        values = [(ages[i],scores[i]) for i in range(len(ages))]
        values.sort()
        result = 0  
        dp = [values[0][1]]

        for i in range(1,len(values)):
            m = 0
            for j in range(i - 1,-1,-1):
                if values[j][1] <= values[i][1] or values[i][0] == values[j][0]:
                    m = max(m,dp[j])
            dp.append(m + values[i][1])
        return max(dp)