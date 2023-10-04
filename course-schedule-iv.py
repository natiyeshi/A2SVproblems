class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        dist = [[False] * n for _ in range(n)]

        for i, j in prerequisites:
            dist[i][j] = True

        for i in range(n):
            dist[i][i] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = dist[i][j] or dist[i][k] and dist[k][j]
        return [dist[u][v] for u,v in queries]