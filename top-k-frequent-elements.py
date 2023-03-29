class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        count = dict(sorted(count.items(),key=lambda item:item[1],reverse=True))
        for i in count:
            result.append(i)
            if len(result) == k:
                break
        return result