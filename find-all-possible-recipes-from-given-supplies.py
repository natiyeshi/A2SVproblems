class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        degree = defaultdict(int)

        que = deque()
        for i,val in enumerate(recipes):
            for items in ingredients[i]:
                if items not in supplies:
                    graph[items].append(val)
                    degree[val] += 1
            if degree[val] == 0:
                que.append(val)
        result = []
        while que:
            node = que.popleft()
            result.append(node)
            for i in graph[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    que.append(i)

        return result