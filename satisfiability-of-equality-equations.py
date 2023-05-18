class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        parent = {chr(i) : chr(i) for i in range(97,123)}

        def find(ind):
            if parent[ind] != ind:
                parent[ind] = find(parent[ind])
            return parent[ind]
        
        def union(f,t):
            print(f,t)
            fp = find(f)
            tp = find(t)
            m = chr(min(ord(fp),ord(tp)))
            parent[f] = parent[t] = parent[fp] = parent[tp] = m

        for temp in equations:
            if temp[1] == "=":
                union(temp[0],temp[3])
        for temp in equations:
            if temp[1] == "!":
                if find(temp[0]) == find(temp[3]):
                    return False
        return True