class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)

        for f,t in prerequisites:
            graph[t].append(f)
        visited = set()
        def dfs(node,find):
            visited.add(node)
            for i in graph[node]:
                if i in visited:
                    continue
                if i == find:
                    return True
                if dfs(i,find):
                    return True
            return False
        result = []

        for i,j in queries:
            result.append(dfs(j,i))
            visited = set()

        return result