class Solution(object):
    def sortArrayByParity(self, nums):
        ch = []
        for i in nums:
            if i % 2 != 0:
                ch.append(i)
            else:
                ch.insert(0,i)
        return ch
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        