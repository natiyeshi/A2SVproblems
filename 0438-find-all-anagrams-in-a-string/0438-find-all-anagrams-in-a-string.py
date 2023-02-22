class Solution(object):
    def findAnagrams(self, s, p):
        pd = Counter(p)        
        wd = Counter(s[:len(p)])

        arr = []
        
        for i in range(len(s) - len(p)):
            if wd == pd:
                arr.append(i)
            wd[s[i+len(p)]] += 1   
            wd[s[i]] -= 1
            if wd[s[i]] == 0:
                del wd[s[i]]
                
        if wd == pd:
            arr.append(len(s) - len(p))
          
        return arr
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        