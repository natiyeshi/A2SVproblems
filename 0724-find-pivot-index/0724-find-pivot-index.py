class Solution(object):
    def pivotIndex(self, nums):
        
        _sum = sum(nums)
        t = 0
        for i,val in enumerate(nums):
            if t * 2 == _sum - val:
                return i
            t += val
        
        return -1    
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        