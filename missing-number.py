class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        i = 0
        while i < len(nums):
            if nums[i] == -1 or nums[i] == i:
                i += 1
                continue
            nums[nums[i]] , nums[i] = nums[i] , nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] == -1:
                return i