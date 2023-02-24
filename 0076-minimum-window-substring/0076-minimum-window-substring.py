class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        left = right = 0
        window = defaultdict(int)
        ind = []
        
        counter = 0
        while right < len(s):
            
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                counter += 1
                
            while counter == len(target):
                
                if not ind or  right - left < ind[1] - ind[0]:
                    ind = [left,right]
                    
                window[s[left]] -= 1
                if window[s[left]] < target[s[left]]:
                    counter -= 1
                        
                left += 1  
                
            right += 1
        
        return s[ind[0]:ind[1]+1] if ind else ''
            