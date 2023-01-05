class Solution(object):
    def onesMinusZeros(self, grid):
        trans = list(list(x) for x in zip(*grid))
        row = []
        col = []
        for i in grid:
            s = sum(i)
            s -= len(grid[0]) - s
            row.append(s)
        for j in trans:
            s = sum(j)
            s -= len(trans[0]) - s
            col.append(s)
        print(row,col)
        ans = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
        for i in range(len(row)):
            for j in range(len(col)):
                ans[i][j] = row[i] + col[j]
                
        return ans
        
                
            