class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result ,i= 0,0
        while i < len(nums):
            if nums[i] < 1 or len(nums) < nums[i] or nums[i] == i + 1:
                i += 1
                continue
            if nums[nums[i] - 1] == nums[i]:
                i += 1
                continue
            nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i + 1
        return max(nums) + 1