class Solution(object):
    def removeDuplicates(self, nums):
        ar = []
        ma = nums[-1] + 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                ar.append(i)
        for i in ar:
            nums[i] = ma
        nums.sort()
        
        return  len(nums) - len(ar)
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        