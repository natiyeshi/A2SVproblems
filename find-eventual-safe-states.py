class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        flag = defaultdict(int)
        
        def dfs(ind):

            if flag[ind] == 2:
                return True
            if flag[ind] == 1:
                return False
            flag[ind] = 1
            for val in graph[ind]:
                if not dfs(val):
                    return False
            flag[ind] = 2
            return True

        result = []

        for i,values in enumerate(graph):
            if dfs(i):
                result.append(i)

        result.sort()
        
        return result