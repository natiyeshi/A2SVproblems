class Solution(object):
    def missingNumber(self, nums):
        
        for i in range(len(nums)):
            if i not in nums:
                return i
            if i + 1 not in nums:
                return i + 1
        
        """
        :type nums: List[int]
        :rtype: int
        """