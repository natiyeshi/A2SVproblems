class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for f,t in richer:
            graph[t].append(f)
        small = float("inf")
        visited = set()
        def dfs(i):
            nonlocal small
            visited.add(i)
            if small != float("inf"):
                small = i if quiet[i] < quiet[small] else small
            else:
                small = i
            for j in graph[i]:
                if j not in visited:
                    dfs(j)

        result = []
        for i in range(len(quiet)):
            dfs(i)
            visited = set()
            result.append(small)
            small = float("inf")
            
        return result