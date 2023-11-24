class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for ind,val in enumerate(nums):
            if target - val in d:
                return [ind,d[target - val]]
            d[val] = ind
        