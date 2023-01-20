class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counter = []
        
        for cell in nums:
            c = 0
            for val in nums:
                if cell > val: 
                    c += 1
            counter.append(c)
        return counter
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        