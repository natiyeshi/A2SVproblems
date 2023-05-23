class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        par = {i : i for i in range(len(points))}
        
        def find(val):
            if par[val] != val:
                par[val] = find(par[val])
            return par[val]

        def union(a,b):
            ap = find(a)
            bp = find(b)
            par[ap] = par[bp] = par[a] = par[b] = min(ap,bp,a,b)
        dic = []
        for i in range(len(points)):
            curr = points[i]
            for j in range(i + 1,len(points)):
                temp = points[j]
                l = abs(temp[0] - curr[0]) + abs(temp[1] - curr[1])  
                dic.append([l,i,j])
        dic.sort()
        result = 0
        for l,i,j in dic:
            if find(i) != find(j):
                result += l
                union(i,j)
        return result