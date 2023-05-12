class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for f,t in richer:
            graph[t].append(f)
        small = float("inf")
        def dfs(i):
            nonlocal small
            if small != float("inf"):
                small = i if quiet[i] < quiet[small] else small
            else:
                small = i
            for i in graph[i]:
                dfs(i)

        result = []
        for i in range(len(quiet)):
            dfs(i)
            result.append(small)
            small = float("inf")
        return result