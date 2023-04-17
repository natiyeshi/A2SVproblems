class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dic = defaultdict(set)
        visited = defaultdict(int)
        for i,val in enumerate(graph):
            for j in val:
                dic[i].add(j)
                dic[j].add(i)
        result = True
        rev = lambda x: -1 if x == 1 else 1 
        def dfs(ind,color):
            nonlocal result
            if visited[ind] != 0:
                if visited[ind] != color:
                    result = False
                return
            visited[ind] = color
            childColor = rev(color)
            for i in dic[ind]:
                dfs(i,childColor)
        for i in range(len(graph)):
            if visited[i] == 0:
                dfs(i,1)
        return result