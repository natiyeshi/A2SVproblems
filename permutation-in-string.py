class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        find = Counter(s1)            
        for i in range(len(s2)):
            if s2[i] in find:
                if find == Counter(s2[i:i+len(s1)]):
                    return True
        return False