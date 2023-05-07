class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        que = deque()
        que.append((click[0],click[1]))
        visited = set()
        directions = [
            (0,1),(0,-1),(1,1),(-1,1),
            (1,0),(-1,0),(-1,-1),(1,-1),
        ]

        checker = lambda a,b: 0 <= a < len(board) and 0 <= b < len(board[0]) 

        def color(x,y):
            counter = 0
            for i,j in directions:
                if checker(x+i,y+j) and board[x+i][y+j] == "M":
                    counter += 1
            return counter
            
        while que:
            i,j = que.popleft()
            temp = color(i,j)
            if board[i][j] == "M":
                board[i][j] = "X"
                return board
            if temp > 0:
                board[i][j] = str(temp)
                continue
            else:
                board[i][j] = "B"
            for x,y in directions:
                if not checker(x + i, y + j): 
                    continue
                if board[x + i][y + j] == "M":
                    board[x + i][y + j] = "X"
                    return board
                if board[x + i][y + j] == "E" and (x+i,j+y) not in visited:
                    visited.add((x+i,y+j))
                    que.append((x + i,y + j)) 

        return board