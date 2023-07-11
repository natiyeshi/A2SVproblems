class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        m = values[0] + values[1] - 1 
        ind  = 1 if values[0] < values[1] + 1 else 0

        for k in range(2,len(values)):
            m = max(m,values[ind] + values[k] - ( k - ind))
            if values[ind] <= values[k] + (k - ind):
                ind = k
        return m