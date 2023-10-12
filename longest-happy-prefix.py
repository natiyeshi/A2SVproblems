class Solution:
    def longestPrefix(self, s: str) -> str:
        
        LPS = [0 for _ in range(len(s))]
        prev , curr = 0 , 1
        while curr < len(s):
            if s[curr] == s[prev]:
                prev += 1
                LPS[curr] = prev
                curr += 1
            else:
                if prev == 0:
                    curr += 1
                else:
                    prev = LPS[prev - 1]
        ans = ""
        m = float("inf")
        prev , curr = 0 , 1
        while curr < len(s):
            if s[curr] == s[prev]:
                curr += 1
                prev += 1
            else:
                if prev == 0:
                    curr += 1
                else:
                    prev = LPS[prev - 1]
        
        return s[:prev]