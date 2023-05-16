class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = defaultdict(list)
        result = [0 for i in range(n)]

        for f,t in edges:
            graph[f].append(t)
            graph[t].append(f)
        visited = set()
        def dfs(curr = 0):
            visited.add(curr)
            temp = defaultdict(int)
            for i in graph[curr]:
                if i in visited:
                    continue
                child = dfs(i)
                for j in child:
                    temp[j] += child[j]
            temp[labels[curr]] += 1
            result[curr] = temp[labels[curr]] 
            
            return temp
        for i in range(n):
            if i not in visited:
                dfs(i)

        return result