class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []

        for i,val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                result[stack.pop()] = val
            stack.append(i)
        stack.reverse()
        sptr = 0
        nptr = 0
        while sptr < len(stack) and nptr < len(nums):
            # print(nums[sptr],nums[nptr])
            if nums[stack[sptr]] < nums[nptr]:
                result[stack[sptr]] = nums[nptr]
                sptr += 1
            else:
                nptr += 1
        return result