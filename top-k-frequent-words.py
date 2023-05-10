class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        words = list(set(words))
        heap = []
        for word in words:
            heapq.heappush(heap,[count[word],word])
        for i in range(len(heap)):
            heap[i][0] *= -1 
        heapify(heap)
        result = []
        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        
        return result