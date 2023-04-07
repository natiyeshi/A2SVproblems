class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(set)
        for i in roads:
            graph[i[0]].add(i[1]) 
            graph[i[1]].add(i[0]) 
        result = 0
        for i in range(n):
            for j in range(n):
                if i == j:continue
                temp = len(graph[j]) + len(graph[i])
                if j in graph[i] or i in graph[j]:
                    temp -= 1
                result = max(temp,result)
        return result