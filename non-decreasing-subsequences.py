class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def backtrack(arr = [],curr = 0):
             for i in range(curr,len(nums)):
                j = i + 1
                arr.append(nums[i]) 
                if len(arr) > 1 and arr[-1] < arr[-2]:
                    arr.pop()
                    continue
                if len(arr) > 1 and tuple(arr) not in result:
                    result.add(tuple(arr))
                while j < len(nums):
                    backtrack(arr,j)
                    j += 1
                arr.pop()
        backtrack()
        return result