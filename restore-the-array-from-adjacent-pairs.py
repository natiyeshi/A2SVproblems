class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for f,t in adjacentPairs:
            graph[f].append(t)
            graph[t].append(f)
        visited = set()
        path = []
        def dfs(start):
            visited.add(start)
            path.append(start)
            for itr in graph[start]:
                if itr not in visited:
                    dfs(itr)
        for i in graph:
            if len(graph[i]) == 1:
                dfs(i)
                return path