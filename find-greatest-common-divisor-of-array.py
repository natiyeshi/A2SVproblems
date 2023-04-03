class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)

        def gcf(a,b):
            if b == 0:
                return a
            return gcf(b, a % b)
        return gcf(a,b)