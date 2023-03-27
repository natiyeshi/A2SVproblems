class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[i] != -1:
                if nums[nums[i] - 1] == nums[i]:
                    ans.append(nums[i])
                    nums[i] = -1
                    i += 1
                else:
                    nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]
            else: i += 1
        return ans