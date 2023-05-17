class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        for temp in matrix:
            result.extend(temp)
        heapify(result)
        return heapq.nsmallest(k,result)[-1]