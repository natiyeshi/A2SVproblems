class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0: nums[i] = 0
            else: nums[i] = 1
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
        counter = Counter(preSum)
        result = 0
        for item in preSum:
            if item >= k:
                result += counter[item - k]
        return result