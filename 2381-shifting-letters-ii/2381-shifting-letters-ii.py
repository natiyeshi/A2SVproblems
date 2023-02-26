class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        change = [ 0 for i in s]
        s = list(s)
        
        for start,end,direction in shifts:
            if direction == 1:
                change[start] += 1
                if end + 1 < len(s):
                    change[end + 1] -= 1
            else:
                change[start] -= 1
                if end + 1 < len(s):
                    change[end + 1] += 1
        preChange = [0] 
        
        for i in change:
            preChange.append(preChange[-1] + i)
    
        for i in range(1,len(preChange)):
            char = (((ord(s[i - 1])) + preChange[i] - 97) % 26) + 97
            s[i - 1] = chr(char)
            
        return "".join(s)