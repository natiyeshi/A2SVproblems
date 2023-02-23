class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        total=0
        k = len(nums)+1
        for i in range(len(nums)):
            total += nums[i]
            while total >=target:
                k =  min((i-l)+1,k)
                total -= nums[l]
                l +=1
        if k != len(nums)+1:
            return k
        else:
            return 0
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        