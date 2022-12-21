class Solution(object):
    def longestCommonPrefix(self, strs):
        ind = ""
        j = 0
        length = len(strs[0])
        for i in strs:
            if len(i) < length:
                length = len(i)
        for i in range(length):
            f = strs[0][i]
            for itr in strs:
                if f != itr[j]:
                    return ind
            ind += f
            j += 1
        return ind
                
            
                
                    
            
    
        """
        :type strs: List[str]
        :rtype: str
        """
        