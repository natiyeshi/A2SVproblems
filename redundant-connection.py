class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        visited = set()
        graph = {i : i for i in range(len(edges)+1)}
        def find(ind):
            if graph[ind] != ind:
                return find(graph[ind])
            return ind
        for x,y in edges:
            xrep = find(x)
            yrep = find(y)
            if (x not in visited or y not in visited or xrep != yrep):
                graph[xrep] = yrep
                visited.add(x)
                visited.add(y)
            else:
                return [x,y]