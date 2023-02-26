class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = defaultdict(int)
        
        for itr in trips:
            for i in range(itr[1],itr[2]):
                dic[i] += itr[0]
            
        return max(dic.values()) <= capacity