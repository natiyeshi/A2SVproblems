class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        wd = len(s1)
        st = 0
        while wd < len(s2) + 1:
            temp = "".join(sorted(s2[st:wd]))
            if s1 == temp:
                return True
            st += 1
            wd += 1
        else:
            if s1 == s2:
                return True
        return False
            
        