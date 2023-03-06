class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        if citations[-1] == 0:
            return 0
        while left < right:
            mid = (left + right) // 2
            if len(citations) - mid <= citations[mid]:
                right = mid
                print(right)
            else:
                left = mid + 1
                
        return len(citations) - right