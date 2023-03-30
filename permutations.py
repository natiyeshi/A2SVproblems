class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(temp = [],s = 0):
            if len(temp) == len(nums):
                result.append(temp[:])
                return
            for i in range(len(nums)):
                if s & (1 << i) == 0:
                    temp.append(nums[i])
                    s |= 1 << i
                    backtrack(temp,s)
                    s &= ~(1 << i)
                    temp.pop()
        backtrack()
        return result