class Solution:
    def balancedString(self, s: str) -> int:
        count = len(s) // 4
        fre = Counter(s)
        temp =  defaultdict(int)
        left = 0
        for i in fre:
            if fre[i] > count:
                temp[i] = fre[i] - count
        curr = defaultdict(int)
        counter = 0
        min_ = float("inf")
        for i in range(len(s)):
            curr[s[i]] += 1
            counter += 1
            if curr["W"] >= temp["W"] and curr["R"] >= temp["R"] and curr["E"] >= temp["E"] and curr["Q"] >= temp["Q"]:
                print(counter)
                min_ = min(counter,min_)
                while left <= i:
                    curr[s[left]] -= 1
                    if curr[s[left]] == 0:
                        del curr[s[left]]
                    left += 1
                    if temp[s[left - 1]] > 0 and temp[s[left - 1]] > curr[s[left -1]]:
                        counter -= 1
                        break 
                    counter -= 1
                    min_ = min(counter,min_)
                    
            
        return min_