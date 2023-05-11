class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        degree = defaultdict(int)

        for val,pre in prerequisites:
            graph[pre].append(val)
            degree[val] += 1
        que = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                que.append(i)
        result = []
        while que:
            node = que.popleft()
            result.append(node)
            for j in graph[node]:
                degree[j] -= 1
                if degree[j] == 0:
                    que.append(j)
        return len(result) == numCourses