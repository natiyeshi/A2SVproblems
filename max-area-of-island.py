class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        temp = 0
        result = 0

        isValid = lambda row, col: 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col] == 1 and (row, col) not in visited

        def visite(row,col, temp = [0]):
            temp[0] += 1
            visited.add((row,col))
            for x,y in direction:
                new_row, new_col = row+x, col+y
                if isValid(new_row, new_col):
                    visite(new_row, new_col, temp)
            return temp[0]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                curr = grid[row][col]
                if curr == 1 and (row,col) not in visited:
                    temp = [0]
                    result = max(result,visite(row,col,temp))
        return result