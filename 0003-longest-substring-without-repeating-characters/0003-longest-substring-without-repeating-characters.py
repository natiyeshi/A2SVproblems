class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = set()
        left = 0
        _max = 0
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[i])
            _max = max(_max,len(sub))
        
        return _max
        """
        :type s: str
        :rtype: int
        """
        