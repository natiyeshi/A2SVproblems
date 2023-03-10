class Solution:
    def splitString(self, s: str) -> bool:
        
        temp = []
        def backtrack(ind):
            if ind >= len(s):
                print(temp)
                return len(temp) > 1
            for i in range(ind,len(s)):
                val = int(s[ind: i + 1])
                if len(temp) == 0 or val + 1 == temp[-1]:
                    temp.append(val)
                    if backtrack(i + 1):
                        return True
                    temp.pop()
        
        return backtrack(0)