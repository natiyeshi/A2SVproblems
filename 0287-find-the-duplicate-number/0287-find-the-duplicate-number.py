class Solution(object):
    def findDuplicate(self, nums):
        
        count = Counter(nums)
        for key in count:
            if count[key] > 1:
                return key
        
        """
        :type nums: List[int]
        :rtype: int
        """
        