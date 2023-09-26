class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        memo = {}
        def dp(i,j):
            if i >= len(dungeon) or j >= len(dungeon[0]):
                return float("-inf")
            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                if dungeon[i][j] <= 0:
                    return dungeon[i][j] 
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            temp = max(dp(i+1,j),dp(i,j+1)) + dungeon[i][j]
            memo[(i,j)] = 0 if temp > 0 else temp
            return memo[(i,j)] 
        temp = dp(0,0)
        if temp > 0:
            return 0
        return abs(temp) + 1