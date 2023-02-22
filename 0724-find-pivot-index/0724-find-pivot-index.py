class Solution(object):
    def pivotIndex(self, nums):
        
        leftPre = [0]
        rightPre = [0]
        for i in nums:
            leftPre.append(leftPre[-1] + i)
        
        for i,val in enumerate(leftPre):
            if i == 0: continue
            if leftPre[i - 1] == leftPre[-1] - val:
                return i - 1
            
        return -1    
        
        
        
        
        
        # left = 0
        # right = len(nums)
        # leftArr = nums[0]
        # rightArr = nums[-1]
        # while left + 1 != right:
        #     if leftArr > rightArr:
        #         right -= 1
        #         rightArr += nums[right]
        #     else:
        #         left += 1
        #         leftArr += nums[left]
        # if rightArr != leftArr and left != 0:
        #     return -1
        # return left
            
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        