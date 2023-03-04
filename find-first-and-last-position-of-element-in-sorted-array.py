class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = bisect_left(nums,nums[mid])
                right = bisect_right(nums,nums[mid])
                result = [left,right - 1]
                break
        return result