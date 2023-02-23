class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = Counter(s1)
        wd = Counter(s2[:len(s1)])
        left = 0
        right = len(s1)
        while right < len(s2):
            if wd == temp:
                return True
            wd[s2[right]] += 1 
            wd[s2[left]] -= 1
            if wd[s2[left]] == 0:
                del wd[s2[left]]
            left += 1
            right += 1
            
        if wd == temp or s1 == s2:
            return True
        return False

        