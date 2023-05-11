class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                temp = [nums1[i],nums2[j]]
                if len(heap) < k:
                    heapq.heappush(heap,(-(nums1[i]+nums2[j]),temp))
                else:
                    if -heap[0][0] < nums1[i] + nums2[j]:
                        break
                    heapq.heappushpop(heap,(-(nums1[i] + nums2[j]),temp))

        temp = [x for i,x in heap]
        
        return temp