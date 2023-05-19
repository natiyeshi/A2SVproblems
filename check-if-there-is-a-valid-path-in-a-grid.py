class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        m = {
            1:set(["l","r"]), 2:set(["t","b"]), 3:set(["l","b"]),
            4:set(["b","r"]), 5:set(["l","t"]), 6:set(["t","r"]),
        }
        dr = {
            "l" : (0,-1), "r" : (0,1),
            "t" : (-1,0),"b" : (1,0)
        }
        flip = {
            "b" : "t","l":"r","r":"l","t":"b"
        }
        visited = set()
        result = True
        checker = lambda a,b: 0 <= a < len(grid) and 0 <= b < len(grid[0])
        def dfs(x=0,y=0,fr=""):
            nonlocal result
            if fr != "" and fr not in m[grid[x][y]]:
                # print(fr,grid[x][y])
                result = False
                return
            visited.add((x,y))
            for val in m[grid[x][y]]:
                i,j = dr[val]
                if (x+i,y+j) not in visited and checker(x+i,y+j):
                    dfs(x+i,y+j,flip[val])
                    # return
        dfs(0,0)
        
        if (len(grid) - 1,len(grid[0]) - 1) not in visited:
            return  False 
        return result