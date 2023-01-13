class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        arr = [[ 0 for _ in range(n - 2) ] for _ in range(n - 2)]
       
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                # print(grid[i][j:j + 3])
                m = max(grid[i][j:j + 3])
                m = max(max(grid[i+1][j:j + 3]), m)
                m = max(max(grid[i+2][j:j + 3]), m)
               
                arr[i][j] = m
                
        return arr
        
        
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        