class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        graph = defaultdict(list)
        for ind,val in enumerate(parent):
            graph[val].append(ind)
        result = 0
        def dfs(ind,path):
            nonlocal result
            m1 = m2 = 0
            for val in graph[ind]:
                temp = dfs(val,s[ind])
                if temp > m1:
                    m2 = m1
                    m1 = temp
                elif temp > m2:
                    m2 = temp
            result = max(result,m1 + m2 + 1)
            # print(path,s[ind],m1 + m2)
            if s[ind] != path:
                return m1 + 1
            return 0
        dfs(0,"")

        return result