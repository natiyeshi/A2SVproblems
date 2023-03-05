class Solution:
    def divide(self,nums,div,tre):
        sum_ = 0
        for i in nums:
            sum_ += ceil(i / div)
        return sum_ <= tre

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if self.divide(nums,mid,threshold):
                right = mid - 1
            else:
                left = mid + 1
        return right + 1