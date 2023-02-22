class Solution(object):
    def findMaxAverage(self, nums, k):
        max_ = float('-inf')
        pointer = k 
        preSum = [0]
        
        for i in nums:
            preSum.append(preSum[-1] + i)
        
        if k == len(nums):
            return sum(nums) / (k * 1.0)
        while pointer < len(preSum):
            temp = (preSum[pointer] - preSum[pointer - k ] ) / ( k * 1.0 )
            max_ = max(temp,max_)
            pointer += 1
            
            
        return max_
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        