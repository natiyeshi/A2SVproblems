class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:return True
        graph = defaultdict(set)
        for i in edges:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])
        f = False
        visited = set()
        def dfs(temp):
            nonlocal f,graph
            visited.add(temp)
            arr = graph[temp]
            print(arr)
            for i in arr:
                if i == destination:
                    f = True
                    return
                if i not in visited:
                    dfs(i)
        dfs(source)
        return f