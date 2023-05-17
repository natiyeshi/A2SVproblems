class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        dic = {i : i for i in range(n)}
        
        def find(ind):
            if dic[ind] != ind:
                return find(dic[ind])
            return ind
        
        def union(x,y):
            xrep = find(x)
            yrep = find(y)
            
            dic[xrep] = yrep
        
        for x,y in edges:
            union(x,y)
        
        return find(source) == find(destination)