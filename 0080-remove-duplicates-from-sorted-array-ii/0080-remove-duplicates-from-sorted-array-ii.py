class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        
        ptr1 = 0
        ptr2 = 1
        ptr3 = 2
        k = 0
        while ptr3 < len(nums):
            if nums[ptr1] == nums[ptr2] == nums[ptr3]:
                nums[ptr3] = nums[-1] + 1
                ptr3 += 1
                k += 1
            else:
                ptr3 += 1
                ptr2 = ptr3 - 1
                ptr1 = ptr2 - 1
        nums.sort()
        
        return len(nums) - k 
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        