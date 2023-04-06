class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_ = 0
        def backtrack(temp = 0,m = 0,st = 0):
            nonlocal max_
            counter[m] += 1
            max_ = max(max_,m)
            if temp == len(nums):
                return
            for i in range(st,len(nums)):
                last = m
                m |= nums[i]
                backtrack(temp + 1,m,i + 1)
                m = last
        backtrack()
        return counter[max_]