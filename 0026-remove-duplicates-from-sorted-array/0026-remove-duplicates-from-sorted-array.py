class Solution(object):
    def removeDuplicates(self, nums):
        pl = 0
        sec = 0
        c = 0
        # if len(nums) == 1:
        #     return 1
        # if len(nums) == 2:
        #     if nums[0] == nums[1]:
        #         return 1
        #     return 2
        while sec < len(nums):
            
            if sec == 0 or nums[sec - 1] != nums[sec]:
                nums[pl] = nums[sec]
                pl += 1
                c += 1
            sec += 1    
            
        return  pl
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        