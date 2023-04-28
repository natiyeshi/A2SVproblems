class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        def checker(x,y):
            check = 0 <= x < len(grid) and 0 <= y < len(grid[0])
            return check and grid[x][y] == 0
        visited = set()
        que = deque()
        que.append((0,0,1))
        dest = (len(grid) - 1,len(grid[0]) - 1)
        directions = [(0,-1),(0,1),(1,-1),(1,0),(-1,1),(-1,0),(1,1),(-1,-1)]
        while que:
            x,y,c = que.popleft()
            if (x,y) == dest:
                return c
            for i,j in directions:
                if checker(x+i,y+j) and (x+i,y+j) not in visited:
                    print(x+i,y+j)
                    que.append((x+i,y+j,c+1))
                    visited.add((x+i,y+j))
        return -1