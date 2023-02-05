class Solution(object):
    def rangeSum(self, nums, n, left, right):
        
        sums = []
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sums.append(sum(nums[i:j+1]))
                
        sums.sort()
        
        return sum(sums[left - 1:right]) % (10**9 + 7)
        
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        