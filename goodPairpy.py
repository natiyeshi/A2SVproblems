class Solution(object):
    def numIdenticalPairs(self, nums):
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if i < j and nums[i] == nums[j]:
                    c += 1
        return c

        """
        :type nums: List[int]
        :rtype: int
        """
