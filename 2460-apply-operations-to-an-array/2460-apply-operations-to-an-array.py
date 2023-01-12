class Solution(object):
    def applyOperations(self, nums):
        c = 0
        arr = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] == 0:
                c += 1
            else:
                arr.append(nums[i])
        if nums[-1] == 0:
            c += 1
        else:
            arr.append(nums[-1])
      
        for i in range(c):
            arr.append(0)
            
        return arr
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        