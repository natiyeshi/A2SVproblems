class Solution(object):
    def rotate(self,nums, k):
                 a = k % len(nums)
                 l = len(nums) - a
                 nums[:] = nums[l:] + nums[:l]
        
