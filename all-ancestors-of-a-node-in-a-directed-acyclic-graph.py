class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)

        for f,t in edges:
            graph[t].append(f)
        tr = set()
        def dfs(val):
            for i in graph[val]:
                if i not in tr:
                    dfs(i)
                    tr.add(i)
        temp = []
        for i in range(n):
            dfs(i)
            t = sorted(list(tr))
            temp.append(t)
            tr = set()
        
        return temp