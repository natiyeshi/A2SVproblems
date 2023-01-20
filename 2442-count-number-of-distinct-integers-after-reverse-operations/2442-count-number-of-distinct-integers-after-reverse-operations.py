class Solution(object):
    def countDistinctIntegers(self, nums):
        length = len(nums)
        i = 0;
        while i < length:
            string = str(nums[i])
            string = string[::-1]
            num = int(string)
            nums.append(num)
            i += 1
        s = set(nums)
        return len(s)
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        