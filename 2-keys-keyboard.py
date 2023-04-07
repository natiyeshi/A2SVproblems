class Solution:
    def minSteps(self, n: int) -> int:
        result = float("inf")
        def backtrack(num = 2,counter = 2,copy = 1):
            nonlocal result
            if num >= n: 
                if num == n: 
                    result = min(result,counter)
                return
            backtrack(num + copy,counter + 1,copy)
            backtrack(num * 2,counter + 2,num)
        backtrack()
        if result == float("inf"): result = 0
        return result