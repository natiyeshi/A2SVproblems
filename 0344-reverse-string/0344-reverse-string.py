class Solution(object):
    def reverseString(self, s,left = 0,right = -1):
        
        if left >= len(s) // 2:
            return 
        s[left], s[right] = s[right],s[left]
        self.reverseString(s,left + 1,right - 1)
        return

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        