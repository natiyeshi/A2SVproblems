class Solution(object):
    def equalPairs(self, grid):
        column = []
        counter = 0
        for col in range(len(grid[0])):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row][col])
            column.append(temp)
        for row in grid:
            for col in column:
                if row == col:
                    counter += 1
        return counter
    
            
    
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        