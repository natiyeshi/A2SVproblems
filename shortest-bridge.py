class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        c = 0
        color = {0:"a",1:"b"}
        def bfs(row,col):
            que = deque()
            temp = []
            que.append((row,col))
            while que:
                i,j = que.popleft()
                grid[i][j] = color[c]
                temp.append((i,j))
                for x,y in directions:
                    a , b = x + i, y + j
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and (a,b) not in visited:
                        if grid[a][b] == 1:
                            que.append((a,b))
                            visited.add((a,b))
            return temp
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans.append(bfs(i,j))
            if len(ans) == 2: break
        result = float("inf")
        print(ans)
        for i in range(len(ans[0])):
            for j in range(len(ans[1])):
                a,b = ans[1][j]
                c,d = ans[0][i]
                result = min(result,abs(a - c) + abs(b - d))
                if result - 1 == 1: return result - 1
        
        return result - 1