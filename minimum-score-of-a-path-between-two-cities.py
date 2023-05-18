class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dic = {i + 1 : i + 1 for i in range(n + 1)}
        def find(ind):
            if dic[ind] != ind:
                dic[ind] = find(dic[ind])
                return dic[ind]
            return ind
        
        def union(x,y):
            xp = find(x)
            yp = find(y)
            m = min(xp,yp)
            dic[x] = dic[y] = dic[xp] = dic[yp] = m
        for a,b,j in roads:
            union(a,b)

        result = float("inf")
        for a,b,k in roads:
            ap = find(a)
            bp = find(b)
            if ap == bp == 1:
                result = min(result,k)
        return result