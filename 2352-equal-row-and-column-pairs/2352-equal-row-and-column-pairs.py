class Solution(object):
    def equalPairs(self, grid):
        ar = []
        c = 0
        for k in range(len(grid[0])):
            st = ""
            for i in range(len(grid)):
                st += "," + str(grid[i][k])
            ar.append(st[1:])
        for i in grid:
            st = ",".join(map(str,i))
            for i in ar:
                if i == st:
                    c += 1
        return c
    
            
    
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        