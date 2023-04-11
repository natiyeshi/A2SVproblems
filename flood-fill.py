class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        newColor = image[sr][sc] 
        visited = set()
        def dfs(row,col):
            nonlocal newColor
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
                return
            
            if image[row][col] != newColor or (row,col) in visited:
                return
            image[row][col] = color
            visited.add((row,col))
            for r,c in directions:
                dfs(row+r,col+c)
        dfs(sr,sc)
        return image