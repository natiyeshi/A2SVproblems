class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapify(heap)
        while len(heap) > 1:
            temp = -heapq.heappop(heap) - (-heapq.heappop(heap))
            if temp > 0: heapq.heappush(heap,-temp)
        return 0 if not heap else -heap[0]