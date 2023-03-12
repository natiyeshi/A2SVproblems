class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        temp = nums[-1]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > temp:
                left = mid + 1
            else:
                right = mid - 1
        return nums[right + 1]