class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        line = []
        for itr in trips:
            line.append((itr[1],itr[0]))
            line.append((itr[2],-itr[0]))
        line.sort()
        
        for itr in line:
            capacity -= itr[1]
            if capacity < 0:
                return False
        return True
        
        return max(dic.values()) <= capacity