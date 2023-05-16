class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        visited = set()
        graph = defaultdict(list)
        result = 0
        
        for f,t in edges:
            graph[f].append(t)
            graph[t].append(f)
        ans = set()
        def dfs(curr = 0):
            find = [False,0]
            visited.add(curr)
            for i in graph[curr]:
                if i not in visited:
                    temp = dfs(i)
                    if temp[1]:
                        ans.add((curr,i))
                        ans.add((i,curr))
                    find = [find[0] or temp[0],find[1] + temp[1]]
            if find[0] or hasApple[curr]:
                return [True,2 + find[1]]
            return [False,0]
                    
        dfs()
        return len(ans)