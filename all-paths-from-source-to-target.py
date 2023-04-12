class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        def dfs(ind,ans = []):
            temp = graph[ind]
            ans.append(ind)
            if ind == len(graph) - 1:
                    result.append(ans)
                    return 
            for i in temp:
                dfs(i,ans[:])
                
        dfs(0)
        return result