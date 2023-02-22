class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp = set()
        left = 0
        max_ = 0
        
        for i in range(len(s)):
            if s[i] not in temp:
                temp.add(s[i])
            else:
                while s[i] in temp:
                    temp.remove(s[left])
                    left += 1
                temp.add(s[i])
            max_ = max(max_, i - left + 1)

        return max_
        
        """
        :type s: str
        :rtype: int
        """
        