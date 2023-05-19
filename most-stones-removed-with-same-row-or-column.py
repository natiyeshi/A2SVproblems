class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {i : i for i in range(len(stones))}
        
        def find(ind):
            if parent[ind] != ind:
                parent[ind] = find(parent[ind])
            return parent[ind]
        
        def union(a,b):
            ap = find(a)
            bp = find(b)
            temp = min(ap,bp)
            parent[a] = parent[b] = parent[ap] = parent[bp] = temp
        
        for i in range(len(stones)):
            for j in range(i,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
                    
        counter = len(stones)
        
        for i in parent:
            if parent[i] == i:
                counter -= 1

        return counter