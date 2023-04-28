class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        que = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0: que.append((i,j))
                else: mat[i][j] = -1

        def checker(x,y):
            temp = 0 <= x < len(mat) and 0 <= y < len(mat[0])
            return temp

        while que:
           x,y = que.popleft()
           for i,j in directions:
               if checker(x + i,y + j) and mat[x + i][y + j] == -1:
                   mat[x + i][y + j] = mat[x][y] + 1
                   que.append((x + i, y + j))
        return mat