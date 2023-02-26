class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        curr = defaultdict(int)
        max_ = 0
        b = False
        for i in range(len(s)):
            curr[s[i]] += 1
            if sum(curr.values()) - max(curr.values()) <= k:
                max_ = max(max_,i - left + 1)
            while sum(curr.values()) - max(curr.values()) > k:
                b = True
                curr[s[left]] -= 1
                if curr[s[left]] == 0: 
                    del curr[s[left]]
                left += 1
        if not b:
            return len(s)
                   
        return max_
