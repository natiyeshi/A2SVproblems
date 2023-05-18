class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic = {chr(i) : chr(i) for i in range(97,123) }
        def find(ind):
            if dic[ind] != ind:
                return find(dic[ind])
            return ind
        def union(f,t):
            fs = find(f)
            ts = find(t)
            temp = chr(min(ord(fs),ord(ts)))
            dic[f] = dic[t] = dic[fs] = dic[ts] = temp
            
        for i in range(len(s1)):
            union(s1[i],s2[i])
        result = []
        for i in range(len(baseStr)):
            temp = find(baseStr[i])
            result.append(temp)
        return "".join(result)