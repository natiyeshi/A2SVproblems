class Solution(object):
    def minimumRecolors(self, blocks, k):
        
        
        
        _min = len(blocks)
        
        
        for i in range(len(blocks) - k + 1):
            c = 0
            
            for j in blocks[i:i+k]:
                if j != "B":
                    c += 1                    
            _min = min(_min,c)
        
        return _min
        
        
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        