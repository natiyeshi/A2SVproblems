class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        que = deque()
        que.append(tuple(entrance))
        visited = set()
        visited.add(tuple(entrance))
        counter = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        checker = lambda a,b: 0 <= a < len(maze) and 0 <= b < len(maze[0]) and maze[a][b] == "."
        while que:
            level = len(que)  
            for _ in range(level):
                x,y = que.popleft()
                if x == len(maze) - 1 or y == len(maze[0]) - 1 or x == 0 or y == 0:
                    if x != entrance[0] or y != entrance[1]:
                        return counter 
                print(x,y)
                for a,b in directions:
                    if checker(x + a,y + b) and (x+a,y+b) not in visited:
                        que.append((x + a,y + b))
                        visited.add((x+a,y+b))
            counter += 1
        return -1