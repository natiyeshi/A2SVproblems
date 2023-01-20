class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        ind = []
        for i in range(len(nums)):
            if nums[i] == target:
                ind.append(i)
        return ind
            
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        