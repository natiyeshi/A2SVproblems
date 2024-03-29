class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        for i in edges:
            graph[i[1]] = 1
        result = []
        for i in range(n):
            if graph[i] == 0:
                result.append(i)
        return result