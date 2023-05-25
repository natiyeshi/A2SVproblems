class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 5: return 0
        return max(nums[1:(len(nums) - 3)]) - nums[0]