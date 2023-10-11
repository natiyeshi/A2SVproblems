class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        cutted = 0

        def dfs(node,parent):
            nonlocal cutted
            cur_val = values[node]

            for nb in graph[node]:
                if nb != parent:
                    cur_val += dfs(nb,node)
            
            if cur_val % k == 0:
                cutted += 1 
                cur_val = 0
            
            return cur_val 
        x = dfs(0,-1)

        return cutted