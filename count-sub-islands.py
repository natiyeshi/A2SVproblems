class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        visited = set()
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def inBound(row,col):
             return -1 < row < len(grid2) and -1 < col < len(grid2[0]) and grid2[row][col] == 1 and (row,col) not in visited
            
        def dfs(row,col):
            if not inBound(row,col):
                return True
            visited.add((row,col))
            temp = grid1[row][col] == 1
            for x,y in directions:
                temp = dfs(row + x,col + y) and temp
            return temp
        result = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    if dfs(i,j): 
                        result += 1
        return result