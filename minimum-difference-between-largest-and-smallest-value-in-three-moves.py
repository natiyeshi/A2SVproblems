class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 5: return 0
        one = nums[len(nums) - 4] - nums[0]
        two = nums[-1] - nums[3] 
        temp = one
        if len(nums) > 5:
            temp = min(nums[-2] - nums[2],nums[-3] - nums[1])
        else:
            temp = nums[-2] - nums[2]
        return min(one,two,temp)