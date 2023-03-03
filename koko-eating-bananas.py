class Solution:
    def check_k(self,piles,k,h):
        sum_ = 0
        for i in piles:
            temp = i // k
            if i % k != 0:
                 temp += 1 
            sum_+=temp
        return sum_ <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = 0
        while left <= right:
            mid = (left + right ) // 2
            if self.check_k(piles,mid,h):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result