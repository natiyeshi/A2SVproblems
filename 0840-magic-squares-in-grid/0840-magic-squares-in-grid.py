class Solution(object):
    def numMagicSquaresInside(self, grid):
        
        # 1,1
        row = len(grid)
        col = len(grid[0])
        
        if row < 3 or col < 3:
            return 0
        i = 0 
        j = 0
        counter = 0
        
        for r in range(row - 2):
            j = 0
            for c in range(col - 2):
                arr = set()
                val = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                flag = True
                if grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != val:
                    flag = False
                elif grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != val:
                    flag = False
                elif grid[i][j] + grid[i+1][j] + grid[i+2][j] != val:
                    flag = False
                elif grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != val:
                    flag = False
                elif grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != val:
                    flag = False
                elif grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != val:
                    flag = False
                elif grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != val:
                    flag = False
                
                
                
                for k in range(i,i + 3):
                    for w in range(j,j+3):
                        arr.add(grid[k][w])
                        if grid[k][w] > 9 or grid[k][w] < 1:
                            flag = False
                            break
                            
                if flag is False:
                    j += 1
                    continue
                    
                j += 1
                if len(arr) < 9:
                    continue
                counter += 1
                
            i += 1
        return counter
                
                
                
                
            
        
        
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        