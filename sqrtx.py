class Solution:
    def mySqrt(self, x: int) -> int:
        end = x // 2
        start = 0
        if x == 1: return 1
        while start <= end:
            mid = (start + end) // 2
            sqr = mid ** 2
            if sqr < x:
                start = mid + 1
            elif sqr > x:
                end = mid - 1
            else:
                return mid
        return start - 1