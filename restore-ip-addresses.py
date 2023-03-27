class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # s = list(s)
        result = []
        def backtrack(start = 0, curr = []):
            if len(curr) == 3:
                if not (len(s[start:]) < 1 or int(s[start:]) > 255 or (len(s[start:]) > 1 and s[start]=="0")):
                    curr.append(s[start:])
                    result.append(".".join(curr))
                return
                    
            for i in range(start,len(s)):
                cell = s[start:i+1]
                if int(cell) > 255 or (cell[0] == "0" and len(cell) > 1):
                    return
                curr.append(cell)
                backtrack(i+1,curr[:])
                curr.pop()
        if len(s) > 3: backtrack()

        return result