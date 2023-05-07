class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(curr):
            visited.add(curr + 1)
            for i,val in enumerate(isConnected[curr]):
                if val == 1 and i + 1  not in visited:
                    dfs(i)
        pr = 0
        for i,conn in enumerate(isConnected):
            if i + 1 in visited:
                continue
            pr += 1
            visited.add(i + 1)
            for j,val in enumerate(conn):
                if val == 1 and j + 1 not in visited:
                    dfs(j)
        return pr