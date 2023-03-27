class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        max_ = max(nums)
        min_ = min(nums)
        for i in range(max_,min_-1,-1):
            if i in count:
                k -= count[i]
            if k < 1:
                return i