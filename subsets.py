class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(temp=[],start = -1):
            result.append(temp[:])
           
            for i in range(start + 1,len(nums)):
                temp.append(nums[i])
                backtrack(temp,i)
                temp.pop()

        backtrack()
        return result