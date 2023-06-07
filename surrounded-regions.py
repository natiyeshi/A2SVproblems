class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        result = []

        def checker(row,col):
            if (0 <= col < len(board[0])) and (0 <= row < len(board)): 
                return True
            return False
        b = False
        visited = set()

        def inBorder(row,col):
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                return True
            return False

        def dfs(row,col):
            nonlocal b
            if not checker(row,col) or board[row][col] == "X" or (row,col) in visited:
                return [True,[]]
            
            if inBorder(row,col):
                return [False,[]]
            visited.add((row,col))
            temp = []
            r = True
            for i,j in directions: 
                res = dfs(row+i,col+j)
                temp.extend(res[1])
                r = r and res[0]                
            temp.append((row,col))
            return [r,temp]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    ans = dfs(i,j)
                    if ans[0]:
                        result.extend(ans[1])

        for row,col in result:
            board[row][col] = "X"