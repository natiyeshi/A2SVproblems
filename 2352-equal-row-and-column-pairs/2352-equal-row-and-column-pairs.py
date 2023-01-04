class Solution(object):
    def equalPairs(self, grid):
        column = defaultdict(int)
        counter = 0
        for col in range(len(grid[0])):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row][col])
            column[tuple(temp)] += 1
        for row in grid:
            if tuple(row) in column:
                counter += column[tuple(row)]
        return counter
    
            
    
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        