class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dis = [[] for i in range(n + 1)]
        for a,b in dislikes:
            dis[a].append(b)
            dis[b].append(a)

        checker = [0 for i in range(n + 1)]
        def rev(a):
            if a == 1:return -1
            return 1 

        def dfs(ind,color):
            if checker[ind] != 0:
               return checker[ind] == color
            checker[ind] = color
            childColor = rev(color)
            temp = []
            for i in dis[ind]:
                temp.append(dfs(i,childColor))

            return all(temp)

        return all(checker[i] != 0 or dfs(i,1) for i in range(1,n + 1))