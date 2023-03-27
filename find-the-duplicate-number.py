class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        greater = len(nums) + 1
        less = 0
        for i in range(len(nums)):
            if greater > nums[i] > less:
                temp1 = temp2 = 0
                for j in range(len(nums)):
                    if i != j and nums[i] == nums[j]:
                        return nums[i]
                    elif nums[i] > nums[j]: temp1 += 1 
                    elif nums[j] > nums[i]: temp2 += 1
                if temp1 > nums[i] - 1:
                    greater = nums[i]
                else:
                    less = nums[i]