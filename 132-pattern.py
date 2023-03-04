class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        rmin = []
        for i in nums:
            if not rmin:
                rmin.append(i)
            else:
                rmin.append(min(rmin[-1],i))
        stack = []
        for i in range(len(nums) - 1,-1,-1):
            while stack and stack[-1] < nums[i]:
                temp = stack.pop()
                if nums[i] > temp > rmin[i]:
                    return True
            stack.append(nums[i])
        return False