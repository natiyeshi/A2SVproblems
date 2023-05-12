class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heap = []
        for i in piles:
            heapq.heappush(heap,-i)
        while k:
            temp = -heapq.heappop(heap)
            temp -= temp // 2
            heapq.heappush(heap,-temp)
            k -= 1
        return -sum(heap)